from datetime import datetime
from typing import List

from Domain.deleteOperationCascade import DeleteOperationCascade
from Domain.multiDeleteOperation import MultiDeleteOperation
from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.updateOperation import UpdateOperation
from Domain.reservation import Reservation
from Exceptions.movieError import MovieError
from Exceptions.reservationError import ReservationError
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService
from myTools.mySorted import mySorted


class ReservationService:

    def __init__(self, reservationRepository: Repository, movieRepository: Repository,
                 cardRepository: Repository, undoRedoService: UndoRedoService):
        self.movieRepository = movieRepository
        self.cardRepository = cardRepository
        self.reservationRepository = reservationRepository
        self.undoRedoService = undoRedoService

    def addReservation(self, idReservation: str, idMovie: str, idCard: str, date: str, hour: str) -> None:
        movie = self.movieRepository.read(idMovie)
        card = self.cardRepository.read(idCard)
        if self.movieRepository.read(movie.idEntity) is None:
            raise MovieError("No film with that id!")
        if movie.inProgram == "no":
            raise ReservationError("Reservation can not be done because the movie is not in program!")
        pointsCumulated = self.acumulatePoints(idMovie)
        if card is not None:
            card.points += pointsCumulated
            self.cardRepository.update(card)
        reservation = Reservation(idReservation, idMovie, idCard, date, hour)
        self.reservationRepository.add(reservation)
        self.undoRedoService.addUndoOperation(AddOperation(self.reservationRepository, reservation))

    def deleteReservation(self, idReservation: str) -> None:
        deletedReservation = self.reservationRepository.read(idReservation)
        self.reservationRepository.delete(idReservation)
        self.undoRedoService.addUndoOperation(DeleteOperation(self.reservationRepository, deletedReservation))

    def updateReservation(self, idReservation: str, idMovie: str, idCard: str, date: str, hour: str) -> None:
        oldReservation = self.reservationRepository.read(idReservation)
        movie = self.movieRepository.read(idMovie)
        card = self.cardRepository.read(idCard)
        if movie.inProgram == "no":
            raise ReservationError("Reservation can not be done because the movie is not in program!")
        pointsEarned = self.acumulatePoints(idMovie)
        if card is not None:
            card['pointsCumulated'] += pointsEarned
            self.cardRepository.update(card)
        reservation = Reservation(idReservation, idMovie, idCard, date, hour)
        self.reservationRepository.update(reservation)
        self.undoRedoService.addUndoOperation(UpdateOperation(self.reservationRepository, oldReservation, reservation))

    def getAll(self) -> List[Reservation]:
        return self.reservationRepository.read()

    def acumulatePoints(self, idMovie: str) -> int:
        """
        returns the points cumulated from the movie price
        """
        movie = self.movieRepository.read(idMovie)
        moviePrice = movie.ticketPrice
        pointsCumulated = int(0.1*moviePrice)
        return pointsCumulated

    def orderMoviesByReservationsReverse(self) -> List:
        """
        orders the movies in reverse by the number of reservations
        """
        filmeRezervate = {film.idEntitate: 0 for film in
                          self.filmRepository.read()}
        for rezervare in self.rezervareRepository.read():
            filmeRezervate[rezervare.idFilm] += 1
        return list(map(lambda x: self.filmRepository.read(x), mySorted(
            list(filmeRezervate), key=lambda x: filmeRezervate[x],
            reverse=True)))

    def afisareRezervariIntervalOrar(self, ora1: datetime, ora2: datetime,
                                     rezervari: list, rezultat: list) -> List:
        """
        Returneaza o lista cu rezervarile dintr-un anumit interval orar
        :param ora1: prima ora
        :param ora2: a doua ora
        :param rezervari: rezervarile existente
        :param rezultat: o lista cu rezervarile din intervalul specificat
        :return: o lista cu rezervarile dintre cele 2 ore date
        """
        """
        return list(filter(lambda x: x if ora1 <= datetime.strptime(x.ora,
                                                                    "%H:%M")
                           <= ora2 else None, self.rezervareRepository.read()))
                           """
        if ora1 > ora2:
            ora1, ora2 = ora2, ora1
        if len(rezervari) == 1:
            if ora1 <= datetime.strptime(rezervari[0].ora, "%H:%M") <= ora2:
                rezultat.append(rezervari[0])
        else:
            if ora1 <= datetime.strptime(rezervari[0].ora, "%H:%M") <= ora2:
                rezultat.append(rezervari[0])
            self.afisareRezervariIntervalOrar(ora1, ora2, rezervari[1:],
                                              rezultat)
        return rezultat

    def stergereRezervariIntervalZile(self, data1: datetime, data2: datetime)\
            -> List:
        """
        Sterge rezervarile dintr-un anumit interval de zile speicificat
        :param data1: prima data
        :param data2: a doua data
        :return: o lista cu rezervarile ramase
        """
        rezervariDeSters = list(filter(lambda x: x if data1 <=
                                       datetime.strptime(x.data,
                                                         "%d.%m.%Y")
                                       <= data2 else None,
                                       self.rezervareRepository.read()))
        for rezervare in rezervariDeSters:
            self.rezervareRepository.sterge(rezervare.idEntitate)

        self.undoRedoService.addUndoOperation(MultiDeleteOperation(
            self.rezervareRepository, rezervariDeSters))
        return self.rezervareRepository.read()

    def stergereInCascada(self, idFilm: str) -> None:
        """
        Sterge filmul cu id-ul introdus si toate
        rezervarile facute la acest film
        :param idFilm: id-ul filmului de sters
        :return: None
        """
        cascade = []

        if self.filmRepository.read(idFilm) is None:
            raise FilmError("Nu exista un film cu id-ul "
                            "specificat de sters !")

        for rezervare in self.rezervareRepository.read():
            if rezervare.idFilm == idFilm:
                cascade.append(rezervare)
                self.rezervareRepository.sterge(rezervare.idEntitate)

        film = self.filmRepository.read(idFilm)
        cascade.append(film)
        self.filmRepository.sterge(film.idEntitate)

        self.undoRedoService.addUndoOperation(CascadaDeleteOperation(
            self.filmRepository, self.rezervareRepository, cascade))

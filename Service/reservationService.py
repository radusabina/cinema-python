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
        reservedMovies = {movie.idEntity: 0 for movie in self.movieRepository.read()}
        for reservation in self.reservationRepository.read():
            reservedMovies[reservation.idMovie] += 1
        return list(map(lambda x: self.movieRepository.read(x), mySorted(
            list(reservedMovies), key=lambda x: reservedMovies[x], reverse=True)))

    def reservationsBetweenHours(self, hour1: datetime, hour2: datetime,
                                 reservations: list, result: list) -> List:
        """
        returns a list with the reservations between two hours
        """
        if hour1 > hour2:
            hour1, hour2 = hour2, hour1
        if len(reservations) == 1:
            if hour1 <= datetime.strptime(reservations[0].hour, "%H:%M") <= hour2:
                result.append(reservations[0])
        else:
            if hour1 <= datetime.strptime(reservations[0].hour, "%H:%M") <= hour2:
                result.append(reservations[0])
            self.reservationsBetweenHours(hour1, hour2, reservations[1:], result)
        return result

    def deleteReservationsBetweenDates(self, date1: datetime, date2: datetime) -> List:
        """
        deletes the reservations between two dates
        """
        reservationsToDelete = list(filter(lambda x: x if date1 <= datetime.strptime(x.date, "%d.%m.%Y")
                                           <= date2 else None, self.reservationRepository.read()))
        for reservation in reservationsToDelete:
            self.reservationRepository.delete(reservation.idEntity)

        self.undoRedoService.addUndoOperation(MultiDeleteOperation(self.reservationRepository, reservationsToDelete))
        return self.reservationRepository.read()

    def deleteInCascade(self, idMovie: str) -> None:
        cascade = []
        if self.movieRepository.read(idMovie) is None:
            raise MovieError("There is no film with that id!")

        for reservation in self.reservationRepository.read():
            if reservation.idFilm == idMovie:
                cascade.append(reservation)
                self.reservationRepository.delete(reservation.idEntity)

        movie = self.movieRepository.read(idMovie)
        cascade.append(movie)
        self.movieRepository.delete(movie.idEntity)

        self.undoRedoService.addUndoOperation(DeleteOperationCascade(self.movieRepository, self.reservationRepository,
                                                                     cascade))

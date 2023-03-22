import datetime

from Domain.clientCard import ClientCard
from Domain.clientCardValidator import ClientCardValidator
from Domain.movie import Movie
from Domain.movieValidator import MovieValidator
from Domain.reservation import Reservation
from Repository.repositoryJson import RepositoryJson
from Service.clientCardService import ClientCardService
from Service.movieService import MovieService
from Service.reservationService import ReservationService
from Service.undoRedoService import UndoRedoService
from utils import clear_file


def testMovieService():
    filename = "testMovieService.json"
    clear_file(filename)
    movieValidator = MovieValidator()
    movieRepository = RepositoryJson("testMovieService.json")
    undoRedo = UndoRedoService()
    movieService = MovieService(movieRepository, movieValidator, undoRedo)
    movieService.addMovie("1", "Titanic", 1997, 14.99, "no")
    assert len(movieService.getAll()) == 1
    movieService.addMovie("2", "The nun", 2019, 0, "yes")
    assert len(movieService.getAll()) == 2
    movieService.updateMovie("1", "Dune", 2021, 18.99, "yes")
    assert len(movieService.getAll()) == 2
    movieService.deleteMovie("1")
    assert len(movieService.getAll()) == 1
    movieService.addMovie("3", "Home Alone", 1999, 20, "yes")


def testCardService():
    filename = "testCardService.json"
    clear_file(filename)
    cardValidator = ClientCardValidator()
    cardRepository = RepositoryJson("testCardService.json")
    undoRedo = UndoRedoService()
    cardService = ClientCardService(cardRepository, cardValidator, undoRedo)
    cardService.addCard("1", "Leu", "Ion", "5043008624836", "30.04.2004", "17.11.2021", 30)
    assert len(cardService.getAll()) == 1
    cardService.addCard("2", "Barsan", "Andra", "6780924985634", "24.09.1978", "13.11.2021", 0)
    assert len(cardService.getAll()) == 2
    cardService.updateCard("2", "Bacanu", "Gheorghe", "5039876435789", "04.04.1999", "17.11.2021", 30)
    assert len(cardService.getAll()) == 2
    cardService.deleteCard("2")
    assert len(cardService.getAll()) == 1


def testReservationService():
    filename = "testReservationService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    reservationRepository = RepositoryJson("testReservationService.json")
    cardRepository = RepositoryJson("testCardService.json")
    filmRepository = RepositoryJson("testMovieService.json")
    reservationService = ReservationService(reservationRepository, filmRepository, cardRepository, undoRedo)
    reservationService.addReservation("1", "2", "1", "12.03.2021", "12:00")
    assert len(reservationService.getAll()) == 1
    reservationService.updateReservation("1", "2", "0", "14.09.2021", "20:00")
    assert len(reservationService.getAll()) == 1
    reservationService.deleteReservation("1")
    assert len(reservationService.getAll()) == 0


def testOrderedCardsByPointsReverse():
    filename = "testCardService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    cardValidator = ClientCardValidator()
    cardRepository = RepositoryJson("testCardService.json")
    cardService = ClientCardService(cardRepository, cardValidator, undoRedo)
    cardService.addCard("5", "Popescu", "Carmen", "6986524739821", "14.08.1988", "17.04.2020", 0)
    cardService.addCard("6", "Ionescu", "Lidia", "6986463312421", "23.11.1988", "02.03.2021", 8)
    lista = cardService.orderedCardsByPointsReverse()
    assert lista[0] == ClientCard("6", "Ionescu", "Lidia", "6986463312421", "23.11.1988", "02.03.2021", 8)
    assert lista[1] == ClientCard("5", "Popescu", "Carmen", "6986524739821", "14.08.1988", "17.04.2020", 0)


def testReservationsBetweenHours():
    filename = "testReservationService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    reservationRepository = RepositoryJson("testReservationService.json")
    cardRepository = RepositoryJson("testCardService.json")
    movieRepository = RepositoryJson("testMovieService.json")
    reservationService = ReservationService(reservationRepository, movieRepository, cardRepository, undoRedo)
    reservationService.addReservation("1", "2", "0", "12.03.2021", "14:00")
    reservationService.addReservation("2", "2", "0", "17.12.2021", "20:00")
    reservationService.addReservation("3", "2", "0", "04.01.2021", "18:00")
    hour1 = datetime.datetime.strptime("12:00", "%H:%M")
    hour2 = datetime.datetime.strptime("18:00", "%H:%M")
    result = []
    reservations = reservationService.getAll()
    reservationService.reservationsBetweenHours(hour1, hour2, reservations, result)
    assert len(result) == 2
    assert result[0] == Reservation("1", "2", "0", "12.03.2021", "14:00")
    assert result[1] == Reservation("3", "2", "0", "04.01.2021", "18:00")




def testSearchTextMovie():
    filename = "testMovieService.json"
    clear_file(filename)
    movieValidator = MovieValidator()
    movieRepository = RepositoryJson("testMovieService.json")
    undoRedo = UndoRedoService()
    movieService = MovieService(movieRepository, movieValidator, undoRedo)
    movieService.addMovie("1", "Film1", 1997, 15.0, "yes")
    movieService.addMovie("2", "Film2", 2000, 19.99, "no")
    movieService.addMovie("3", "Film3", 2019, 14.99, "no")
    result = movieService.searchTextMovie("no")
    assert len(result) == 2
    assert result[0] == Movie("2", "Film2", 2000, 19.99, "no")
    assert result[1] == Movie("3", "Film3", 2019, 14.99, "no")
    result = movieService.searchTextMovie("9")
    assert len(result) == 3
    assert result[0] == Movie("1", "Film1", 1997, 15.0, "yes")
    assert result[1] == Movie("2", "Film2", 2000, 19.99, "no")
    assert result[2] == Movie("3", "Film3", 2019, 14.99, "no")


def testSearchTextCard():
    filename = "testCardService.json"
    clear_file(filename)
    cardValidator = ClientCardValidator()
    cardRepository = RepositoryJson("testCardService.json")
    undoRedo = UndoRedoService()
    cardService = ClientCardService(cardRepository, cardValidator, undoRedo)
    cardService.addCard("1", "Nume1", "Prenume1", "6023481397131", "12.03.1999", "21.11.2021", 0)
    cardService.addCard("2", "Nume2", "Prenume2", "6023748201382", "17.12.1867", "14.04.2020", 0)
    cardService.addCard("3", "Nume3", "Prenume3", "5130193018319", "15.01.2000", "20.12.2020", 0)
    result = cardService.searchTextCard("2020")
    assert len(result) == 2
    assert result[0] == ClientCard("2", "Nume2", "Prenume2", "6023748201382", "17.12.1867", "14.04.2020", 0)
    assert result[1] == ClientCard("3", "Nume3", "Prenume3", "5130193018319", "15.01.2000", "20.12.2020", 0)
    result = cardService.searchTextCard("Nume3")
    assert len(result) == 1
    assert result[0] == ClientCard("3", "Nume3", "Prenume3", "5130193018319", "15.01.2000", "20.12.2020", 0)


def testDeleteReservationsBetweenDates():
    filename = "testReservationService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    reservationRepository = RepositoryJson("testReservationService.json")
    cardRepository = RepositoryJson("testCardService.json")
    movieRepository = RepositoryJson("testMovieService.json")
    reservationService = ReservationService(reservationRepository, movieRepository, cardRepository, undoRedo)
    filename = "testMovieService.json"
    clear_file(filename)
    movieValidator = MovieValidator()
    movieRepository = RepositoryJson("testMovieService.json")
    undoRedo = UndoRedoService()
    movieService = MovieService(movieRepository, movieValidator, undoRedo)
    movieService.addMovie("1", "Film1", 1997, 15.0, "yes")
    movieService.addMovie("2", "Film2", 2000, 19.99, "yes")
    reservationService.addReservation("1", "1", "0", "12.03.2021", "14:00")
    reservationService.addReservation("2", "2", "0", "17.12.2021", "20:00")
    reservationService.addReservation("3", "2", "0", "04.01.2021", "18:00")
    date1 = datetime.datetime.strptime("01.01.2021", "%d.%m.%Y")
    date2 = datetime.datetime.strptime("01.04.2021", "%d.%m.%Y")
    result = reservationService.deleteReservationsBetweenDates(date1, date2)
    assert len(result) == 1
    assert result[0] == Reservation("2", "2", "0", "17.12.2021", "20:00")


def testAddPoints():
    filename = "testCardService.json"
    clear_file(filename)
    cardValidator = ClientCardValidator()
    cardRepository = RepositoryJson("testCardService.json")
    undoRedo = UndoRedoService()
    cardService = ClientCardService(cardRepository, cardValidator, undoRedo)
    cardService.addCard("1", "Nume1", "Prenume1", "6023481397131", "12.03.1999", "21.11.2021", 0)
    cardService.addCard("2", "Nume2", "Prenume2", "6023748201382", "17.12.1867", "14.04.2020", 5)
    cardService.addCard("3", "Nume3", "Prenume3", "5130193018319", "15.01.2000", "20.12.2020", 10)
    date1 = datetime.datetime.strptime("01.01.1999", "%d.%m.%Y")
    date2 = datetime.datetime.strptime("31.12.2002", "%d.%m.%Y")
    result = cardService.addPoints(date1, date2, 10)
    assert len(result) == 2
    assert result[0] == ClientCard("1", "Nume1", "Prenume1", "6023481397131", "12.03.1999", "21.11.2021", 10)
    assert result[1] == ClientCard("3", "Nume3", "Prenume3", "5130193018319", "15.01.2000", "20.12.2020", 20)


def testAllServices():
    testMovieService()
    testCardService()
    testReservationService()
    testOrderedCardsByPointsReverse()
    testAddPoints()
    testSearchTextMovie()
    testDeleteReservationsBetweenDates()
    testReservationsBetweenHours()
    testSearchTextCard()

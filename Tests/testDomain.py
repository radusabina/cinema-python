from Domain.clientCard import ClientCard
from Domain.movie import Movie
from Domain.reservation import Reservation


def testMovie():
    movie = Movie("1", "Titanic", 1997, 15, "yes")
    assert movie.idEntity == "1"
    assert movie.title == "Titanic"
    assert movie.releaseYear == 1997
    assert movie.ticketPrice == 15
    assert movie.inProgram == "yes"


def testClientCard():
    card = ClientCard("1", "Simionescu", "Cosmin", "5682930245623", "12.03.1998", "16.11.2021", 80)
    assert card.idEntity == "1"
    assert card.name == "Simionescu"
    assert card.surname == "Cosmin"
    assert card.CNP == "5682930245623"
    assert card.birthDate == "12.03.1998"
    assert card.registrationDate == "16.11.2021"
    assert card.points == 80


def testReservation():
    reservation = Reservation("1", "3", "5", "12.03.2021", "12:00")
    assert reservation.idEntity == "1"
    assert reservation.idMovie == "3"
    assert reservation.idClientCard == "5"
    assert reservation.date == "12.03.2021"
    assert reservation.hour == "12:00"


def testAllDomains():
    testMovie()
    testClientCard()
    testReservation()

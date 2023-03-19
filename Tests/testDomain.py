from Domain.clientCard import CardClient
from Domain.movie import Film
from Domain.reservation import Rezervare


def testFilm():
    film = Film("1", "Titanic", 1997, 15, "da")
    assert film.idEntitate == "1"
    assert film.titlu == "Titanic"
    assert film.anAparitie == 1997
    assert film.pretBilet == 15
    assert film.inProgram == "da"


def testCardClient():
    card = CardClient("1", "Simionescu", "Cosmin", "5682930245623",
                      "12.03.1998", "16.11.2021", 80)
    assert card.idEntitate == "1"
    assert card.nume == "Simionescu"
    assert card.prenume == "Cosmin"
    assert card.CNP == "5682930245623"
    assert card.dataNasterii == "12.03.1998"
    assert card.dataInregistrarii == "16.11.2021"
    assert card.puncteCumulate == 80


def testRezervare():
    rezervare = Rezervare("1", "3", "5", "12.03.2021", "12:00")
    assert rezervare.idEntitate == "1"
    assert rezervare.idFilm == "3"
    assert rezervare.idCard == "5"
    assert rezervare.data == "12.03.2021"
    assert rezervare.ora == "12:00"


def testAllDomains():
    testFilm()
    testCardClient()
    testRezervare()

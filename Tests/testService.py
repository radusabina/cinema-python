import datetime

from Domain.clientCard import CardClient
from Domain.clientCardValidator import CardClientValidator
from Domain.movie import Film
from Domain.movieValidator import FilmValidator
from Domain.reservation import Rezervare
from Repository.repositoryJson import RepositoryJson
from Service.cardClientService import CardClientService
from Service.filmService import FilmService
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService
from utils import clear_file


def testFilmService():
    filename = "testFilmService.json"
    clear_file(filename)
    filmValidator = FilmValidator()
    filmRepository = RepositoryJson("testFilmService.json")
    undoRedo = UndoRedoService()
    filmService = FilmService(filmRepository, filmValidator, undoRedo)
    filmService.adaugaFilm("1", "Titanic", 1997, 14.99, "nu")
    assert len(filmService.getAll()) == 1
    filmService.adaugaFilm("2", "The nun", 2019, 0, "da")
    assert len(filmService.getAll()) == 2
    filmService.modificaFilm("1", "Dune", 2021, 18.99, "da")
    assert len(filmService.getAll()) == 2
    filmService.stergeFilm("1")
    assert len(filmService.getAll()) == 1
    filmService.adaugaFilm("3", "Home Alone", 1999, 20, "da")


def testCardService():
    filename = "testCardService.json"
    clear_file(filename)
    cardValidator = CardClientValidator()
    cardRepository = RepositoryJson("testCardService.json")
    undoRedo = UndoRedoService()
    cardService = CardClientService(cardRepository, cardValidator, undoRedo)
    cardService.adaugaCard("1", "Leu", "Ion", "5043008624836",
                           "30.04.2004", "17.11.2021", 30)
    assert len(cardService.getAll()) == 1
    cardService.adaugaCard("2", "Barsan", "Andra", "6780924985634",
                           "24.09.1978", "13.11.2021", 0)
    assert len(cardService.getAll()) == 2
    cardService.modificaCard("2", "Bacanu", "Gheorghe", "5039876435789",
                             "04.04.1999", "17.11.2021", 30)
    assert len(cardService.getAll()) == 2
    cardService.stergeCard("2")
    assert len(cardService.getAll()) == 1


def testServiceRezervare():
    filename = "testRezervareService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    rezervareRepository = RepositoryJson(
        "testRezervareService.json")
    cardRepository = RepositoryJson("testCardService.json")
    filmRepository = RepositoryJson("testFilmService.json")
    rezervareService = RezervareService(rezervareRepository,
                                        filmRepository, cardRepository,
                                        undoRedo)
    rezervareService.adaugaRezervare("1", "2", "1", "12.03.2021", "12:00")
    assert len(rezervareService.getAll()) == 1
    rezervareService.modificaRezervare("1", "2", "0", "14.09.2021", "20:00")
    assert len(rezervareService.getAll()) == 1
    rezervareService.stergeRezervare("1")
    assert len(rezervareService.getAll()) == 0


def testOrdonareDescCarduriDupaPuncte():
    filename = "testCardService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    cardValidator = CardClientValidator()
    cardRepository = RepositoryJson("testCardService.json")
    cardService = CardClientService(cardRepository, cardValidator, undoRedo)
    cardService.adaugaCard("5", "Popescu", "Carmen", "6986524739821",
                           "14.08.1988", "17.04.2020", 0)
    cardService.adaugaCard("6", "Ionescu", "Lidia", "6986463312421",
                           "23.11.1988", "02.03.2021", 8)
    lista = cardService.ordonareDescCarduriDupaPuncte()
    assert lista[0] == CardClient("6", "Ionescu", "Lidia", "6986463312421",
                                  "23.11.1988", "02.03.2021", 8)
    assert lista[1] == CardClient("5", "Popescu", "Carmen", "6986524739821",
                                  "14.08.1988", "17.04.2020", 0)


def testAfisareRezervariIntervalOrar():
    filename = "testRezervareService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    rezervareRepository = RepositoryJson(
        "testRezervareService.json")
    cardRepository = RepositoryJson("testCardService.json")
    filmRepository = RepositoryJson("testFilmService.json")
    rezervareService = RezervareService(rezervareRepository,
                                        filmRepository, cardRepository,
                                        undoRedo)
    rezervareService.adaugaRezervare("1", "2", "0", "12.03.2021", "14:00")
    rezervareService.adaugaRezervare("2", "3", "0", "17.12.2021", "20:00")
    rezervareService.adaugaRezervare("3", "2", "0", "04.01.2021", "18:00")
    ora1 = datetime.datetime.strptime("12:00", "%H:%M")
    ora2 = datetime.datetime.strptime("18:00", "%H:%M")
    rezultat = []
    rezervari = rezervareService.getAll()
    rezervareService.afisareRezervariIntervalOrar(ora1, ora2, rezervari,
                                                  rezultat)
    assert len(rezultat) == 2
    assert rezultat[0] == Rezervare("1", "2", "0", "12.03.2021", "14:00")
    assert rezultat[1] == Rezervare("3", "2", "0", "04.01.2021", "18:00")


def testOrdonareFilmeDescDupaRezervari():
    filename = "testRezervareService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    rezervareRepository = RepositoryJson(
        "testRezervareService.json")
    cardRepository = RepositoryJson("testCardService.json")
    filmRepository = RepositoryJson("testFilmService.json")
    rezervareService = RezervareService(rezervareRepository,
                                        filmRepository, cardRepository,
                                        undoRedo)
    rezervareService.adaugaRezervare("1", "2", "0", "12.03.2021", "14:00")
    rezervareService.adaugaRezervare("2", "3", "0", "17.12.2021", "20:00")
    rezervareService.adaugaRezervare("3", "3", "0", "04.01.2021", "18:00")
    rezultat = rezervareService.ordonareFilmeDescDupaRezervari()
    assert len(rezultat) == 2
    assert rezultat[1] == Film(idEntitate='2', titlu='The nun',
                               anAparitie=2019, pretBilet=0, inProgram='da')
    assert rezultat[0] == Film(idEntitate='3', titlu='Home Alone',
                               anAparitie=1999, pretBilet=20, inProgram='da')


def testCautareTextFilm():
    filename = "testFilmService.json"
    clear_file(filename)
    filmValidator = FilmValidator()
    filmRepository = RepositoryJson("testFilmService.json")
    undoRedo = UndoRedoService()
    filmService = FilmService(filmRepository, filmValidator, undoRedo)
    filmService.adaugaFilm("1", "Film1", 1997, 15.0, "da")
    filmService.adaugaFilm("2", "Film2", 2000, 19.99, "nu")
    filmService.adaugaFilm("3", "Film3", 2019, 14.99, "nu")
    rezultat = filmService.cautareTextFilm("nu")
    assert len(rezultat) == 2
    assert rezultat[0] == Film("2", "Film2", 2000, 19.99, "nu")
    assert rezultat[1] == Film("3", "Film3", 2019, 14.99, "nu")
    rezultat = filmService.cautareTextFilm("9")
    assert len(rezultat) == 3
    assert rezultat[0] == Film("1", "Film1", 1997, 15.0, "da")
    assert rezultat[1] == Film("2", "Film2", 2000, 19.99, "nu")
    assert rezultat[2] == Film("3", "Film3", 2019, 14.99, "nu")


def testCautareTextCard():
    filename = "testCardService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    cardValidator = CardClientValidator()
    cardRepository = RepositoryJson("testCardService.json")
    cardService = CardClientService(cardRepository, cardValidator, undoRedo)
    cardService.adaugaCard("1", "Nume1", "Prenume1", "6023481397131",
                           "12.03.1999", "21.11.2021", 0)
    cardService.adaugaCard("2", "Nume2", "Prenume2", "6023748201382",
                           "17.12.1867", "14.04.2020", 0)
    cardService.adaugaCard("3", "Nume3", "Prenume3", "5130193018319",
                           "15.01.2000", "20.12.2020", 0)
    rezultat = cardService.cautareTextCard("2020")
    assert len(rezultat) == 2
    assert rezultat[0] == CardClient("2", "Nume2", "Prenume2",
                                     "6023748201382", "17.12.1867",
                                     "14.04.2020", 0)
    assert rezultat[1] == CardClient("3", "Nume3", "Prenume3",
                                     "5130193018319", "15.01.2000",
                                     "20.12.2020", 0)
    rezultat = cardService.cautareTextCard("Nume3")
    assert len(rezultat) == 1
    assert rezultat[0] == CardClient("3", "Nume3", "Prenume3",
                                     "5130193018319", "15.01.2000",
                                     "20.12.2020", 0)


def testStergereRezervariIntervalZile():
    filename = "testRezervareService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    rezervareRepository = RepositoryJson(
        "testRezervareService.json")
    cardRepository = RepositoryJson("testCardService.json")
    filmRepository = RepositoryJson("testFilmService.json")
    rezervareService = RezervareService(rezervareRepository,
                                        filmRepository, cardRepository,
                                        undoRedo)
    filename = "testFilmService.json"
    clear_file(filename)
    filmValidator = FilmValidator()
    filmRepository = RepositoryJson("testFilmService.json")
    filmService = FilmService(filmRepository, filmValidator, undoRedo)
    filmService.adaugaFilm("1", "Film1", 1997, 15.0, "da")
    filmService.adaugaFilm("2", "Film2", 2000, 19.99, "da")
    rezervareService.adaugaRezervare("1", "1", "0", "12.03.2021", "14:00")
    rezervareService.adaugaRezervare("2", "2", "0", "17.12.2021", "20:00")
    rezervareService.adaugaRezervare("3", "2", "0", "04.01.2021", "18:00")
    data1 = datetime.datetime.strptime("01.01.2021", "%d.%m.%Y")
    data2 = datetime.datetime.strptime("01.04.2021", "%d.%m.%Y")
    rezultat = rezervareService.stergereRezervariIntervalZile(data1, data2)
    assert len(rezultat) == 1
    assert rezultat[0] == Rezervare("2", "2", "0", "17.12.2021", "20:00")


def testAdaugaValoarePuncte():
    filename = "testCardService.json"
    undoRedo = UndoRedoService()
    clear_file(filename)
    cardValidator = CardClientValidator()
    cardRepository = RepositoryJson("testCardService.json")
    cardService = CardClientService(cardRepository, cardValidator, undoRedo)
    cardService.adaugaCard("1", "Nume1", "Prenume1", "6023481397131",
                           "12.03.1999", "21.11.2021", 0)
    cardService.adaugaCard("2", "Nume2", "Prenume2", "6023748201382",
                           "17.12.1867", "14.04.2020", 5)
    cardService.adaugaCard("3", "Nume3", "Prenume3", "5130193018319",
                           "15.01.2000", "20.12.2020", 10)
    data1 = datetime.datetime.strptime("01.01.1999", "%d.%m.%Y")
    data2 = datetime.datetime.strptime("31.12.2002", "%d.%m.%Y")
    rezultat = cardService.adaugaValoarePuncte(data1, data2, 10)
    assert len(rezultat) == 2
    assert rezultat[0] == CardClient("1", "Nume1", "Prenume1", "6023481397131",
                                     "12.03.1999", "21.11.2021", 10)
    assert rezultat[1] == CardClient("3", "Nume3", "Prenume3", "5130193018319",
                                     "15.01.2000", "20.12.2020", 20)


def testAllServices():
    testFilmService()
    testCardService()
    testServiceRezervare()
    testOrdonareDescCarduriDupaPuncte()
    testAfisareRezervariIntervalOrar()
    testOrdonareFilmeDescDupaRezervari()
    testCautareTextFilm()
    testCautareTextCard()
    testStergereRezervariIntervalZile()
    testAdaugaValoarePuncte()

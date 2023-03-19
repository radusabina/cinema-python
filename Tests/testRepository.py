from Domain.clientCard import CardClient
from Domain.movie import Film
from Domain.reservation import Rezervare
from Repository.repositoryJson import RepositoryJson
from utils import clear_file


def testFilmRepository():
    repo = RepositoryJson("testFilmRepository.json")

    clear_file("testFilmRepository.json")
    repo.adauga(Film("1", "Titanic", 1997, 10, "da"))
    repo.adauga(Film("2", "Dune", 2021, 13, "da"))
    assert len(repo.read()) == 2
    assert repo.read("1").titlu == "Titanic"
    assert repo.read("1").anAparitie == 1997
    assert repo.read("1").pretBilet == 10
    assert repo.read("1").inProgram == "da"
    repo.modifica(Film("1", "Dune", 2021, 19.99, "da"))
    assert len(repo.read()) == 2
    assert repo.read("1").titlu == "Dune"
    assert repo.read("1").anAparitie == 2021
    assert repo.read("1").pretBilet == 19.99
    assert repo.read("1").inProgram == "da"
    repo.sterge("1")
    assert len(repo.read()) == 1
    repo.sterge("2")
    assert len(repo.read()) == 0


def testCardRepository():
    repo = RepositoryJson("testCardRepository.json")
    repo.adauga(CardClient("1", "Ureche", "Grigore", "5670429873323",
                           "29.04.1967", "14.12.2021", 30))
    assert len(repo.read()) == 1
    assert repo.read("1").nume == "Ureche"
    assert repo.read("1").prenume == "Grigore"
    assert repo.read("1").CNP == "5670429873323"
    assert repo.read("1").dataNasterii == "29.04.1967"
    assert repo.read("1").dataInregistrarii == "14.12.2021"
    assert repo.read("1").puncteCumulate == 30
    repo.modifica(CardClient("1", "Ban", "Betina", "6985678892531",
                             "28.05.2002", "14.03.2021", 0))
    assert len(repo.read()) == 1
    assert repo.read("1").nume == "Ban"
    assert repo.read("1").prenume == "Betina"
    assert repo.read("1").CNP == "6985678892531"
    assert repo.read("1").dataNasterii == "28.05.2002"
    assert repo.read("1").dataInregistrarii == "14.03.2021"
    assert repo.read("1").puncteCumulate == 0
    repo.sterge("1")
    assert len(repo.read()) == 0


def testRepositoryRezervare():
    repo = RepositoryJson("testRezervareRepository.json")
    repo.adauga(Rezervare("1", "2", "0", "17.11.2021", "13:00"))
    assert len(repo.read()) == 1
    assert repo.read("1").idEntitate == "1"
    assert repo.read("1").idFilm == "2"
    assert repo.read("1").idCard == "0"
    assert repo.read("1").data == "17.11.2021"
    assert repo.read("1").ora == "13:00"
    repo.modifica(Rezervare("1", "2", "0", "13.12.2021", "14:00"))
    assert len(repo.read()) == 1
    assert repo.read("1").idEntitate == "1"
    assert repo.read("1").idFilm == "2"
    assert repo.read("1").idCard == "0"
    assert repo.read("1").data == "13.12.2021"
    assert repo.read("1").ora == "14:00"
    repo.sterge("1")
    assert len(repo.read()) == 0


def testAllRepositories():
    testFilmRepository()
    testCardRepository()
    testRepositoryRezervare()

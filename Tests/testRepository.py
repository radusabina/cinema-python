from Domain.clientCard import ClientCard
from Domain.movie import Movie
from Domain.reservation import Reservation
from Repository.repositoryJson import RepositoryJson
from utils import clear_file


def testMovieRepository():
    repo = RepositoryJson("testMovieRepository.json")

    clear_file("testMovieRepository.json")
    repo.add(Movie("1", "Titanic", 1997, 10, "yes"))
    repo.add(Movie("2", "Dune", 2021, 13, "yes"))
    assert len(repo.read()) == 2
    assert repo.read("1").title == "Titanic"
    assert repo.read("1").releaseYear == 1997
    assert repo.read("1").ticketPrice == 10
    assert repo.read("1").inProgram == "yes"
    repo.update(Movie("1", "Dune", 2021, 19.99, "yes"))
    assert len(repo.read()) == 2
    assert repo.read("1").title == "Dune"
    assert repo.read("1").releaseYear == 2021
    assert repo.read("1").ticketPrice == 19.99
    assert repo.read("1").inProgram == "yes"
    repo.delete("1")
    assert len(repo.read()) == 1
    repo.delete("2")
    assert len(repo.read()) == 0


def testCardRepository():
    repo = RepositoryJson("testCardRepository.json")
    repo.add(ClientCard("1", "Ureche", "Grigore", "5670429873323", "29.04.1967", "14.12.2021", 30))
    assert len(repo.read()) == 1
    assert repo.read("1").name == "Ureche"
    assert repo.read("1").surname == "Grigore"
    assert repo.read("1").CNP == "5670429873323"
    assert repo.read("1").birthDate == "29.04.1967"
    assert repo.read("1").registrationDate == "14.12.2021"
    assert repo.read("1").points == 30
    repo.update(ClientCard("1", "Ban", "Betina", "6985678892531", "28.05.2002", "14.03.2021", 0))
    assert len(repo.read()) == 1
    assert repo.read("1").name == "Ban"
    assert repo.read("1").surname == "Betina"
    assert repo.read("1").CNP == "6985678892531"
    assert repo.read("1").birthDate == "28.05.2002"
    assert repo.read("1").registrationDate == "14.03.2021"
    assert repo.read("1").points == 0
    repo.delete("1")
    assert len(repo.read()) == 0


def testReservationRepository():
    repo = RepositoryJson("testReservationRepository.json")
    repo.add(Reservation("1", "2", "0", "17.11.2021", "13:00"))
    assert len(repo.read()) == 1
    assert repo.read("1").idEntity == "1"
    assert repo.read("1").idMovie == "2"
    assert repo.read("1").idClientCard == "0"
    assert repo.read("1").date == "17.11.2021"
    assert repo.read("1").hour == "13:00"
    repo.update(Reservation("1", "2", "0", "13.12.2021", "14:00"))
    assert len(repo.read()) == 1
    assert repo.read("1").idEntity == "1"
    assert repo.read("1").idMovie == "2"
    assert repo.read("1").idClientCard == "0"
    assert repo.read("1").date == "13.12.2021"
    assert repo.read("1").hour == "14:00"
    repo.delete("1")
    assert len(repo.read()) == 0


def testAllRepositories():
    testMovieRepository()
    testCardRepository()
    testReservationRepository()

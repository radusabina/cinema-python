from Domain.clientCardValidator import ClientCardValidator
from Domain.movieValidator import MovieValidator
from Repository.repositoryJson import RepositoryJson
from Service.clientCardService import ClientCardService
from Service.movieGenerator import MovieGenerator
from Service.movieService import MovieService
from Service.reservationService import ReservationService
from Service.undoRedoService import UndoRedoService
from Tests.testAll import testAll
from UserInterface.consola import Console
from utils import clear_file


def main():
    testAll()

    undoRedoService = UndoRedoService()

    movieRepository = RepositoryJson("movies.json")
    movieValidator = MovieValidator()
    movieService = MovieService(movieRepository, movieValidator, undoRedoService)

    cardRepository = RepositoryJson("cards.json")
    cardValidator = ClientCardValidator()
    cardService = ClientCardService(cardRepository, cardValidator, undoRedoService)

    reservationRepository = RepositoryJson("reservations.json")
    reservationService = ReservationService(reservationRepository, movieRepository, cardRepository, undoRedoService)

    movieGeneratorRepository = RepositoryJson("randomMovies.json")
    movieGeneratorValidator = MovieValidator()
    movieGeneratorService = MovieGenerator(movieGeneratorRepository, movieGeneratorValidator)
    clear_file("randomMovies.json")

    console = Console(movieService, cardService, reservationService, movieGeneratorService, undoRedoService)
    console.runMenu()


if __name__ == "__main__":
    main()

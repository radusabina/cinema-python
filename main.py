from Domain.clientCardValidator import CardClientValidator
from Domain.movieValidator import FilmValidator
from Repository.repositoryJson import RepositoryJson
from Service.cardClientService import CardClientService
from Service.filmGenerator import FilmGenerator
from Service.filmService import FilmService
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService
from Tests.testAll import testAll
from UserInterface.consola import Console
from utils import clear_file


def main():
    testAll()

    undoRedoService = UndoRedoService()

    filmRepository = RepositoryJson("filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, filmValidator, undoRedoService)

    cardRepository = RepositoryJson("carduri.json")
    cardValidator = CardClientValidator()
    cardService = CardClientService(cardRepository, cardValidator,
                                    undoRedoService)

    rezervareRepository = RepositoryJson("rezervari.json")
    rezervareService = RezervareService(rezervareRepository,
                                        filmRepository, cardRepository,
                                        undoRedoService)

    filmGeneratorRepository = RepositoryJson("filmeRandom.json")
    filmGeneratorValidator = FilmValidator()
    filmGeneratorService = FilmGenerator(filmGeneratorRepository,
                                         filmGeneratorValidator)
    clear_file("filmeRandom.json")

    consola = Console(filmService, cardService, rezervareService,
                      filmGeneratorService, undoRedoService)
    consola.runMenu()


if __name__ == "__main__":
    main()

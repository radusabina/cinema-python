from typing import List

from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.movie import Movie
from Domain.movieValidator import MovieValidator
from Domain.updateOperation import UpdateOperation
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class MovieService:

    def __init__(self, movieRepository: Repository, movieValidator: MovieValidator, undoRedoService: UndoRedoService):
        self.movieRepository = movieRepository
        self.movieValidator = movieValidator
        self.undoRedoService = undoRedoService

    def addMovie(self, idMovie: str, title: str, releaseYear: int,
                 ticketPrice: float, inProgram: str) -> None:
        movie = Movie(idMovie, title, releaseYear, ticketPrice, inProgram)
        self.movieValidator.validate(movie)
        self.movieRepository.add(movie)
        self.undoRedoService.addUndoOperation(AddOperation(self.movieRepository, movie))

    def updateMovie(self, idMovie: str, title: str, releaseYear: int,
                    ticketPrice: float, inProgram: str) -> None:
        oldMovie = self.movieRepository.read(idMovie)
        movie = Movie(idMovie, title, releaseYear, ticketPrice, inProgram)
        self.movieValidator.validate(movie)
        self.movieRepository.update(movie)
        self.undoRedoService.addUndoOperation(UpdateOperation(self.movieRepository, oldMovie, movie))

    def deleteMovie(self, idMovie: str) -> None:
        deletedMovie = self.movieRepository.read(idMovie)
        self.movieRepository.delete(idMovie)
        self.undoRedoService.addUndoOperation(DeleteOperation(self.movieRepository, deletedMovie))

    def getAll(self) -> List[Movie]:
        return self.movieRepository.read()

    def searchTextMovie(self, stringMovie: str) -> List:
        """
        returns a list with movies that contain the specified string
        """
        return list(filter(lambda x: x if stringMovie in x.getTextFomat() else None,
                           self.movieRepository.read()))

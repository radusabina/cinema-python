import string
from random import randint, choices, uniform, choice, sample
from typing import List

from Domain.movie import Movie
from Domain.movieValidator import MovieValidator
from Repository.repository import Repository


class MovieGenerator:
    def __init__(self, movieRepository: Repository, movieValidator: MovieValidator):
        self.movieRepository = movieRepository
        self.movieValidator = movieValidator

    def generateRandomMovies(self, n: int) -> None:
        """
        generates n random movies
        :param n: numarul de filme random de generat
        :return: None
        """
        list_in_program = ["yes", "no"]
        for i in range(0, n):
            idMovie = str(sample(range(0, 1000), 1))
            title = ''.join(choices(string.ascii_uppercase + string.digits, k=10))
            releaseYear = randint(1887, 2021)
            ticketPrice = uniform(10.5, 30.0)
            inProgram = choice(list_in_program)
            movie = Movie(idMovie, title, releaseYear, ticketPrice, inProgram)
            self.movieValidator.validate(movie)
            self.movieRepository.add(movie)

    def getAll(self) -> List[Movie]:
        return self.movieRepository.read()

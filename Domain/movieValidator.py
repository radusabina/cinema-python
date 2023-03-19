from Domain.movie import Movie
from Exceptions.movieError import MovieError


class MovieValidator:
    """
    the class that validates a movie
    """

    @staticmethod
    def validate(movie: Movie):
        if movie.inProgram not in ["yes", "no"]:
            raise MovieError("Field 'in program' can be filled with yes/no!")
        if movie.ticketPrice < 0:
            raise MovieError("Ticket price can not be negative!")

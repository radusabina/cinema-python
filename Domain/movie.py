from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Movie(Entity):
    """
    creates a movie
    - idEntity: movie id
    - title: movie title
    - releaseYear: the year the film was released
    - ticketPrice: the price of the ticket
    - inProgram: specifies if the movie is in the program or not
    """
    title: str
    releaseYear: int
    ticketPrice: float
    inProgram: str

    def getTextFomat(self):
        return f'{self.idEntity} {self.title} {self.releaseYear} ' \
               f'{self.ticketPrice} {self.inProgram}'

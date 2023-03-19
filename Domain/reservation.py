from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Reservation(Entity):
    """
    creates a reservation
    - idEntity: reservation id, must be unique
    - idMovie: movie's id
    - idClientCard: client card's id
    - dateAndhour: date and hour of the reservation
    """
    idMovie: str
    idClientCard: str
    date: str
    hour: str

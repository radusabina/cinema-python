from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class ClientCard(Entity):
    """
    creates a client card
    - idEntity: card id, must be unique
    - name: client's name
    - surname: client's surname
    - CNP: clinet's cnp, must be unique
    - birthDate: client's birth date
    - registrattionDate: card's registraton date
    - points: points on the card
    """
    name: str
    surname: str
    CNP: str
    birthDate: str
    registrationDate: str
    points: int

    def getTextFormat(self):
        return f'{self.idEntity}. {self.name} {self.surname} {self.CNP} ' \
               f'{self.birthDate} ' \
               f'{self.registrationDate} ' \
               f'{self.points}'

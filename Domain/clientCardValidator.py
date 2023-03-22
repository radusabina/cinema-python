from Domain.clientCard import ClientCard
from Exceptions.clientCardError import ClientCardError
from Exceptions.cnpError import CNPError


class ClientCardValidator:
    """
    the class that validates a client's card
    """

    @staticmethod
    def validate(card: ClientCard):
        if card.points < 0:
            raise ClientCardError("Points can not be negative!")
        if len(card.CNP) != 13:
            raise CNPError("CNP must have exactly 13 characters!")

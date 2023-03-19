from datetime import datetime
from typing import List

from Domain.multiUpdateOperation import MultiUpdateOperation
from Domain.addOperation import AddOperation
from Domain.clientCard import ClientCard
from Domain.clientCardValidator import ClientCardValidator
from Domain.deleteOperation import DeleteOperation
from Domain.entity import Entity
from Domain.updateOperation import UpdateOperation
from Exceptions.cnpError import CNPError

from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class ClientCardService:
    def __init__(self, cardRepository: Repository, cardValidator: ClientCardValidator,
                 undoRedoService: UndoRedoService):
        self.cardRepository = cardRepository
        self.cardValidator = cardValidator
        self.undoRedoService = undoRedoService

    def addCard(self, idCard: str, name: str, surname: str, CNP: str,
                birthDate: str, registrationDate: str, points: int) -> None:
        card = ClientCard(idCard, name, surname, CNP, birthDate,
                          registrationDate, points)
        self.cardValidator.validate(card)
        if self.readCNP(card.CNP, card.idEntity) is not None:
            raise CNPError("There is already a card with that CNP! CNP must be unique!")
        self.cardRepository.add(card)
        self.undoRedoService.addUndoOperation(AddOperation(self.cardRepository, card))

    def updateCard(self, idCard: str, name: str, surname: str, CNP: str,
                   birthDate: str, registrationDate: str, points: int) -> None:
        oldCard = self.cardRepository.read(idCard)
        card = ClientCard(idCard, name, surname, CNP,
                          birthDate, registrationDate, points)
        self.cardValidator.validate(card)
        if self.readCNP(card.CNP, card.idEntity) is not None:
            raise CNPError("There is already a card with that CNP! CNP must be unique!")
        self.cardRepository.update(card)
        self.undoRedoService.addUndoOperation(UpdateOperation(self.cardRepository, oldCard, card))

    def deleteCard(self, idCard: str) -> None:
        deletedCard = self.cardRepository.read(idCard)
        self.cardRepository.delete(idCard)
        self.undoRedoService.addUndoOperation(DeleteOperation(self.cardRepository, deletedCard))

    def getAll(self) -> List[ClientCard]:
        return self.cardRepository.read()

    def getById(self, idCard=None) -> [Entity]:
        return self.cardRepository.read(idCard)

    def orderedCardsByPointsReverse(self) -> List:
        """
        Sorts the cards list in reverse by the number of points
        """
        return sorted(self.cardRepository.read(), key=lambda card: card.points, reverse=True)

    def readCNP(self, cnp: str, idCard=None) -> [Entity]:
        """
        checks if the CNP is unique
        """
        cards = self.cardRepository.read()
        if idCard is None:
            for card in cards:
                if card.CNP == cnp:
                    return card
            return None
        else:
            for card in cards:
                if card.CNP == cnp and idCard != card.idEntity:
                    return card
            return None

    def searchTextCard(self, stringCard: str) -> List:
        """
        returns a list of cards in which the introduced string is found
        """
        return list(filter(lambda x: x if stringCard in x.getTextFormat() else None,
                           self.cardRepository.read()))

    def addPoints(self, data1: datetime, data2: datetime, value: int) -> List:
        """
        adds points to the cards that have the birthdate between two dates
        """
        oldCards = {}
        newCards = {}
        result = []
        if data1 > data2: data1, data2 = data2, data1
        cardsToUpdate = list(filter(lambda x: x if data1 <= datetime.strptime(x.dataNasterii, "%d.%m.%Y")
                                    <= data2 else None, self.cardRepository.read()))
        for card in cardsToUpdate:
            oldCard = self.cardRepository.read(card.idEntitate)
            oldCards[oldCard.idEntity] = oldCard

            card.points += value
            self.cardRepository.update(card)

            newCards[card.idEntity] = card
            result.append(card)

        self.undoRedoService.addUndoOperation(MultiUpdateOperation(
            self.cardRepository, oldCards, newCards))
        return result

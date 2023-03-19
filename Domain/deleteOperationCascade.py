from typing import List

from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class DeleteOperationCascade(UndoRedoOperation):

    def __init__(self, repository: Repository, rezervationRepository: Repository, cascadeList: List):
        self.repository = repository
        self.rezervationRepository = rezervationRepository
        self.cascadeList = cascadeList

    def doUndo(self):
        for i in range(len(self.cascadeList) - 1):
            self.rezervationRepository.add(self.cascadeList[i])
        self.repository.add(self.cascadeList[-1])

    def doRedo(self):
        for i in range(len(self.cascadeList) - 1):
            self.rezervationRepository.delete(self.cascadeList[i].idEntitate)
        self.repository.delete(self.cascadeList[-1].idEntitate)

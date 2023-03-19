from Domain.entity import Entity
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class MultiDeleteOperation(UndoRedoOperation):
    """
    undo and redo for multiple delete operations
    """

    def __init__(self, repository: Repository, deletedObjects: list[Entity]):
        self.repository = repository
        self.deletedObjects = deletedObjects

    def doUndo(self):
        for entity in self.deletedObjects:
            self.repository.add(entity)

    def doRedo(self):
        for entity in self.deletedObjects:
            self.repository.delete(entity.idEntity)

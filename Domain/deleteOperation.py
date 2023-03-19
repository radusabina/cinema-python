from Domain.entity import Entity
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class DeleteOperation(UndoRedoOperation):
    """
    undo and redo for delete operation
    """

    def __init__(self, repository: Repository, deletedObject: Entity):
        self.repository = repository
        self.deletedObject = deletedObject

    def doUndo(self):
        self.repository.add(self.deletedObject)

    def doRedo(self):
        self.repository.delete(self.deletedObject.idEntity)


from Domain.entity import Entity
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class UpdateOperation(UndoRedoOperation):
    """
    undo and redo for update operation
    """

    def __init__(self, repository: Repository, oldObject: Entity, newObject: Entity):
        self.repository = repository
        self.oldObject = oldObject
        self.newObject = newObject

    def doUndo(self):
        self.repository.update(self.oldObject)

    def doRedo(self):
        self.repository.update(self.newObject)

from Domain.entity import Entity
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class AddOperation(UndoRedoOperation):
    """
    undo and redo for add operation
    """

    def __init__(self, repository: Repository, addedObject:Entity):
        self.repository = repository
        self.addedObject = addedObject

    def doUndo(self):
        self.repository.delete(self.addedObject.idEntity)

    def doRedo(self):
        self.repository.add(self.addedObject)

from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class MultiUpdateOperation(UndoRedoOperation):
    """
    undo and redo for multiple update operations
    """

    def __init__(self, repository: Repository, oldObjects: dict, newObjects: dict):
        self.repository = repository
        self.oldObjects = oldObjects
        self.newObjects = newObjects

    def doUndo(self):
        for idEntity in self.newObjects:
            self.repository.update(self.oldObjects[idEntity])

    def doRedo(self):
        for idEntity in self.oldObjects:
            self.repository.update(self.newObjects[idEntity])

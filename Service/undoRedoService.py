from Domain.undoRedoOperation import UndoRedoOperation


class UndoRedoService:
    def __init__(self):
        self.undoOperations: list[UndoRedoOperation] = []
        self.redoOperations: list[UndoRedoOperation] = []

    def addUndoOperation(self, undoRedoOperation: UndoRedoOperation):
        self.undoOperations.append(undoRedoOperation)
        self.redoOperations.clear()

    def undo(self):
        if self.undoOperations:
            lastUndoOperation = self.undoOperations.pop()
            self.redoOperations.append(lastUndoOperation)
            lastUndoOperation.doUndo()

    def redo(self):
        if self.redoOperations:
            lastRedoOperation = self.redoOperations.pop()
            self.undoOperations.append(lastRedoOperation)
            lastRedoOperation.doRedo()

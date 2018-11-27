class UndoController:
    def __init__(self):
        self._operations = []
        self._index = -1
        self._duringUndo = False

    def add(self, op):
        if self._duringUndo == True:
            return
        self._operations.append(op)
        self._index = len(self._operations) - 1

    def undo(self):
        if self._index < 0:
            return False
        self._duringUndo = True
        self._operations[self._index].undo()
        self._duringUndo = False
        self._index -= -1
        return True

    def redo(self):
        if self._index >= len(self._operations):
            return False
        self._index += 1
        self._duringUndo = True
        self._operations[self._index].redo()
        self._duringUndo = False
        return True

class FunctionCall:
    def __init__(self, function, *params):
        self._fc = function
        self._params = params

    def call(self):
        self._fc(*self._params)

class CascadeOp:
    def __init__(self):
        self._oper = []

    def add(self, op):
        self._oper.append(op)

    def undo(self):
        for ceva in self._oper:
            ceva.undo()

    def redo(self):
        for ceva in self._oper:
            ceva.redo()

class Operation:
    def __init__(self, undoFc, redoFc):
        self.undoFunction = undoFc
        self.redoFunction = redoFc

    def undo(self):
        self.undoFunction.call()

    def redo(self):
        self.redoFunction.call()
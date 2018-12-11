from copy import deepcopy

def filter(list, param):
    listN = []
    for l in list:
        if param(l.ID):
            listN.append(l)
    return listN

def sortFunc(list, param):
    listN = deepcopy(list)
    g = len(listN) // 2
    while g > 0:
        i = g
        while i < len(listN):
            aux = listN[i]
            j = i
            while j >= g and param(listN[j - g], aux):
                listN[j] = listN[j - g]
                j -= g
            listN[j] = aux
            i += 1
        g = g // 2
    return listN

class Iterable:
    def __init__(self):
        self._index = 0
        self._data = list()

    def append(self, obj):
        self._data.append(obj)

    def __iter__(self):
        return self

    def __setItem__(self, p, v):
        self._data[p] = v

    def __delitem__(self, key):
        del self._data[key]

    def __next__(self):
        if self._index >= len(self._data):
            self._index = 0
            raise StopIteration
        index = self._index
        self._index += 1
        return self._data[index]

    def __len__(self):
        return len(self._data)
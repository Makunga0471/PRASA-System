import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)
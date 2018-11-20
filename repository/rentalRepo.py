from domain.stuff import *
from repository.repoException import *

class rentalRepository:

    def __init__(self):
        self.rentals = []

    def findMID(self, ID):
        for i in self.rentals:
            if i.mID == ID:
                return True
        return False

    def findCID(self, ID):
        for i in self.rentals:
            if i.cID == ID:
                return i
        return False

    def addRent(self, rental):
        self.rentals.append(rental)

    def newRentID(self):
        if len(self.rentals) != 0:
            return self.rentals[-1].rID + 1
        else:
            return 1

    def returnMovie(self, mID, now):
        for i in self.rentals:
            if i.mID == mID:
                if i.returnedD == 0:
                    i.setReturned(now)
                else:
                    raise RepositoryException("The movie was already returned!")
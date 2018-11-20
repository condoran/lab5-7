import datetime
from repository.moviesRepo import *
from domain.stuff import *
from operations.controlException import *

class Controller:
    def __init__(self, movies, clients, rentals):
        self.movieRepo = movies
        self.clientRepo = clients
        self.rentalRepo = rentals

    def testMovieID(self, ID):
        return self.movieRepo.findID(ID)

    def testClientID(self, ID):
        return self.clientRepo.findID(ID)

    def addMovie(self, ID, title, desc, genre):
        self.movieRepo.add(Movie(ID, title, desc, genre))

    def addClient(self, ID, name):
        self.clientRepo.add(Client(ID, name))

    def deleteMovie(self, movie):
        self.movieRepo.remove(movie)

    def deleteClient(self, client):
        self.clientRepo.remove(client)

    def updateMovie(self, movie, pos):
        del self.movieRepo[pos]
        self.addMovie(movie.ID, movie.title, movie.desc, movie.genre)

    def updateClient(self, client, pos):
        del self.clientRepo[pos]
        self.addClient(client.ID, client.name)

    def printM(self):
        return str(self.movieRepo)

    def printC(self):
        return str(self.clientRepo)

    def rentMovie(self, mID, cID, now):
        end = datetime.timedelta(days=14)
        if self.rentalRepo.findMID(mID) == True:
            raise ControllerException("The movie is already rented!")
        else:
            rentalClient = self.rentalRepo.findCID(cID)
            if rentalClient != False:
                if now < rentalClient.dueD and rentalClient.returnedD == 0:
                    raise ControllerException("The client has not returned a movie in the due date!")
                else:
                    self.rentalRepo.addRent(Rental(self.rentalRepo.newRentID, mID, cID, now, end, 0))
            else:
                self.rentalRepo.addRent(Rental(self.rentalRepo.newRentID, mID, cID, now, end, 0))

    def returnMovie(self, mID, now):
        if self.rentalRepo.findMID(mID) == False:
            raise ControllerException("The movie was not rented!")
        else:
            self.rentalRepo.returnMovie(mID, now)

from repository.moviesRepo import *
from repository.clientRepo import *

class Controler:
    def __init__(self, movies, clients, rentals):
        self.movieRepo = movies
        self.clients = clients
        self.rentals = rentals

    def testMovieID(self, ID):
        for i in range(0, len(self.movieRepo)):
            if self.movieRepo.movies[i].getID() == ID:
                return False
        return True

    def testClientID(self, ID):
        for i in range(0, len(self.clients)):
            if self.clients.clients[i].getID() == ID:
                return False
        return True

    def addMovie(self, ID, title, desc, genre):
        self.movieRepo.addM(Movie(ID, title, desc, genre))

    def addClient(self, ID, name):
        self.clients.addC(Client(ID, name))

    def printM(self):
        return self.movieRepo.getAll()
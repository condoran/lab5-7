from repository.moviesRepo import *
from repository.clientRepo import *
from domain.stuff import *

class Controler:
    def __init__(self, movies, clients, rentals):
        self.movieRepo = movies
        self.clientRepo = clients
        self.rentalRepo = rentals

    def testMovieID(self, ID):
        return self.movieRepo.findID(ID)

    def testClientID(self, ID):
        return self.clientRepo.findID(ID)

    def addMovie(self, ID, title, desc, genre):
        self.movieRepo.addM(Movie(ID, title, desc, genre))

    def addClient(self, ID, name):
        self.clientRepo.addC(Client(ID, name))

    def printM(self):
        return str(self.movieRepo)
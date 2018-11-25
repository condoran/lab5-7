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

    '''
    def testMovieExists(self, movie):
        return self.movieRepo.find(movie)
    '''

    '''
    def testClientExists(self, client):
        return self.clientRepo.findID(client)
    '''

    def addMovie(self, ID, title, desc, genre):
        self.movieRepo.add(Movie(ID, title, desc, genre))

    def addClient(self, ID, name):
        self.clientRepo.add(Client(ID, name))

    def deleteMovie(self, ID):
        movies = self.movieRepo.getAll()
        for i in range(0, len(movies)):
            if movies[i].ID == ID:
                del movies[i]
                break

    def deleteClient(self, ID):
        clients = self.clientRepo.getAll()
        for i in range(0, len(clients)):
            if clients[i].ID == ID:
                del clients[i]
                break

    def updateMovie(self, movie, ID):
        movies = self.movieRepo.getAll()
        for i in range(0, len(movies)):
            if movies[i].ID == ID:
                movies[i] = movie

    def updateClient(self, client, pos):
        clients = self.clientRepo.getAll()
        for i in range(0, len(clients)):
            if clients[i].ID == ID:
                clients[i] = client

    def printM(self):
        return str(self.movieRepo)

    def printC(self):
        return str(self.clientRepo)

    def rentMovie(self, mID, cID, now):
        end = datetime.datetime.strptime(now, '%Y-%m-%d') + datetime.timedelta(days=14)
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

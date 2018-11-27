import datetime
from copy import deepcopy
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
                movies[i].setID(movie.ID)
                movies[i].setTitle(movie.title)
                movies[i].setDesc(movie.desc)
                movies[i].setGenre(movie.genre)

    def updateClient(self, client, ID):
        clients = self.clientRepo.getAll()
        for i in range(0, len(clients)):
            if clients[i].ID == ID:
                clients[i].setID(client.ID)
                clients[i].setName(client.name)

    def printM(self):
        return str(self.movieRepo)

    def printC(self):
        return str(self.clientRepo)

    def rentMovie(self, mID, cID):
        end = datetime.datetime.now() + datetime.timedelta(days=14)
        now = datetime.datetime.now()
        if self.rentalRepo.findMID(mID) == True:
            raise ControllerException("The movie is already rented!")
        else:
            rentalClient = self.rentalRepo.findCID(cID)
            if rentalClient != False:
                if now > rentalClient.dueD and rentalClient.returnedD == 0:
                    raise ControllerException("The client has not returned a movie in the due date!")
                else:
                    self.rentalRepo.addRent(Rental(self.rentalRepo.newRentID, mID, cID, now, end, 0))
            else:
                self.rentalRepo.addRent(Rental(self.rentalRepo.newRentID, mID, cID, now, end, 0))

    def returnMovie(self, mID):
        now = datetime.datetime.now()
        if self.rentalRepo.findMID(mID) == False:
            raise ControllerException("The movie was not rented!")
        else:
            self.rentalRepo.returnMovie(mID, now)

    def findInMoviesID(self, ID):
        try:
            ID = int(ID)
        except ValueError:
            raise ValueError("Incorect ID!")
        movies = self.movieRepo.getAll()
        moviesN = []
        for i in movies:
            if str(i.ID).find(str(ID)) != -1:
               moviesN.append(i)
        return moviesN

    def findInMoviesTitle(self, title):
        movies = deepcopy(self.movieRepo.getAll())
        title = title.lower()
        moviesN = []
        for i in movies:
            titl = i.title.lower()
            if titl.find(title) != -1:
                moviesN.append(i)
        return moviesN

    def findInMoviesDesc(self, desc):
        movies = deepcopy(self.movieRepo.getAll())
        desc = desc.lower()
        moviesN = []
        for i in movies:
            de = i.desc.lower()
            if de.find(desc) != -1:
                moviesN.append(i)
        return moviesN

    def findInMoviesGenre(self, genre):
        movies = deepcopy(self.movieRepo.getAll())
        genre = genre.lower()
        moviesN = []
        for i in movies:
            ge = i.genre.lower()
            if ge.find(genre) != -1:
                moviesN.append(i)
        return moviesN

    def findInClientsID(self, ID):
        try:
            ID = int(ID)
        except ValueError:
            raise ValueError("Incorect ID!")
        clients = self.clientRepo.getAll()
        clientsN = []
        for i in clients:
            if str(i.ID).find(str(ID)) != -1:
               clientsN.append(i)
        return clientsN

    def findInClientsName(self, name):
        clients = deepcopy(self.movieRepo.getAll())
        name = name.lower()
        clientsN = []
        for i in clients:
            na = i.name.lower()
            if na.find(name) != -1:
                clientsN.append(i)
        return clientsN

    def allRentals(self):
        movies = self.movieRepo.getAll()
        moviesN = []
        for i in movies:
            if self.rentalRepo.findMID(i.ID) == True:
                moviesN.append(i)
        return moviesN

    def lateRentals(self):
        movies = self.allRentals()
        moviesN = []
        for i in movies:
            a = self.rentalRepo.returnByMovie(i.ID)
            if a.dueD < datetime.datetime.now():
                moviesN.append(i)
        return moviesN

    def mostRentedMovie(self):
        kM = []
        movies = self.movieRepo.getAll()
        rentals = self.rentalRepo.getAll()
        for i in movies:
            d = 0
            k = 0
            for j in rentals:
                if i.ID == j.mID:
                    k += 1
                    if j.returnedD == 0:
                        now = datetime.datetime.now()
                        ceva = now - j.rentedD
                        d += ceva.days
                    else:
                        ceva = j.returnedD - j.rentedD
                        d += ceva.days
            if k != 0:
                kM.append([k, d, i])
        kM.sort(key=lambda x: x[1])
        kM.sort(key=lambda x: x[0])
        return kM


    def mostActiveClient(self):
        kM = []
        clients = self.clientRepo.getAll()
        rentals = self.rentalRepo.getAll()
        for i in clients:
            k = 0
            d = 0
            for j in rentals:
                if i.ID == j.cID:
                    k += 1
                    if j.returnedD == 0:
                        now = datetime.datetime.now()
                        ceva = now - j.rentedD
                        d += ceva.days
                    else:
                        ceva = j.returnedD - j.rentedD
                        d += ceva.days
            if k != 0:
                kM.append([d, i])
        kM.sort(key=lambda x: x[0])
        return kM
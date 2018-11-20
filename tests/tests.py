import unittest
import datetime
from repository.moviesRepo import *
from repository.rentalRepo import *
from operations.controller import *

class Test(unittest.TestCase):
    def setUp(self):
        self.controller = Controller(moviesRepository(), moviesRepository(), rentalRepository())

    def tearDown(self):
        del self.controller

    def testAddMovie(self):
        self.controller.addMovie(Movie(12, "Die hard", "Lot of shooting", "Action"))
        assert self.controller.movieRepo.movies[0] == Movie(12, "Die hard", "Lot of shooting", "Action")

    def testAddClient(self):
        self.controller.addClient(Client(12, "Crizatema Florin"))
        assert self.controller.clientRepo.movies[0] == Client(12, "Crizatema Florin")

    def testDeteleMovie(self):
        self.controller.addMovie(Movie(12, "Die hard", "Lot of shooting", "Action"))
        self.controller.deleteMovie(Movie(12, "Die hard", "Lot of shooting", "Action"))
        assert self.controller.movieRepo.movies == []

    def testDeteleClient(self):
        self.controller.addClient(Client(12, "Crizatema Florin"))
        self.controller.deleteClient(Client(12, "Crizatema Florin"))
        assert self.controller.clientRepo.movies == []

    def testUpdateMovie(self):
        self.controller.addMovie(Movie(12, "Die hard", "Lot of shooting", "Action"))
        self.controller.updateMovie(Movie(1, "This", "That", "Other"), 0)
        assert self.controller.movieRepo.movies[0] == Movie(1, "This", "That", "Other")

    def testUpdateClient(self):
        self.controller.addClient(Client(12, "Crizatema Florin"))
        self.controller.updateClient(Client(1, "Georgel Ala"))
        assert self.controller.clientRepo.movies[0] == Client(1, "Georgel Ala")

    def testRentMovie(self):
        self.controller.addMovie(Movie(12, "Die hard", "Lot of shooting", "Action"))
        self.controller.addClient(Client(12, "Crizatema Florin"))
        now = datetime.datetime.today().strftime('%Y-%m-%d')
        end = datetime.timedelta(days=14)
        self.controller.rentMovie(12, 12, now)
        assert self.controller.rentalRepo.rentals[0] == Rental(1, 12, 12, now, end, 0)

    def testReturnMovie(self):
        self.controller.addMovie(Movie(12, "Die hard", "Lot of shooting", "Action"))
        self.controller.addClient(Client(12, "Crizatema Florin"))
        now = datetime.datetime.today().strftime('%Y-%m-%d')
        end = datetime.timedelta(days=14)
        self.controller.rentMovie(12, 12, now)
        self.controller.returnMovie(12, now)
        assert self.controller.rentalRepo.rentals[0] == Rental(1, 12, 12, now, end, now)
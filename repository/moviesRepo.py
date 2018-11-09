from domain.stuff import Movie

class moviesRepository:

    def __init__(self):
        self.movies = []

    def addM(self, movie):
        self.movies.append(movie)

    def findID(self, ID):
        for i in range(0, len(self.movies)):
            if self.movies[i].getID() == ID:
                return False
        return True

    def find(self, movie):
        for i in range(0, len(self.movies)):
            if self.movies[i] == movie:
                return i
        return -1

    def remove(self, movie):
        if self.find(movie) != -1:
            del self.movies[self.find(movie)]
        else:
            raise RepositoryException("We do not have the movie at the shop!")

    def update(self, movie, movieN):
        self.movies[self.find(movie)] = movieN

    def getAll(self):
        return self.movies

class RepositoryException:

    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return  self.__message
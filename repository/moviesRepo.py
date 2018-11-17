class moviesRepository:

    def __init__(self):
        self.movies = []

    def addM(self, movie):
        self.movies.append(movie)

    def findID(self, ID):
        for i in self.movies:
            if self.movies[i].ID == ID:
                return True
        return False

    def find(self, movie):
        for i in self.movies:
            if self.movies[i] == movie:
                return i
        return False

    def remove(self, movie):
        if self.find(movie) != -1:
            del self.movies[self.find(movie)]
        else:
            raise RepositoryException("We do not have the movie at the shop!")

    def update(self, movie, movieN):
        if self.find(movie) != -1:
            self.remove(movie)
            self.addM(movieN)
        else:
            raise RepositoryException("We do not have the movie at the shop!")

    def getAll(self):
        return self.movies

    def __len__(self):
        return len(self.movies)

    def __str__(self):
        final = ""
        for r in self.movies:
            final += str(r)
            final += "/n"
        return final

class RepositoryException(Exception):

    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return  self.__message
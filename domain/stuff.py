class Movie:
    def __init__(self, movieID, title, desc, genre):
        self.movieID = movieID
        self.movieTitle = title
        self.movieDesc = desc
        self.movieGenre = genre

    @property
    def ID(self):
        return self.movieID

    @property
    def title(self):
        return self.movieTitle

    @property
    def desc(self):
        return self.movieDesc

    @property
    def genre(self):
        return self.genre

    def print(self):
        print(self.movieID, self.title, self.desc, self.genre)

class Client:
    def __init__(self, clientID, name):
        self.clientID = clientID
        self.name = name

    @property
    def ID(self):
        return self.clientID

    @property
    def name(self):
        return self.name

    def print(self):
        print(self.clientID, self.name)
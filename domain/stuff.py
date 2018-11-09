class Movie:
    def __init__(self, movieID, title, desc, genre):
        self.movieID = movieID
        self.title = title
        self.desc = desc
        self.genre = genre

    def getID(self):
        return self.movieID

    def getTitle(self):
        return self.title

    def getDesc(self):
        return self.title

    def getGenre(self):
        return self.genre

    def setID(self, v):
        self.movieID = v

    def setTitle(self, v):
        self.title = v

    def setDesc(self, v):
        self.desc = v

    def setGenre(self, v):
        self.desc = v

    def print(self):
        print(self.movieID, self.title, self.desc, self.genre)

class Client:
    def __init__(self, clientID, name):
        self.clientID = clientID
        self.name = name

    def getID(self):
        return self.clientID

    def getName(self):
        return self.name

    def setID(self, v):
        self.clientID = v

    def setName(self, v):
        self.name = v

    def print(self):
        print(self.clientID, self.name)
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
        return self.movieGenre

    def setID(self, ID):
        self.movieID = ID

    def setTitle(self, title):
        self.movieTitle = title

    def setDesc(self, desc):
        self.movieDesc = desc

    def setGenre(self, genre):
        self.movieGenre = genre

    def __str__(self):
        return str(self.movieID) + ". " + self.title + "; " + self.desc + "; " + self.genre + '\n'

class Client:
    def __init__(self, clientID, name):
        self.clientID = clientID
        self.clientName = name

    @property
    def ID(self):
        return self.clientID

    @property
    def name(self):
        return self.clientName

    def setID(self, ID):
        self.clientID = ID

    def setName(self, name):
        self.clientName = name

    def __str__(self):
        return str(self.clientID) + ". " + self.clientName + '\n'

class Rental:
    def __init__(self, rentalID, movieID, clientID, rentedDate, dueDate, returnedDate):
        self.rentalID = rentalID
        self.movieID = movieID
        self.clientID = clientID
        self.rentedDate = rentedDate
        self.dueDate = dueDate
        self.returnedDate = returnedDate

    @property
    def rID(self):
        return self.rentalID

    @property
    def mID(self):
        return self.movieID

    @property
    def cID(self):
        return self.clientID

    @property
    def rentedD(self):
        return self.rentedDate

    @property
    def dueD(self):
        return self.dueDate

    @property
    def returnedD(self):
        return self.returnedDate

    def setReturned(self, date):
        self.returnedDate = date

    def __str__(self):
        return str(self.rentalID) + ". " + str(self.movieID) + "; " + str(self.clientID)+ "; " + str(self.rentedDate) + "; " + str(self.dueDate) + "; " + str(self.returnedD) + '\n'
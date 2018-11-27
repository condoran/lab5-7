import datetime
from operations.controller import *

class UI:
    def __init__(self, controller):
        self._controller = controller

    def printMenu(self):
        print("1.Add")
        print("2.Remove")
        print("3.Update")
        print("4.List")
        print("5.Rent a movie")
        print("6.Return a movie")
        print("7.Search for an element")
        print("8.Statistics")
        print("9.Exit")

    def menu(self):
        while True:
            self.printMenu()
            userInput = input("Enter a command: ")

            if userInput == "1":
                print("1.Movie")
                print("2.Client")
                a = input("What do you want to add? ")
                if a == "1":
                    ID = input("Enter the ID: ")
                    title = input("Enter the title: ")
                    desc = input("Enter the description: ")
                    genre = input("Enter the genre: ")
                    try:
                        ID = int(ID)
                    except ValueError:
                        print("Invalid ID!")
                    if not self._controller.testMovieID(ID):
                        self._controller.addMovie(ID, title, desc, genre)
                    else:
                        print("The ID is already in use")
                elif a == "2":
                    ID = input("Enter the ID: ")
                    name = input("Enter the name: ")
                    try:
                        ID = int(ID)
                    except ValueError:
                        print("Invalid ID!")
                    if not self._controller.testClientID(ID):
                        self._controller.addClient(ID, name)
                    else:
                        print("The ID is already in use")
                else:
                    print("Incorect input!")
            elif userInput == "2":
                print("1.Movie")
                print("2.Client")
                a = input("What do you want to remove? ")
                if a == "1":
                    print(self._controller.printM())
                    ID = input("Enter the ID: ")
                    try:
                        ID = int(ID)
                    except ValueError:
                        print("Invalid ID!")
                    if self._controller.testMovieID(ID):
                        self._controller.deleteMovie(ID)
                    else:
                        print("There is no movie with this ID!")
                elif a == "2":
                    print(self._controller.printC())
                    ID = input("Enter the ID: ")
                    try:
                        ID = int(ID)
                    except ValueError:
                        print("Invalid ID!")
                    if self._controller.testClientID(ID):
                        self._controller.deleteClient(Client(ID, name))
                    else:
                        print("There is no client with this ID!")
                else:
                    print("Invalid input!")
            elif userInput == "3":
                print("1.Movie")
                print("2.Client")
                a = input("What do you want to update? ")
                if a == "1":
                    print(self._controller.printM())
                    ID = input("Enter the ID: ")
                    try:
                        ID = int(ID)
                    except ValueError:
                        print("Invalid ID!")
                    if not self._controller.testMovieID(ID):
                        print("There is no movie with this ID!")
                    else:
                        IDN = input("Enter the new ID: ")
                        titleN = input("Enter the new title: ")
                        descN = input("Enter the new description: ")
                        genreN = input("Enter the new genre: ")
                        if not self._controller.testMovieID(IDN):
                            self._controller.updateMovie(Movie(IDN, titleN, descN, genreN), ID)
                        else:
                            print("The ID is already in use")
                elif a == "2":
                    print(self._controller.printC())
                    ID = input("Enter the ID: ")
                    try:
                        ID = int(ID)
                    except ValueError:
                        print("Invalid ID!")
                    if not self._controller.testClientID(ID):
                        print("There is no such client!")
                    else:
                        IDN = input("Enter the new ID: ")
                        nameN = input("Enter the new name: ")
                        if not self._controller.testClientID(IDN):
                            self._controller.updateClient(Client(IDN, nameN), ID)
                        else:
                            print("The ID is already in use!")
                else:
                    print("Invalid input!")
            elif userInput == "4":
                print("1.Movie")
                print("2.Client")
                a = input("What do you want to list? ")
                if a == "1":
                    print(self._controller.printM())
                elif a == "2":
                    print(self._controller.printC())
                else:
                    print("Invalid input")
            elif userInput == "5":
                print(self._controller.printM())
                mID = input("Type the ID of the movie you want to rent: ")
                print(self._controller.printC())
                cID = input("Type the ID of the client that is renting the movie: ")
                try:
                    cID = int(cID)
                    mID = int(mID)
                except ValueError:
                    print("Invalid ID!")
                if not self._controller.testClientID(cID):
                    print("There is no such client!")
                elif  not self._controller.testMovieID(mID):
                    print("There is no such movie!")
                else:
                    try:
                        self._controller.rentMovie(mID, cID)
                    except ControllerException or RepositoryException as ce:
                        print(ce)
            elif userInput == "6":
                print(self._controller.printM())
                mID = input("Type the ID of the movie you want to return: ")
                try:
                    mID = int(mID)
                except ValueError:
                    print("Invalid ID!")
                if not self._controller.testMovieID(mID):
                    print("There is no such movie!")
                else:
                    try:
                        self._controller.returnMovie(mID)
                    except ControllerException as ce:
                        print(ce)
            elif userInput == "7":
                print("1.Movie")
                print("2.Client")
                a = input("What do you want to search for? ")
                if a == "1":
                    print("1.ID")
                    print("2.Title")
                    print("3.Description")
                    print("4.Genre")
                    kms = input("What do you want to search by? ")
                    if kms == "1":
                        ID = input("Enter the ID: ")
                        try:
                            moviesN = self._controller.findInMoviesID(ID)
                        except ValueError as ve:
                            print(ve)
                        r = ""
                        for i in moviesN:
                            r += str(i)
                        print(r)
                    elif kms == "2":
                        title = input("Enter the title: ")
                        moviesN = self._controller.findInMoviesTitle(title)
                        r = ""
                        for i in moviesN:
                            r += str(i)
                        print(r)
                    elif kms == "3":
                        desc = input("Enter the descritpion: ")
                        moviesN = self._controller.findInMoviesDesc(desc)
                        r = ""
                        for i in moviesN:
                            r += str(i)
                        print(r)
                    elif kms == "4":
                        genre = input("Enter the genre: ")
                        moviesN = self._controller.findInMoviesGenre(genre)
                        r = ""
                        for i in moviesN:
                            r += str(i)
                        print(r)
                    else:
                        print("Invalid input!")
                elif a == "2":
                    print("1.ID")
                    print("2.Name")
                    kms = input("What do you want to search by? ")
                    if kms == "1":
                        ID = input("Enter the ID: ")
                        try:
                            clientsN = self._controller.findInClientsID(ID)
                        except ValueError as ve:
                            print(ve)
                        r = ""
                        for i in clientsN:
                            r += str(i)
                        print(r)
                    elif kms == "2":
                        name = input("Enter the genre: ")
                        clientsN = self._controller.findInClientsName(name)
                        r = ""
                        for i in clientsN:
                            r += str(i)
                        print(r)
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
            elif userInput == "8":
                print("1.Most rented movies")
                print("2.Most active clients")
                print("3.All rentals")
                print("4.Late rentals")
                a = input("What statistics do you want? ")
                if a == "1":
                    moviesN = self._controller.mostRentedMovie()
                    for i in moviesN:
                        print(str(i[2]))
                elif a == "2":
                    clientsN = self._controller.mostActiveClient()
                    for i in clientsN:
                        print(str(i[1]))
                elif a == "3":
                    moviesN = self._controller.allRentals()
                    r = ""
                    for i in moviesN:
                        r += str(i)
                    print(r)
                elif a == "4":
                    moviesN = self._controller.lateRentals()
                    r = ""
                    for i in moviesN:
                        r += str(i)
                    print(r)
            elif userInput == "9":
                return False
            else:
                print("Invalid input")
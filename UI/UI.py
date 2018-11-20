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
        print("7.Exit")

    def menu(self):
        now = datetime.datetime.today().strftime('%Y-%m-%d')

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
                    if not self._controller.testMovieID(ID):
                        self._controller.addMovie(ID, title, desc, genre)
                    else:
                        print("The ID is already in use")
                elif a == "2":
                    ID = input("Enter the ID: ")
                    name = input("Enter the name: ")
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
                    title = input("Enter the title: ")
                    desc = input("Enter the description: ")
                    genre = input("Enter the genre: ")
                    try:
                        ID = int(ID)
                    except ValueError:
                        print("Invalid ID!")
                    self._controller.deleteMovie(Movie(ID, title, desc, genre))
                elif a == "2":
                    print(self._controller.printC())
                    ID = input("Enter the ID: ")
                    name = input("Enter the name: ")
                    self._controller.deleteClient(Client(ID, name))
                else:
                    print("Invalid input!")
            elif userInput == "3":
                print("1.Movie")
                print("2.Client")
                a = input("What do you want to update? ")
                if a == "1":
                    ID = input("Enter the ID: ")
                    title = input("Enter the title: ")
                    desc = input("Enter the description: ")
                    genre = input("Enter the genre: ")
                    pos = self._controller.testMovieExists(ID, title, desc, genre)
                    if pos == False:
                        print("There is no such movie!")
                    else:
                        IDN = input("Enter the new ID: ")
                        titleN = input("Enter the new title: ")
                        descN = input("Enter the new description: ")
                        genreN = input("Enter the new genre: ")
                        if self._controller.testMovieID(IDN):
                            self._controller.updateMovie(Movie(IDN, titleN, descN, genreN), pos)
                        else:
                            print("The ID is already in use")
                elif a == "2":
                    ID = input("Enter the ID: ")
                    name = input("Enter the name: ")
                    pos = self._controller.testClientExists(ID, name)
                    if pos == False:
                        print("There is no such movie!")
                    else:
                        IDN = input("Enter the new ID: ")
                        nameN = input("Enter the new name: ")
                        if self._controller.testMovieID(IDN):
                            self._controller.updateClient(Client(IDN, nameN), pos)
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
                self._controller.rentMovie(mID, cID, now)
            elif userInput == "6":
                print(self._controller.printM())
                mID = input("Type the ID of the movie you want to return: ")
                self._controller.returnMovie(mID, now)
            elif userInput == "7":
                return False
            else:
                print("Invalid input")
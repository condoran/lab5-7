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
                    if self._controller.testMovieID(ID):
                        self._controller.addMovie(ID, title, desc, genre)
                    else:
                        print("The ID is already in use")
                elif a == "2":
                    ID = input("Enter the ID: ")
                    name = input("Enter the name: ")
                    if self._controller.testClientID(ID):
                        self._controller.addClient(ID, name)
                else:
                    print("Incorect input!")
            elif userInput == "7":
                return False
            else:
                print("Invalid input")
            '''
            elif userInput == "2":
                print("1.Movie")
                print("2.Client")
                a = input("What do you want to remove? ")
                if a == "1":
                    ID = input("Enter the ID: ")
                    title = input("Enter the title: ")
                    desc = input("Enter the description: ")
                    genre = input("Enter the genre: ")
                    pos = self._controller.testMovieExists(ID, title, desc, genre)
                    if pos == False:
                        print("There is no such movie!")
                    else:
                        self._controller.deleteMovie(pos)
                elif a == "2":
                    ID = input("Enter the ID: ")
                    name = input("Enter the name: ")
                    pos = self._controller.testClientExists(ID, name)
                    if pos == False:
                        print("There is no such client!")
                    else:
                        self._controller.deleteClient(pos)
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
                            self._controller.updateMovie(pos, IDN, titleN, descN, genreN)
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
                            self._controller.updateClient(pos, IDN, nameN)
                        else:
                            print("The ID is already in use!")#
            elif userInput == "4":
                    print(self._controller.printM.printM())
            '''

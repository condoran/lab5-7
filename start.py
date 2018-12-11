from operations.controller import *
from domain.stuff import *
from repository.moviesRepo import *
from repository.rentalRepo import *
from operations.undoController import *
import random
from UI.UI import *
from tests.tests import *
'''
movies1 = ["juvenile", "stupid", "hilarious", "enjoyable", "dreadful", "powerful", "thought-provoking", "boring", "second-rate", "imaginative", "powerful", "hilarious", "enjoyable", "imaginative", "though-provoking", "boring", "second-rate", "juvenile", "stupid", "dreadful"]
movies2 = ["first", "old", "new", "good", "goo", "silent", "bad", "favorite", "western", "american", "last", "entire", "whole", "popular", "next", "late", "latest", "best", "successful", "original", "final", "classic", "recent", "scary", "current", "rated", "big", "test", "hour", "funny", "minute", "length", "occasional", "finished", "pornographic", "animated", "budget", "famous", "romantic", "wonderful", "fiction", "porn", "sound", "dirty", "japanese", "night", "violent", "sad", "stupid", "typical", "flight", "cheap", "winning", "italian", "blue", "documentary", "digital", "time", "exciting", "interesting", "excellent", "worst", "non", "hindi", "expensive", "interactive"]
genres = ["action", "adventure", "comedy", "crime", "drama", "historical", "horror", "musical", "science fiction", "war", "western"]
names = ["Gregory", "Joan", "Kanesha", "Lashon", "Beatris", "Dani", "Maryetta", "Candyce", "Stanford", "Anitra", "Nancey", "Angelika", "Marvin", "Chet", "Ora", "Sherley", "Hermila", "Mimi", "Ivana", "Luke"]
repo = moviesRepository()
repoC = moviesRepository()
repoR = rentalRepository()
now = datetime.datetime.today().strftime('%d-%m-%Y')
end = datetime.datetime.strptime(now, '%d-%m-%Y') - datetime.timedelta(days=14)
end1 = datetime.datetime.strptime(now, '%d-%m-%Y') - datetime.timedelta(days=1)
for i in range(0, 100):
    mT = str(random.choice(movies1) + " " + random.choice(movies2))
    mD = str(random.choice(movies2) + " "  + random.choice(movies2))
    mG = str(random.choice(genres))
    name = str(random.choice(names))
    repo.add(Movie(i + 1, mT, mD, mG))
    repoC.add(Client(i + 1, name))
    repoR.addRent(Rental(i + 1, i, i, end, end1, 0))
'''
repo = moviesRepository()
repoC = moviesRepository()
repoR = rentalRepository()
undo = UndoController()
controller = Controller(repo, repoC, repoR, undo)
controller.firstRead()
ui = UI(controller)
ui.menu()
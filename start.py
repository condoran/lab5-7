from operations.controller import *
from domain.stuff import *
from repository.moviesRepo import *
from repository.rentalRepo import *
from UI.UI import *

repo = moviesRepository()
repoC = moviesRepository()
repoR = rentalRepository()
repo.add(Movie(12, "Die hard", "Lot of shooting", "Action"))
repo.add(Movie(21, "Transhuman", "About a transhuman", "Adventure"))
repo.add(Movie(11, "yes", "yes", "yes"))
repoC.add(Client(11, "Barbu"))
controller = Controller(repo, repoC, repoR)
ui = UI(controller)
ui.menu()
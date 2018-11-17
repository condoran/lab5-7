from operations.controller import *
from domain.stuff import *
from repository.moviesRepo import *

repo = moviesRepository()
repo.addM(Movie(12, "Die hard", "Lot of shooting", "Action"))
repo.addM(Movie(11, "Transhuman", "About a tanshuman", "Adventure"))
repo.addM(Movie(11, "yes", "yes", "yes"))
controller = Controler(repo, repo, repo)
print(controller.printM())
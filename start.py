from operations.controller import *
from domain.stuff import *
from repository.moviesRepo import *
from repository.rentalRepo import *
from UI.UI import *
from tests.tests import *

repo = moviesRepository()
repoC = moviesRepository()
repoR = rentalRepository()
repo.add(Movie(12, "Die hard", "Lot of shooting", "Action"))
repo.add(Movie(21, "Transhuman", "About a transhuman", "Adventure"))
repo.add(Movie(11, "yes", "yes", "yes"))
repo.add(Movie(1, "Mars", "2 explorers adventure on mars", "Adventure"))
repo.add(Movie(2, "Saw", "Psycho killer out for blood", "Thriller"))
repoC.add(Client(11, "Barbu"))
repoC.add(Client(12, "Stark"))
repoC.add(Client(13, "Tony"))
repoC.add(Client(14, "Myself"))
now = datetime.datetime.today().strftime('%d-%m-%Y')
end = datetime.datetime.strptime(now, '%d-%m-%Y') - datetime.timedelta(days=14)
end1 = datetime.datetime.strptime(now, '%d-%m-%Y') - datetime.timedelta(days=1)
repoR.addRent(Rental(1, 21, 11, end, end1, 0))
controller = Controller(repo, repoC, repoR)
ui = UI(controller)
ui.menu()
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
repoC.add(Client(11, "Barbu"))
now = datetime.datetime.today().strftime('%d-%m-%Y')
end = datetime.datetime.strptime(now, '%d-%m-%Y') - datetime.timedelta(days=14)
end1 = datetime.datetime.strptime(now, '%d-%m-%Y') - datetime.timedelta(days=1)
repoR.addRent(Rental(1, 21, 11, end, end1, 0))
controller = Controller(repo, repoC, repoR)
ui = UI(controller)
ui.menu()
from domain.stuff import Client

class clientsRepository:

    def __init__(self):
        self.clients = []

    def addC(self, client):
        self.clients.append(client)
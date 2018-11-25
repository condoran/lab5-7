class ControllerException(Exception):

    def __init__(self, message):
        self.__message = message

    @property
    def __str__(self):
        return self.__message
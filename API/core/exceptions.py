from logging import error, basicConfig, ERROR
from os import getenv

class OwnException(Exception):
    def __init__(self, error_code, msg):
        self.__error_code = error_code
        self.__msg = msg
        self.__log_path = getenv("LOG")
        basicConfig(filename=f"{self.__log_path}/error.log", filemode="w", level=ERROR)
        pass

    @property
    def msg(self):
        return self.__msg

    @property
    def error_code(self):
        return self.__error_code

    def __call__(self):
        error(f"{self.__error_code} : {self.__msg}")
        pass
    pass

#Write your personal exception here
class ServiceAlreadyExist(OwnException):
    pass

class ServiceDoesntExist(OwnException):
    pass

from .services import Service
from .exceptions import ServiceAlreadyExist, ServiceDoesntExist

class ServiceProviders:
    __instance = None

    def __init__(self):
        self.__services = dict()
        pass

    def add_service(self, name: str, service) -> None:
        for i, j in self.__services.items():
            if i == name:
                raise ServiceAlreadyExist(1, f"{name} already exist")
        pass

    def provide_service(self, name: str) -> Service:
        service_key = self.__services.keys()
        if name not in service_key:
            raise ServiceDoesntExist(1, f"{name} doesn't exist")
        return self.__services[name]
        
    @staticmethod
    def get_instance():
        if ServiceProviders.__instance is None:
            ServiceProviders.__instance = ServiceProviders()
        return ServiceProviders.__instance
    pass


    

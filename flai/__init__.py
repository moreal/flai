from socket import socket
from enum import Enum
from typing import Callable, Type

class Flai:
    def __init__(self):
        self.routes = dict()

    def event(self, case: Type[Enum]) -> Callable:
        if case in self.routes:
            raise Exception("Duplicate option")
        
        def decorator(func):
            self.routes[case] = func
            return func
        
        return decorator

    def run(self, host: str, port: int):
        self.sock = socket()
        self.sock.bind((host, port))
        self.sock.listen(100)
        while True:
            accepted, address = self.sock.accept()
            print(accepted, address)
    
    def close(self):
        self.sock.close()

flai = Flai()
flai.run("0.0.0.0", 9000)
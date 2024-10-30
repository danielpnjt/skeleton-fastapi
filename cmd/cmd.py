from internal import server
from infrastructure import container

def Run() :
    server.StartService(container.New())

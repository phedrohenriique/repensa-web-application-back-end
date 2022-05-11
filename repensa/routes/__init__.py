import sanic as sn
from .server import server

## if used the statement $ import server will reference the server.py file while
## $ from .server import server will import the variable inside the server.py file

## file where to put all route Blueprint objects, for organization each route will have its
## own handler to be dealt and url

routes = sn.Blueprint.group(
    server, 
    url_prefix='/'
    )
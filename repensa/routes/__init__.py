import sanic as sn
from .server import server

routes = sn.Blueprint.group(
    server, 
    url_prefix='/'
    )
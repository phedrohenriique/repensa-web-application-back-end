import os
import sanic as sn
import configuration as config

server = sn.Blueprint('server',url_prefix='/server')

@server.get('/')
async def server_start(request):
    print('server startd')
    return sn.json({ "message": "server started"})

@server.get('/env')
async def server_variables(request):
    print(config.PORT)
    return sn.json(config.PORT)
import sanic as sn

server = sn.Blueprint('server',url_prefix='/server')

@server.get('/')
async def server_start(request):
    print('server startd')
    return sn.json({ "message": "server started"})
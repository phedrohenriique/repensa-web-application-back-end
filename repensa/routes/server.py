import sanic as sn
import configuration as config
from connection import create_pool

server = sn.Blueprint('server',url_prefix='/server')

@server.get('/')
async def server_start(request):
    print('server startd')
    return sn.json({ "message": "server started"})

@server.get('/env')
async def server_variables(request):
    print(config.PORT)
    return sn.json({"message":f"PORT : {config.PORT}"})

@server.get('/data')
async def server_data(request):
    query = """
    select name, email from users where name = 'pedro'
    """
    pool = await  create_pool()
    connection = await  pool.acquire()

    ## setting the .acquire() method allows for connecting and use db
    ## connection.transaction() necessar for more than one queries

    results = await connection.fetch(query)

    ## print(results, *results) the fetch result returns a list, with a record type variable
    ## in order to use and parse easily the parameters the result must have its arguments
    ## all used out of list, thats why use *results wich is the same as result[0]
    ## specificall for one list returned value query, if there were more results,
    ## another list should be done in an array

    response = dict(*results)

    connection.close()
    return  sn.json(response, 200)
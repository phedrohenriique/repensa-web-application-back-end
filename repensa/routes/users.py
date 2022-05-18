import sanic as sn
from connection import create_pool
from mappers import map_users
import hashlib as hs
from configuration import SECRET_KEY
import jwt

users = sn.Blueprint('users', url_prefix='/users')

@users.get('/')
async def get_users(request):
    pool = await create_pool()
    connection = await pool.acquire()

    query = """
        SELECT id, name, email
        FROM users
    """
    try:
        result = await connection.fetch(query)  
        result = [map_users(result) for result in result]
        response = result
        return sn.json(response, 200)
    except Exception as error :
        print(f"{error}")
        return sn.json({"message": f"{error}"})

@users.post('/')
async def post_users(request):
    pool = await create_pool()
    connection = await pool.acquire()

    name = request.json.get('name')
    email = request.json.get('email')
    password = str(request.json.get('password'))

    query = """
        INSERT INTO users (name, email, password)
        VALUES ($1, $2, $3)
    """
    try:

    ## password must be transformed into string, and .encode() method used so
    ## it transforms it into bytes so it can be used in hash and hexed

        password = password.encode()
        password = hs.sha256(password).hexdigest()
        await connection.execute(query, name, email, password)
        return sn.json({"message": "user registered"})
    except Exception as error:
        print(f"{error}")
        return sn.json({"message": f"{error}"})

@users.post('/login')
async def users_login(request):
    pool = await create_pool()
    connection = await pool.acquire()
    
    email = request.json.get('email')
    password = request.json.get('password')
    hash_password = hs.sha256(str(password).encode()).hexdigest()

    query_login = """
        SELECT password 
        FROM users
        WHERE email = $1
    """

    query_return = """
        SELECT id, name, email
        FROM users
        WHERE email = $1
    """
    try:
        result = await connection.fetch(query_login, email)
        result = [map_users(result) for result in result]
        db_password = result[0].get('password')
        if db_password == hash_password:
            user = await connection.fetch(query_return, email)
            user = [map_users(user) for user in user]

            key = SECRET_KEY
            payload = {
                "message": "user logged in",
                "user": user
            }
            token = jwt.encode(payload, key, "HS256")
            return sn.json(token)
    except Exception as error:
        print(f"{error}")
        return sn.json({"message": f"{error}"})

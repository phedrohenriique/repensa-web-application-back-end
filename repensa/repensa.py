import sanic as sn

## instantiated Sanic Server

## can start server with sanic repensa.app or python repensa.py (with app.run method)

app = sn.Sanic('repensa_application')

@app.get('/')
async def server_initiated(request):
    print('server is running on PORT : 8800')
    return sn.json({"message":"server is on"})

## can configure the server parameters after the routes are set

app.run(host='0.0.0.0',port=8800)
import sanic as sn

## instantiated Sanic Server

app = sn.Sanic('repensa_application')

@app.get('/')
async def server_initiated(request):
    print('server is running on PORT : 8800')
    return sn.json({"message":"server is on"})

## can configure the server parameters after the routes are set

app.run(port=8800)
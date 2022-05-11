from xmlrpc import server
import sanic as sn
import routes as rt

## instantiated Sanic Server

## can start server with sanic repensa.app or python repensa.py (with app.run method)

app = sn.Sanic('repensa')
app.blueprint(rt.routes)

app.run(host='0.0.0.0', port=8800, debug=True)
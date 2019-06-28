'''
Serve file.
'''
from aiohttp import web
from aiohttp_jwt import JWTMiddleware

from chunked_app import handle as chunked_handle
from standard_app import handle as standard_handle
from settings import jwt_secret



app = web.Application(
    middlewares=[
        JWTMiddleware(jwt_secret, auth_scheme='JWT', algorithms='HS256')
    ]
)
app.add_routes([
    web.get('/chunked', chunked_handle),
    web.get('/standard', standard_handle)
])

web.run_app(app)

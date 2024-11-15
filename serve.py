from asyncio import sleep
from os import environ

from aiohttp import ClientSession, ClientTimeout, web

BASE_URL = environ.get('RENDER_EXTERNAL_URL', '')
PORT = environ.get('PORT', '')

route = web.RouteTableDef()


@route.get('/', allow_head=True)
async def root_route_handler(_):
    return web.Response(status=200, text='Server pinging...')


async def ping_server():
    attempt = 1
    while attempt < 6:
        try:
            if not BASE_URL:
                raise ValueError(f'PING_URL not provided! Retrying in 10 seconds ({attempt}/5).')
            async with ClientSession(timeout=ClientTimeout(total=10)) as session, session.get(BASE_URL, ssl=False) as res:
                if res.status != 200:
                    raise ValueError(f'ERROR, got response {res.status}. Retrying in 10 seconds ({attempt}/5).')
            await sleep(600)
        except Exception:
            await sleep(10)
            attempt += 1


web_app = web.Application(client_max_size=30000000)
web_app.add_routes(route)
server = web.AppRunner(web_app)
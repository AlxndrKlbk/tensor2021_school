import json
from functools import partial
from objects.MainEntities import Scenario, Enemies, Room
from aiohttp import web
import aiofiles
import aiohttp_cors
from asgiref.sync import sync_to_async

routes = web.RouteTableDef()
rus_json_dumps = partial(json.dumps, ensure_ascii=False)

@routes.get('/scenarios_list')
async def scenarios_list(request):
    scenario = Scenario()
    result = await scenario.get_scenario_list()

    return web.json_response({'result': result}, dumps=rus_json_dumps)


if __name__ == '__main__':
    app = web.Application()

    # routes.static('/script', 'static/script')
    # routes.static('/css', 'static/css')
    app.add_routes(routes)

    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*")})
    for route in app.router.routes():
        cors.add(route)

    web.run_app(app, host='127.0.0.1', port=8888)

# if __name__ == "__main__":
#     test = scenarios_list("nothing")
#     print(test)
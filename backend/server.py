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


@routes.get('/get_rooms')
async def get_rooms(request):
    result = {}
    room = Room()
    data = list(map(int, request.headers['rooms_id'].split(sep=",")))
    for room_id in data:
        result[room_id] = await room.find_entity('rooms_id', room_id)

    return web.json_response({'result': result}, dumps=rus_json_dumps)


@routes.get('/get_enemies')
async def get_enemies(request):
    result = {}
    room = Enemies()
    data = list(request.headers['enemies_names'].split(sep=","))
    for enemie_name in data:
        result[enemie_name] = await room.find_entity('name', enemie_name)
    return web.json_response({'result': result}, dumps=rus_json_dumps)


@routes.post('/save_scenario')
async def save_scenario(request):
    result = {}
    # frontend/store/createScenario.js
    return web.json_response({'result': result}, dumps=rus_json_dumps)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)

    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*")})
    for route in app.router.routes():
        cors.add(route)

    web.run_app(app, host='127.0.0.1', port=8888)

# if __name__ == "__main__":
#     test = scenarios_list("nothing")
#     print(test)
import asyncio
import requests
import requests_cache
import config

import functools

def set_plant_type(plant_type):
    try:
        selected_type = config.plant_type_path[plant_type]

        print(plant_type + " selected")
        return selected_type
    except KeyError:
        print("no type for plant type {plant_type}, veg or fruit".format(plant_type=plant_type))


class static_api:
    def __init__(self, data_path=None):
        """
        :param data_path: path for the statics api
        """
        self.data_path = data_path

    async def fatch_data_by_path(self):
        """
           fetch the data from gov by path
           :return: json with the requested
        """
        requests_cache.install_cache(cache_name='envents_cacheh', backend='memory', expire_after=60)

        req_string = config.israel_path_api.format(data_path=self.data_path)
        print(req_string)
        gov_data = requests.get(req_string)
        print(gov_data.json())
        return gov_data.json()




async def main():
    c1 = static_api('12,2,3')
    f1 = await c1.fatch_data_by_path()


asyncio.run(main())

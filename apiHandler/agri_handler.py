import asyncio
import requests
import requests_cache
import config
from api_statics_class import static_api

def set_plant_type(plant_type):
    try:
        selected_type = config.plant_type_path[plant_type]

        print(plant_type + " selected")
        return selected_type
    except KeyError:
        print("no type for plant type {plant_type}, veg or fruit".format(plant_type=plant_type))


class agri_handler(static_api):
    async def fatch_all_plant_type(self ):
        """
           fetch the data from gov
           :return: json with the requested
        """

        plantes
        # req_string = config.israel_path_api.format(path=self.data_path, plant_index="", data_type="")
        # print(req_string)
        # plants_data = requests.get(req_string)
        #
        # return plants_data.json()

    async def fatch_by_plant_index(self, plant_index, data_type=""):
        """
           fetch the data from gov
           :return: json with the requested
        """
        try:
            data_type = "," + str(config.data_type_path[data_type])
        except KeyError:
            data_type = ""
        plant_index = "," + str(plant_index)
        req_string = config.israel_path_api.format(path=self.data_path, plant_index=plant_index,

                                                   data_type="")

        plants_data = requests.get(req_string)
        return plants_data.json()


async def main():
    c1 = static_api('veg')
    f1 = await c1.fatch_by_plant_index(20)


asyncio.run(main())

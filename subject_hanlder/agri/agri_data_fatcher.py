import config
import asyncio

from apiHandler.static_api_functions import fatch_data_by_path

async def get_full_plants_data(type,plant_index="",data_type=""):
    if plant_index!="":
        plant_index=","+plant_index
    if data_type != "":
        data_type = "," + data_type
    req_string=type+plant_index+data_type

    return await fatch_data_by_path(req_string)


async def get_sumed_agri_data(type=config.agri_type_path['sumed']):
    return await get_full_plants_data(type)



async def get_full_agri_data():


    return await fatch_data_by_path()



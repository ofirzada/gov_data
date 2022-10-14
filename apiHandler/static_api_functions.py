import asyncio

import pandas as pd
import requests
import requests_cache
import config

async def fatch_data_by_path(data_path):
    """
       fetch the data from gov by path
       :return: json with the requested
    """
    requests_cache.install_cache(cache_name='envents_cacheh', backend='memory', expire_after=60)

    req_string = config.israel_path_api.format(data_path=data_path)
    print(req_string)
    pd.DataFrame
    gov_data = requests.get(req_string)
    return gov_data.json()




# asyncio.run(fatch_data_by_path('12,2,3,20,1323'))
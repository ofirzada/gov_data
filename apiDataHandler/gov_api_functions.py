import requests

import config


# requests_cache.install_cache(cache_name='envents_cacheh', backend='memory', expire_after=60)


async def fatch_data_by_path(data_path):
    """
       fetch the data from gov by path
       :return: json with the requested
    """

    # req_string = config.israel_path_api.format(data_path=data_path)

    http_data = config.israel_path_api
    http_data['params']['id'] = data_path
    gov_data = requests.get(url=http_data['url'], params=http_data['params'])
    print(gov_data.url)
    return gov_data


async def fatch_data_by_cathalog(subject, id=1):
    """
       fetch the data from gov by path
       :return: json with the requested
    """
    # req_string = config.israel_path_api.format(data_path=data_path)

    http_data = config.israel_subject_api

    print(subject, id)

    http_data['params']['id'] = id

    http_data['params']['subject'] = subject

    gov_data = requests.get(url=http_data['url'], params=http_data['params'])

    return gov_data

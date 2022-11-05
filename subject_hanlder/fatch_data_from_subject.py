import asyncio

import apiDataHandler.gov_api_functions
import dataHandler.path_data


async def update_cath_json(item):
    levels_list = (list(map(lambda ld: str(ld), item['path'])))
    path = (','.join(levels_list))
    item['df'] = await dataHandler.path_data.get_data_from_path(data_path=path)
    return item


async def get_data_from_subject(subject, id):
    catalog_path = await get_subjects(subject, id)
    data_task = []
    for item in catalog_path:
        data_task.append(asyncio.create_task(update_cath_json(item)))
        print('collectin ' + str(len(data_task)) + ' data points')
        if len(data_task) > 1:
            break
    df_subject = await asyncio.gather(*data_task)
    return df_subject


async def get_subjects(subject, level):

    subject_cat = await apiDataHandler.gov_api_functions.fatch_data_by_cathalog(subject, level)
    if subject_cat.status_code != 200:
        print('failed at ' +subject_cat.url)
        return subject_cat
    else:
        catalog_path = subject_cat.json()['catalogs']['catalog']
        return catalog_path





async def show_data():
    data_json = await get_data_from_subject(12, 3)

    # show(*list(map(lambda item:item['df'],data_json)))

# asyncio.run(show_data())

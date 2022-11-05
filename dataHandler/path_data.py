import asyncio
import pandas as pd
from pandasgui import show
import config
from .validate_path import get_path_data_into_col,get_reduce_data
from apiDataHandler.gov_api_functions import fatch_data_by_path


async def gov_data_to_df(fatch_data):
    subject_df = pd.json_normalize(fatch_data['DataSet']['Series'], record_path=['obs'],
                                  meta=config.agri_meta,
                                  errors='ignore',
                                   max_level=10000
                                   )

    df2=get_path_data_into_col(df=subject_df)
    df3=get_reduce_data(subject_df)
    # df_join=subject_df.join(df2,rsuffix='_caller')
    subject_df=subject_df.join(df3)
    #
    #
    # df_join=df_join.drop(index=1,columns= ['id_caller', 'path'])

    subject_df=subject_df.astype(str)
    subject_df=subject_df.rename(columns={"unit.name": "units","unit.value": "unitsV"})


    return subject_df


async def get_data_from_path(data_path='12,2'):
    data = await fatch_data_by_path(data_path=data_path)
    if data.status_code==200:
        return await gov_data_to_df(data.json())
    print('data not found at {url} '.format(url=data.url))


async def get_all_data_from_subject(data_paths=[[12,2]]):
    """

    :param data_path:path of data
    :return: data_frames of mulipale paths
    """
    request_from_gov = []
    for levels in data_paths:
        if (type(levels)==list):
            levels_list=levels
            levels_list = (list(map(lambda ld: str(ld), levels_list)))
            levels=(','.join(levels_list))
            request_from_gov.append(asyncio.create_task(get_data_from_path(data_path= str(levels))))
    df_subject=(await asyncio.gather(*request_from_gov))
    return df_subject






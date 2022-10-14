import asyncio
import pandas as pd
from subject_hanlder.agri import agri_data_fatcher as agi_data
from pandasgui import show
import config
from get_path_data import get_path_data

async def full_plants_df(condition=None):
    fatch_data = await agi_data.get_sumed_agri_data()

    plants_df = pd.json_normalize(fatch_data['DataSet']['Series'], record_path=['obs'],
                                  meta=config.agri_meta,
                                  errors='ignore')

    df2=(get_path_data(df=plants_df))
    plants_df.info()
    print(plants_df)
    plants_df.join(df2)
    show(plants_df.join(df2))
    return plants_df.join(df2)



asyncio.run(full_plants_df())

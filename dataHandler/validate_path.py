import functools

import pandas as pd

def level_data_validator(data,col):
    if data==None:
        return ''

    return data[col]


# def get_path_data(df, values=['name', 'value']):
#     """
#
#     :param df:
#     :param values: values to reduce
#     :return: df
#     """
#     values_df = pd.DataFrame()
#
#     for data_path in df.path:
#         levels_data = list(map(lambda d: data_path[d], data_path.keys()))
#         index_data = {}
#         for col in values:
#             levels_name = (list(map(lambda ld:level_data_validator(ld,col), levels_data)))
#             index_data[col] = functools.reduce(lambda a, b: str(a) + "," + str(b), levels_name)
#         values_df = values_df.append(index_data, ignore_index=True)
#     values_df.columns = list(map(lambda n: "path_" + n, values_df.columns))
#
#     return values_df

def get_path_data_into_col(df):
    df_path_Data=pd.DataFrame(columns=['level1.value', 'level1.name', 'level2.value', 'level2.name',
       'level3.value', 'level3.name', 'level4.value', 'level4.name',
       'name_id.value', 'name_id.name', 'id'])

    for i in df.index:
        levels_data=pd.json_normalize(df['path'][i])
        levels_data['id']=df['id'][i]

        df_path_Data=df_path_Data.append(levels_data,ignore_index=True)
    return df_path_Data




def get_reduce_data(df, values=['name']):
    """

    :param df:
    :param values: values to reduce
    :return: df
    """
    values_df = pd.DataFrame()

    for data_path in df.path:
        levels_data = list(map(lambda d: data_path[d], data_path.keys()))
        index_data = {}
        for col in values:
            levels_name = (list(map(lambda ld:level_data_validator(ld,col), levels_data)))
            index_data[col] = functools.reduce(lambda a, b: str(a) + "," + str(b), levels_name)
        values_df = values_df.append(index_data, ignore_index=True)
    values_df.columns = list(map(lambda n: "path_" + n, values_df.columns))

    return values_df



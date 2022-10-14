
import pandas as pd
import functools
def get_path_data(df,values=['name','value']):
    """

    :param df:
    :param values: values to reduce
    :return: df
    """
    values_df = pd.DataFrame()

    for data_path in df.path:
        levels_data=list(map(lambda d:data_path[d], data_path.keys()))
        index_data={}
        for col in values :
            levels_name=(list(map(lambda ld:ld[col],levels_data)))
            index_data[col]=functools.reduce(lambda a, b: str(a)+","+str(b), levels_name)
        values_df = values_df.append(index_data,ignore_index=True)
    values_df.columns =list(map(lambda n:"path_"+n,values_df.columns))

    return values_df

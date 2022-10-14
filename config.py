
israel_argi_subject_api='https://apis.cbs.gov.il/series/catalog/level?subject=12&format=json&download=false&id=4'
# israel_agri_path_api='https://apis.cbs.gov.il/series/data/path?id={path}{plant_index}{data_type}
israel_path_api= 'https://apis.cbs.gov.il/series/data/path?id={data_path}&format=json&download=false'
agri_type_path={
    'sumed':'12,2',
    'veg':'12,2,3',
    'fruit':'12,2,4'
}
data_type_path={
    'mass':'1324',
    'price':'1323'
}
#
# agri_meta=['id', 'update',['unit','value'],['path','level1','name'],['path','level2','name'],['path','level3','name'],['path','level4','name']]


agri_meta=['id', 'update',['unit','value'],'path']
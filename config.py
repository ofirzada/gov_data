israel_argi_subject_api = 'https://apis.cbs.gov.il/series/catalog/level?subject=12&format=json&download=false&id=4'
israel_subject_api = {
    'url': 'https://apis.cbs.gov.il/series/catalog/level',
    'params': {
        'format': 'json',
        'lang': 'he',

    }

}

israel_path_api = {
    'url': 'https://apis.cbs.gov.il/series/data/path',
    'params': {
        'format': 'json',
        'lang': 'he',

    }
}

agri_type_path = {
    'sumed': '12,2',
    'veg': '12,2,3',
    'fruit': '12,2,4'
}
data_type_path = {
    'mass': '1324',
    'price': '1323'
}
#
# agri_meta=['id', 'update',['unit','value'],['path','level1','name'],['path','level2','name'],['path','level3','name'],['path','level4','name']]


agri_meta = ['id', 'update', ['unit', 'value'],['unit', 'name'], 'path']

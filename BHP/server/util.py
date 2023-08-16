import pickle
import json
import sklearn
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,area_type,availability,total_sqft,bath,balcony,bhk):

    try:
        if location == 'other':
            location_index = 0
        else:
            location_index = __data_columns.index(location.lower().strip())
    except:
        location_index = -1

    
    try:
        if area_type == 'Built-up  Area':
            area_type_index = 0
        else:
            area_type_index = __data_columns.index(area_type.lower().strip())
    except:
        area_type_index = -1

    x = np.zeros(len(__data_columns))

    x[0] = availability
    x[1] = total_sqft
    x[2] = bath
    x[3] = balcony
    x[4] = bhk
    
    if location_index>0:
        x[location_index] = 1
    
    if area_type_index >0:
        x[area_type_index] =1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as a:
        __data_columns = json.load(a)['data_columns']
        __locations = __data_columns[5:-4]  

    global __model
    if __model is None:
        with open('./artifacts/BHP_Model.pickle', 'rb') as m:
            __model = pickle.load(m)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar','Super built-up  Area',1,1000,2,0,2))
import numpy as np
import requests

#print('MetaInfo:',res['response']['metaInfo'])
#print('MatrixEntry', res['response']['matrixEntry'])
#print('a00', res['response']['matrixEntry'][0]['summary'])
#print('a01', res['response']['matrixEntry'][1]['summary'])

# seems like the maximum is 15x100 per request
# departure, use now or some date?

def Here_maps(lat,lgn,lat_col,lgn_col):
    " Request to here Maps for getting travel time & distance between points "
    build_string = ''

    for i in range(0,len(lat)):
        build_string = build_string + 'start' + str(i) + '=' + str(lat[i]) + '%2C' + str(lgn[i]) + '&'
    for i in range(0,len(lat_col)):
        build_string = build_string + 'destination' + str(i) + '=' + str(lat_col[i]) + '%2C' + str(lgn_col[i]) + '&'

    r = requests.get('https://matrix.route.api.here.com/routing/7.2/calculatematrix.json?'+
                     #'start0=-13.0094%2C-38.5322&destination0=-13.0094%2C-38.5322&destination1=-12.9567%2C-38.3539&'\
                      build_string +
                     'summaryAttributes=distance,traveltime&'\
                     'mode=fastest%3Bcar&'\
                     'app_id=devportal-demo-20180625&'\
                     'app_code=9v2BkviRwi9Ot26kp2IysQ')
    res = r.json()
 
    Num_Elem_i = len(lat)
    Num_Elem_j = len(lat_col)
    D = np.zeros((Num_Elem_i,Num_Elem_j))
    T = np.zeros((Num_Elem_i,Num_Elem_j))
    cont = 0

    for i in range (0,Num_Elem_i):
            for j in range (0,Num_Elem_j):
                    D[i][j] = res['response']['matrixEntry'][cont]['summary']['distance']/1000
                    T[i][j] = res['response']['matrixEntry'][cont]['summary']['travelTime']/3600
                    cont += 1
    return D,T

def Split_coord(lat,lgn):
    " Separate latitute and longitude in vector of maximum 10 values "
    lat_2 = []
    lgn_2 = []
    lat_2_x = []
    lgn_2_x = []
    a = 0
    b = np.minimum(10,len(lat))
    cont_break = 0

    if (len(lat) > 10):
        while (len(lat) > cont_break):
            for i in range(a,b):
                lat_2.append(lat[i])
                lgn_2.append(lgn[i])
                cont_break += 1
            aux = b    
            b += np.minimum(10,len(lat)-b)
            a = aux
            lat_2_x.append(lat_2)
            lgn_2_x.append(lgn_2)
            lat_2 = []
            lgn_2 = []
    else:
        lat_2_x.append(lat)
        lgn_2_x.append(lgn)
    return lat_2_x,lgn_2_x

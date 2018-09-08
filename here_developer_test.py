import requests
import numpy as np
import time
from Here_Maps import Here_maps,Split_coord

#r = requests.get('https://matrix.route.api.here.com/routing/7.2/calculatematrix.json?start0=52.5139%2C13.3576&start1=52.5214%2C13.4155&start2=52.5253%2C13.3693&destination0=52.5411%2C13.2127&destination1=52.5163%2C13.3780&destination2=52.4920%2C13.2849&destination3=52.4987%2C13.5228&destination4=52.5547%2C13.4578&summaryAttributes=distance&mode=fastest%3Bcar&app_id=oOQlyMCKNDgff79nhfve&app_code=M9aHgjD9HuiBmp313fKCvg')

lat = [-12.869658,
-12.984005,
-13.013010,
-13.006691,
-12.978834,
-12.981857,
-12.969814,
-13.001721]
#-12.974547,
#-13.010015]
#-12.864899,
#-12.869658]

lgn = [-38.445192,
-38.434759,
-38.489694,
-38.524403,
-38.454730,
-38.463442,
-38.411875,
-38.450314]
#-38.420095,
#-38.516900]
#-38.456736,
#-38.445192]

lat_2 = lat
lgn_2 = lgn
#lat_2 = lat+lat+lat
#lgn_2 = lgn+lgn+lgn
#lat_2 = lat+lat+lat[:5]
#lgn_2 = lgn+lgn+lgn[:5]

start_time = time.time()
coord = Split_coord(lat_2,lgn_2)
lat_3 = coord[0]
lgn_3 = coord[1]

for i in range(0,len(lat_3)):
    for j in range(0,len(lgn_3)):
        res = Here_maps(lat_3[i],lgn_3[i],lat_3[j],lgn_3[j])               
        if (j == 0):
            D = res[0]
            T = res[1]
        else:
            D = np.concatenate((D,res[0]),axis=1)
            T = np.concatenate((T,res[1]),axis=1)
    if (i == 0):
        M_d = D
        M_t = T
    else:
        M_d = np.concatenate((M_d,D))
        M_t = np.concatenate((M_t,T))
    D = []
    T = []
#np.shape(M_d)
#np.shape(M_t)
elapsed_time = time.time() - start_time
print("Time elapsed (seconds)", elapsed_time) 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('housesalesprediction/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = pd.read_csv('housesalesprediction/kc_house_data.csv')
print(data.shape)
data.head()

data.drop(['id','date'],axis=1,inplace=True)

from sklearn.model_selection import train_test_split

Y = data.price.values

X = data.drop('price',axis=1)

train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.33,random_state = 42)
train_x.shape,train_y.shape,test_x.shape,test_y.shape

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100)
model.fit(train_x,train_y)

preds = model.predict(test_x)

from sklearn.metrics import mean_absolute_error

MAE = mean_absolute_error(preds,test_y)

import pickle

with open('rf.pkl','wb') as rfpkl:
    pickle.dump(model,rfpkl)

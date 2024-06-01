import pandas as pd
import os
from matplotlib.colors import ListedColormap
import logging

# check dataset directory
newDataset_path = os.path.join(os.getcwd(), 'newDataset')

# if the newData_path directory not exists make newDataset directory
if (os.path.exists(newDataset_path)):
    os.chdir(newDataset_path)
else:
    print('No directory named "newdataset"')
    exit()

# read csv file
data = pd.read_csv('clustered_rental_dataset.csv',encoding='cp949')
data['대여월']=data['대여일자'].str.split('-').str[1].astype(int)
data['대여일']=data['대여일자'].str.split('-').str[2].astype(int)

# GridSearch
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

# feature, target 설정
X=data[['대여소번호', '대여월', '대여시간대', '일 강수량', '기온(°C)']]
#X=data[['대여월', '대여시간대', '일 강수량', '기온(°C)']]
y = data['cluster']

# train, test set 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
logging.warning('train test split done')

# StandardScaler를 이용하여 정규화
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
logging.warning('standard scaler done')

# GridSearch
dt=DecisionTreeClassifier(random_state=0)
params = {
    'max_depth': [6, 12],
    'min_samples_leaf': [8, 18],
    'min_samples_split': [8, 20]
}
# best hyper parameter:
#  {'max_depth': 12, 'min_samples_leaf': 8, 'min_samples_split': 8}

grid_cv = GridSearchCV(dt, param_grid=params, cv=2, n_jobs=-1)
grid_cv.fit(X_train_scaled, y_train)
print('best hyper parameter:\n', grid_cv.best_params_)
print('best accuracy:\n', grid_cv.best_score_)
best_dt = grid_cv.best_estimator_
logging.warning('grid search done')

# deicisionTree classification
y_pred = best_dt.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print('accuracy:', accuracy)
logging.warning('decision tree done')

# confusion matrix
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('confusion matrix:\n', conf_matrix)

# classification report
from sklearn.metrics import classification_report
class_report = classification_report(y_test, y_pred)
print('classification report:\n', class_report)

# evaluation using k-fold cross validation
from sklearn.model_selection import cross_val_score
import numpy as np
scores = cross_val_score(best_dt, X, y, cv=5)
print('cross validation scores:', scores)
print('cross validation mean score:', np.mean(scores))

# evaluation using RMSE
from sklearn.metrics import mean_squared_error
from math import sqrt
rmse = sqrt(mean_squared_error(y_test, y_pred))
print('RMSE:', rmse)

# evaluation using MAE
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
print('MAE:', mae)
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

#SVM classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# feature, target 설정
X=data[['대여소번호', '대여월', '대여시간대', '일 강수량', '기온(°C)']]
#X = data[['대여월', '대여시간대', '일 강수량', '기온(°C)']]
y = data['cluster']

# train data와 test data로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logging.warning('train test split done')

# StandardScaler를 이용하여 정규화
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
logging.warning('standard scaler done')

# SVM classification
svm = SVC(kernel='linear', C=1.0, random_state=0)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
logging.warning('SVM done')

# 정확도 출력
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

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
scores = cross_val_score(estimator=svm, X=X_train, y=y_train, cv=10, n_jobs=1)
print('cross validation scores:', scores)
print('cross validation accuracy: %.3f +/- %.3f' % (scores.mean(), scores.std()))

# evaluation using RMSE
from sklearn.metrics import mean_squared_error
from math import sqrt
rmse = sqrt(mean_squared_error(y_test, y_pred))
print('RMSE:', rmse)

# evaluation using MAE
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
print('MAE:', mae)

exit()
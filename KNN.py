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

# KNN classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

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

# k값에 따른 accuracy 비교해서 best K 찾기
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

accuracy = []
for i in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    accuracy.append(accuracy_score(y_test, y_pred))
    
plt.plot(range(1, 11), accuracy, marker='o')
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')
plt.show()

# best K로 KNN classification
best_k = np.argmax(accuracy) + 1
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
logging.warning('knn done')

# accuracy
accuracy = accuracy_score(y_test, y_pred)
print('accuracy:', accuracy)

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
scores = cross_val_score(knn, X, y, cv=5)
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

exit()

# confusion matrix visualization
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(conf_matrix, annot=True, cmap='Blues', xticklabels=['cluster0', 'cluster1', 'cluster2', 'cluster3', 'cluster4'], yticklabels=['cluster0', 'cluster1', 'cluster2', 'cluster3', 'cluster4'])
plt.xlabel('prediction')
plt.ylabel('target')
plt.title('confusion matrix')
plt.show()
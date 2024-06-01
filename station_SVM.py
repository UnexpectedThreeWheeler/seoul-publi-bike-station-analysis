import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
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
os.chdir(newDataset_path)
YDPstationRentalReturn = pd.read_csv('YDP_station_property_with_cluster.csv', encoding='cp949')

#SVM classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# StandardScaler를 이용하여 정규화
scaler = StandardScaler()
scaler.fit((YDPstationRentalReturn[['대여건수', '반납건수', '대여반납비율']]))
YDPstationRentalReturn_scaled = scaler.transform((YDPstationRentalReturn[['대여건수', '반납건수', '대여반납비율']]))
X = pd.DataFrame(YDPstationRentalReturn, columns=['대여건수', '반납건수', '대여반납비율'])
y=YDPstationRentalReturn['cluster']
logging.warning('standard scaler done')

# train data와 test data로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logging.warning('train test split done')

# SVM 모델 생성
svm = SVC(kernel='linear', C=1.0, random_state=0)
svm.fit(X_train, y_train)

# test data로 예측
y_pred = svm.predict(X_test)
logging.warning('SVM done')

# 정확도 출력
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

# 리소스 사용량이 너무 커서 시각화 코드는 주석처리
'''# 시각화
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # 마커와 컬러맵 설정
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 결정 경계 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=[cmap(idx)],
                    marker=markers[idx], label=cl)

    # 테스트 샘플 부각
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='',
                    alpha=1.0, linewidth=1, marker='o',
                    s=55, label='test set')
        
# 시각화
X_combined_std = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X=X_combined_std, y=y_combined, classifier=svm, test_idx=range(105, 150))
plt.xlabel('Rental Count')
plt.ylabel('Return Count')
plt.legend(loc='upper left')
plt.show()
'''
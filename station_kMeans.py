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
YDPstationRentalReturn= pd.read_csv('YDP_station_rental_return_dataset.csv', encoding='cp949')

# kmeans clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# StandardScaler를 이용하여 정규화
scaler = StandardScaler()
scaler.fit(YDPstationRentalReturn[['대여건수', '반납건수', '대여반납비율']])
YDPstationRentalReturn_scaled = scaler.transform((YDPstationRentalReturn[['대여건수', '반납건수', '대여반납비율']]))
YDPstationRentalReturn_scaled = pd.DataFrame(YDPstationRentalReturn, columns=['대여건수', '반납건수', '대여반납비율'])
logging.warning('standard scaler done')

# KMeans 알고리즘을 이용하여 군집화, elbow method를 이용하여 best K 찾기
distortions = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(YDPstationRentalReturn_scaled)
    distortions.append(kmeans.inertia_)
    
plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

# best_k=3 사용하여 KMeans 알고리즘을 이용하여 군집화
print('best K=3')
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(YDPstationRentalReturn_scaled)
YDPstationRentalReturn_scaled['cluster'] = kmeans.labels_
logging.warning('kmeans clustering done')

# 군집화 결과 시각화
plt.scatter(YDPstationRentalReturn_scaled['대여건수'], YDPstationRentalReturn_scaled['반납건수'], c=YDPstationRentalReturn_scaled['cluster'], cmap='viridis')
plt.xlabel('Rental Count')
plt.ylabel('Return Count')
plt.show()

# 군집화 결과 evaluation
from sklearn.metrics import silhouette_samples, silhouette_score
silhouette_avg = silhouette_score(YDPstationRentalReturn_scaled, YDPstationRentalReturn_scaled['cluster'])
silhouette_values = silhouette_samples(YDPstationRentalReturn_scaled, YDPstationRentalReturn_scaled['cluster'])
print('silhouette_avg:', silhouette_avg)

# evaluation 결과 시각화
y_lower = 10
plt.figure(figsize=(10, 10))
for i in range(3):
    cluster_silhouette_values = silhouette_values[YDPstationRentalReturn_scaled['cluster'] == i]
    cluster_silhouette_values.sort()
    y_upper = y_lower + cluster_silhouette_values.shape[0]
    plt.fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_silhouette_values, facecolor='blue', alpha=0.7)
    plt.text(-0.05, y_lower + 0.5 * cluster_silhouette_values.shape[0], str(i))
    y_lower = y_upper + 10
    
plt.axvline(x=silhouette_avg, color='red', linestyle='--')
plt.xlabel('Silhouette coefficient values')
plt.ylabel('Cluster label')
plt.show()

# 군집화 결과 병합
YDPstationPropertyWithCluster = pd.merge(YDPstationRentalReturn, YDPstationRentalReturn_scaled['cluster'], left_index=True, right_index=True)
YDPstationPropertyWithCluster.to_csv('YDP_station_property_with_cluster.csv', encoding='cp949', index=False)

YDP_bike_rental_dataset_2023=pd.read_csv('YDP_bike_rental_dataset_2023.csv',encoding='cp949')
print('영등포 내 대여소별 대여/반납건수 및 대여반납비율에 군집화 결과 병합\n', YDPstationPropertyWithCluster)

clustered_rental_dataset = pd.merge(YDP_bike_rental_dataset_2023, YDPstationPropertyWithCluster, left_on=['대여소번호', '대여시간대'], right_on=['대여소번호', '시간대'], how='left')
clustered_rental_dataset=clustered_rental_dataset.drop(columns= ['이용건수', '시간대'])
clustered_rental_dataset.to_csv('clustered_rental_dataset.csv', encoding='cp949', index=False)
print('기존 영등포 내 대여이력 정보에 대여소 속성 및 군집화 결과 병합\n', clustered_rental_dataset)

exit()
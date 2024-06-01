import pandas as pd
import os

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
YDP_bike_rental_dataset_2023=pd.read_csv('YDP_bike_rental_dataset_2023.csv',encoding='cp949')
YDPstationRentalReturn_data=pd.read_csv('YDP_station_rental_return_dataset.csv',encoding='cp949')
YDP_bike_rental_with_station_property_2023 = pd.merge(YDP_bike_rental_dataset_2023, YDPstationRentalReturn_data, left_on=['대여소번호', '대여시간대'], right_on=['대여소번호', '시간대'], how='left')
YDP_bike_rental_with_station_property_2023=YDP_bike_rental_with_station_property_2023.drop(columns= ['이용건수', '시간대'])
YDP_bike_rental_with_station_property_2023.astype({'대여소번호':int, '대여시간대':int, '일 강수량':float, '기온(°C)':float, '대여건수':int, '반납건수':int, '대여반납비율':float})
print('기존 영등포 내 대여이력 정보에 대여소 속성 병합한 데이터\n', YDP_bike_rental_with_station_property_2023)

# 영등포 내 대여이력 정보에 대여소 속성 병합한 데이터 저장, (8764288, 11)
YDP_bike_rental_with_station_property_2023.to_csv('YDP_bike_rental_with_station_property_2023.csv', encoding='cp949', index=False)
print('Data saved successfully!')
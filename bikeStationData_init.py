import pandas as pd
import matplotlib.pyplot as plt
import os

# check dataset directory
data_path = os.path.join(os.getcwd(), 'dataset')
newDataset_path = os.path.join(os.getcwd(), 'newDataset')

# if the newData_path directory not exists make newDataset directory
if not os.path.exists(newDataset_path):
    os.mkdir(newDataset_path)
    
# check if the directory exists
if(os.path.exists(data_path)): 
    os.chdir(data_path) # change the current working directory to the directory where the data is stored
else:
    print('No directory named "dataset"')
    exit()
    
# read excel file from 5th row(delete header)
bikeStation_Info = pd.read_csv('공공자전거 대여소 정보(23.12월 기준).csv',
                               encoding='cp949',
                               skiprows=5,
                               names=['대여소번호', '대여소명', '자치구', '상세주소', '위도', '경도', '설치시기', 'LCD 거치대수', 'QR 거치대수', '운영방식'],
                               usecols=['대여소번호', '대여소명', '자치구', 'LCD 거치대수', 'QR 거치대수'],
                               #dtype={'대여소번호':int, '위도':float, '경도':float, 'LCD 거치대수':int, 'QR 거치대수':int}
                               )

# 결측치 0으로 채우고 데이터타입 변경
bikeStation_Info.fillna(0, inplace=True)
bikeStation_Info = bikeStation_Info.astype({'대여소번호':int, 'LCD 거치대수':int, 'QR 거치대수':int})

# bikesStation_Info['자치구']가 '영등포구'인 행만 추출
bikeStation_Info = bikeStation_Info[bikeStation_Info['자치구'].str.contains('영등포구')] 
YDP_station_dataset = pd.DataFrame(bikeStation_Info[['대여소번호', '대여소명']], columns=['대여소번호', '대여소명'])

# 데이터 저장
os.chdir(newDataset_path)
YDP_station_dataset.to_csv('YDP_station_dataset.csv', encoding='cp949', index=False)
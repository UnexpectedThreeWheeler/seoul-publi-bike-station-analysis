import pandas as pd
import matplotlib.pyplot as plt
import os

# 데이터프레임 생략 없이 전체 출력
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

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
    
# read csv file
bikeRentalData_2303 = pd.read_csv('서울특별시 공공자전거 이용정보(시간대별)_2303.csv',
                                   encoding='cp949',
                                   skiprows=1,
                                   names=['대여일자', '대여시간대', '대여소번호', '대여소명', '대여구분코드', '성별', '연령대코드', '이용건수', '운동량', '탄소량', '이동거리(M)', '이용시간(분)'],
                                   usecols=['대여일자', '대여시간대', '대여소번호', '대여구분코드', '성별', '연령대코드', '이용건수'],
                                   na_values=['', '기타'],
                                   dtype={'대여시간':int ,'대여소번호':int, '대여구분코드':str, '성별':str, '연령대코드':str, '이용건수':int}
                                   )

bikeRentalData_2306 = pd.read_csv('서울특별시 공공자전거 이용정보(시간대별)_2306.csv',
                                   encoding='cp949',
                                   skiprows=1,
                                   names=['대여일자', '대여시간대', '대여소번호', '대여소명', '대여구분코드', '성별', '연령대코드', '이용건수', '운동량', '탄소량', '이동거리(M)', '이용시간(분)'],
                                   usecols=['대여일자', '대여시간대', '대여소번호', '대여구분코드', '성별', '연령대코드', '이용건수'],
                                   na_values=['', '기타'],
                                   dtype={'대여시간':int ,'대여소번호':int, '대여구분코드':str, '성별':str, '연령대코드':str, '이용건수':int}
                                   )

bikeRentalData_2309 = pd.read_csv('서울특별시 공공자전거 이용정보(시간대별)_2309.csv',
                                   encoding='cp949',
                                   skiprows=1,
                                   names=['대여일자', '대여시간대', '대여소번호', '대여소명', '대여구분코드', '성별', '연령대코드', '이용건수', '운동량', '탄소량', '이동거리(M)', '이용시간(분)'],
                                   usecols=['대여일자', '대여시간대', '대여소번호', '대여구분코드', '성별', '연령대코드', '이용건수'],
                                   na_values=['', '기타'],
                                   dtype={'대여시간':int ,'대여소번호':int, '대여구분코드':str, '성별':str, '연령대코드':str, '이용건수':int}
                                   )

bikeRentalData_2312 = pd.read_csv('서울특별시 공공자전거 이용정보(시간대별)_2312.csv',
                                   encoding='cp949',
                                   skiprows=1,
                                   names=['대여일자', '대여시간대', '대여소번호', '대여소명', '대여구분코드', '성별', '연령대코드', '이용건수', '운동량', '탄소량', '이동거리'],
                                   usecols=['대여일자', '대여시간대', '대여소번호', '대여구분코드', '성별', '연령대코드', '이용건수'],
                                   na_values=['', '기타'],
                                   dtype={'대여시간':int ,'대여소번호':int, '대여구분코드':str, '성별':str, '연령대코드':str, '이용건수':int}
                                   )

# 4개월 데이터 합치기
bikeRentalData_23 = pd.concat([bikeRentalData_2303, bikeRentalData_2306, bikeRentalData_2309, bikeRentalData_2312])

# 중복되는 카테고리 데이터 치환 및 결측치 제거
bikeRentalData_23['성별'].replace(['m', 'f'], ['M', 'F'], inplace=True)
bikeRentalData_23.dropna(inplace=True) # 성별과 연령대코드에서 결측치 발생, 결측치 제거후 (702890, 8)

# 영등포 내 정류소 목록 데이터, 영등포 날씨(시간대별 기온, 일 강수량) 데이터 불러오기
os.chdir(newDataset_path)
YDP_station_dataset = pd.read_csv('YDP_station_dataset.csv', encoding='cp949') # 영등포 내 정류소 목록 데이터, (159, 2)
YDP_weather_dataset = pd.read_csv('YDP_weather_dataset_2023.csv', encoding='cp949') # 영등포 시간대별 기온, 강수량 데이터, (2846, 4)

# YDP_station_dataset에 있는 대여소번호와 일치하는 데이터만 추출 (영등포 내 대여/반납만 추출)
YDP_bikeRentalData_23 = bikeRentalData_23[bikeRentalData_23['대여소번호'].isin(YDP_station_dataset['대여소번호'])]
YDP_bikeRentalData_23.reset_index(drop=True, inplace=True) # 필터링 후 데이터 크기 (702890, 7)
#print('After filtering range-YDP\n', YDP_bikeRentalData_23)

# YDP_station_dataset이랑 대여소번호로 merge(대여소명 추가)
#YDP_bikeRentalData_23 = pd.merge(bikeRentalData_23, YDP_station_dataset, on='대여소번호')
#YDP_bikeRentalData_23.reset_index(drop=True, inplace=True) # 병합 후 데이터 크기 (702890, 10)
#print('After merge YDP list\n', YDP_bikeRentalData_23) # 결측치 없음

# YDP_weather_dataset이랑 일시, 시간대로 merge
# YDP_weather_dataset에 06-08 16시~06-09 13시, 06-30 5시~23시,  12-30 5시~12-31 23시 데이터가 없음, 병합시 기온과 강수량에 결측치 발생
YDP_bikeRentalData_23 = pd.merge(YDP_bikeRentalData_23, YDP_weather_dataset, left_on=['대여일자', '대여시간대'], right_on=['일시', '시간대'], how='left')
YDP_bikeRentalData_23['기온(°C)'].fillna(YDP_bikeRentalData_23['기온(°C)'].mean(), inplace=True) # 기온 결측치 평균값으로 채우기
YDP_bikeRentalData_23['일 강수량'].fillna(0, inplace=True) # 강수량 결측치 0으로 채우기
YDP_bikeRentalData_23.reset_index(drop=True, inplace=True) # 병합 후 데이터 크기 (702890, 11)
YDP_bikeRentalData_23.drop(['일시', '시간대'], axis=1, inplace=True) # 중복되는 칼럼 삭제
#YDP_bikeRentalData_23[YDP_bikeRentalData_23['일시'].isna()].to_csv('missing_data.csv', encoding='cp949', index=False)
#print('After merge YDP weather\n', YDP_bikeRentalData_23)

# 칼럼 순서 변경
YDP_bikeRentalData_23 = YDP_bikeRentalData_23[['대여일자', '대여시간대', '일 강수량', '기온(°C)', '대여소번호', '대여구분코드', '성별', '연령대코드', '이용건수']]

# save the data
YDP_bikeRentalData_23.to_csv('YDP_bike_rental_dataset_2023.csv', encoding='cp949', index=False)
print('YDP_bike_rental_dataset_2023.csv saved successfully!')
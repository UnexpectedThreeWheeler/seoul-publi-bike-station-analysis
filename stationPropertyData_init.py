import pandas as pd
import os

# check dataset directory
data_path = os.path.join(os.getcwd(), 'dataset')
newDataset_path = os.path.join(os.getcwd(), 'newDataset')

# if the newData_path directory not exists make newDataset directory
if (os.path.exists(newDataset_path)):
    os.chdir(newDataset_path)
else:
    print('No directory named "newdataset"')
    exit()
# read csv file
os.chdir(newDataset_path)
YDP_station_dataset = pd.read_csv('YDP_station_dataset.csv', encoding='cp949')

os.chdir(data_path)
bikeRentalReturn_data_2303 = pd.read_csv('서울특별시 공공자전거 대여이력 정보_2303.csv',
                                    encoding='cp949',
                                    na_values=['\\N'],
                                    skiprows=1,
                                    na_filter=False,
                                    names=['자전거번호', '대여일시', '대여대여소번호', '대여대여소명', '대여거치대', '반납일시', '반납대여소번호', '반납대여소명', '반납거치대', '이용시간', '이용거리', '생년', '성별', '이용자종류', '대여대여소ID', '반납대여소ID'],
                                    usecols=['대여대여소번호', '대여일시', '반납대여소번호', '반납일시'],
                                    #dtype={'대여대여소번호':int, '반납대여소번호':int}
                                    )
# 영등포 내에서 반납|대여한 데이터만 추출, 대여소번호가 \N인 데이터 삭제
bikeRentalReturn_data_2303 = bikeRentalReturn_data_2303[bikeRentalReturn_data_2303['대여대여소번호'].isin(YDP_station_dataset['대여소번호']) |
                                                        bikeRentalReturn_data_2303['반납대여소번호'].isin(YDP_station_dataset['대여소번호'])]
bikeRentalReturn_data_2303.replace({'대여대여소번호': {'\\N': 0}, '반납대여소번호': {'\\N': 0}}, inplace=True)
bikeRentalReturn_data_2303 = bikeRentalReturn_data_2303.astype({'대여대여소번호':int, '반납대여소번호':int})
bikeRentalReturn_data_2303 = bikeRentalReturn_data_2303[(bikeRentalReturn_data_2303['대여대여소번호'] != 0) & (bikeRentalReturn_data_2303['반납대여소번호'] != 0)]
bikeRentalReturn_data_2303.reset_index(drop=True, inplace=True)

bikeRentalReturn_data_2306 = pd.read_csv('서울특별시 공공자전거 대여이력 정보_2306.csv',
                                    encoding='cp949',
                                    skiprows=1,
                                    na_filter=False,
                                    na_values=['\\N'],
                                    names=['자전거번호', '대여일시', '대여대여소번호', '대여대여소명', '대여거치대', '반납일시', '반납대여소번호', '반납대여소명', '반납거치대', '이용시간', '이용거리', '생년', '성별', '이용자종류', '대여대여소ID', '반납대여소ID'],
                                    usecols=['대여대여소번호', '대여일시', '반납대여소번호', '반납일시'],
                                    #na_filter=False
                                    )
# 영등포 내에서 반납|대여한 데이터만 추출, 대여소번호가 \N인 데이터 삭제
bikeRentalReturn_data_2306 = bikeRentalReturn_data_2306[bikeRentalReturn_data_2306['대여대여소번호'].isin(YDP_station_dataset['대여소번호']) |
                                                        bikeRentalReturn_data_2306['반납대여소번호'].isin(YDP_station_dataset['대여소번호'])]
bikeRentalReturn_data_2306.replace({'대여대여소번호': {'\\N': 0}, '반납대여소번호': {'\\N': 0}}, inplace=True)
bikeRentalReturn_data_2306 = bikeRentalReturn_data_2306.astype({'대여대여소번호':int, '반납대여소번호':int})
bikeRentalReturn_data_2306 = bikeRentalReturn_data_2306[(bikeRentalReturn_data_2306['대여대여소번호'] != 0) & (bikeRentalReturn_data_2306['반납대여소번호'] != 0)]
                                    
bikeRentalReturn_data_2309 = pd.read_csv('서울특별시 공공자전거 대여이력 정보_2309.csv',
                                    encoding='cp949',
                                    skiprows=1,
                                    na_filter=False,
                                    na_values=['\\N'],
                                    names=['자전거번호', '대여일시', '대여대여소번호', '대여대여소명', '대여거치대', '반납일시', '반납대여소번호', '반납대여소명', '반납거치대', '이용시간', '이용거리', '생년', '성별', '이용자종류', '대여대여소ID', '반납대여소ID', '자전거종류'],
                                    usecols=['대여대여소번호', '대여일시', '반납대여소번호', '반납일시'],
                                    #na_filter=False
                                    )
# 영등포 내에서 반납|대여한 데이터만 추출, 대여소번호가 \N인 데이터 삭제
bikeRentalReturn_data_2309 = bikeRentalReturn_data_2309[bikeRentalReturn_data_2309['대여대여소번호'].isin(YDP_station_dataset['대여소번호']) |
                                                        bikeRentalReturn_data_2309['반납대여소번호'].isin(YDP_station_dataset['대여소번호'])]
bikeRentalReturn_data_2309.replace({'대여대여소번호': {'\\N': 0}, '반납대여소번호': {'\\N': 0}}, inplace=True)
bikeRentalReturn_data_2309 = bikeRentalReturn_data_2309.astype({'대여대여소번호':int, '반납대여소번호':int})
bikeRentalReturn_data_2309 = bikeRentalReturn_data_2309[(bikeRentalReturn_data_2309['대여대여소번호'] != 0) & (bikeRentalReturn_data_2309['반납대여소번호'] != 0)]

bikeRentalReturn_data_2312 = pd.read_csv('서울특별시 공공자전거 대여이력 정보_2312.csv',
                                    encoding='cp949',
                                    skiprows=1,
                                    na_filter=False,
                                    na_values=['\\N'],
                                    names=['자전거번호', '대여일시', '대여대여소번호', '대여대여소명', '대여거치대', '반납일시', '반납대여소번호', '반납대여소명', '반납거치대', '이용시간', '이용거리', '생년', '성별', '이용자종류', '대여대여소ID', '반납대여소ID', '자전거종류'],
                                    usecols=['대여대여소번호', '대여일시', '반납대여소번호', '반납일시'],
                                    #na_filter=False
                                    )
# 영등포 내에서 반납|대여한 데이터만 추출, 대여소번호가 \N인 데이터 삭제
bikeRentalReturn_data_2312 = bikeRentalReturn_data_2312[bikeRentalReturn_data_2312['대여대여소번호'].isin(YDP_station_dataset['대여소번호']) |
                                                        bikeRentalReturn_data_2312['반납대여소번호'].isin(YDP_station_dataset['대여소번호'])]
bikeRentalReturn_data_2312.replace({'대여대여소번호': {'\\N': 0}, '반납대여소번호': {'\\N': 0}}, inplace=True)
bikeRentalReturn_data_2312 = bikeRentalReturn_data_2312.astype({'대여대여소번호':int, '반납대여소번호':int})
bikeRentalReturn_data_2312 = bikeRentalReturn_data_2312[(bikeRentalReturn_data_2312['대여대여소번호'] != 0) & (bikeRentalReturn_data_2312['반납대여소번호'] != 0)]

# 4개월 데이터 합치기
YDP_RentalReturn_data_23 = pd.concat([bikeRentalReturn_data_2303, bikeRentalReturn_data_2306, bikeRentalReturn_data_2309, bikeRentalReturn_data_2312], ignore_index=True) # 결측치 없음, (1304921, 4)

# 대여/반납일시를 대여/반납일자와 대여/반납시간대로 나누기(일자는 string, 시간대는 int로 변환)
YDP_RentalReturn_data_23['대여일자'] = YDP_RentalReturn_data_23['대여일시'].str.split(' ').str[0]
YDP_RentalReturn_data_23['대여시간대'] = YDP_RentalReturn_data_23['대여일시'].str.split(' ').str[1].str.split(':').str[0].astype(int)
YDP_RentalReturn_data_23['반납일자'] = YDP_RentalReturn_data_23['반납일시'].str.split(' ').str[0]
YDP_RentalReturn_data_23['반납시간대'] = YDP_RentalReturn_data_23['반납일시'].str.split(' ').str[1].str.split(':').str[0].astype(int)
YDP_RentalReturn_data_23.drop(columns=['대여일시', '반납일시'], inplace=True)
YDP_RentalReturn_data_23.reset_index(drop=True, inplace=True)

# 영등포 내 대여소별 대여/반납 데이터 저장(대여대여소번호, 반납대여소번호, 대여일자, 대여시간대, 반납일자, 반납시간대), (1304921, 6)
os.chdir(newDataset_path)
YDP_RentalReturn_data_23.to_csv('YDP_station_rental_return_2023.csv', encoding='cp949', index=False)

# 대여대여소번호와 대여시간대 기준으로 대여건수 계산
YDPstation_Rental_data = YDP_RentalReturn_data_23.groupby(['대여대여소번호', '대여시간대']).size().reset_index(name='대여건수')
YDPstation_Rental_data.reset_index(drop=True, inplace=True)

# 반납대여소번호와 반납시간대 기준으로 반납건수 계산
YDPstation_Return_data = YDP_RentalReturn_data_23.groupby(['반납대여소번호', '반납시간대']).size().reset_index(name='반납건수')
YDPstation_Return_data.reset_index(drop=True, inplace=True)

# 대여소번호 뱔 시간대당 대여건수, 반납건수 정리
YDPstationRentalReturn_data = pd.merge(YDPstation_Rental_data, YDPstation_Return_data, left_on=['대여대여소번호', '대여시간대'], right_on=['반납대여소번호', '반납시간대'], how='outer')

# 반납/대여의 시간대/대여소번호가 없으면 대여/반납 시간대/대여소번호와 똑같이 설정
YDPstationRentalReturn_data['시간대'] = YDPstationRentalReturn_data['반납시간대'].fillna(YDPstationRentalReturn_data['대여시간대'])
YDPstationRentalReturn_data['시간대'] = YDPstationRentalReturn_data['대여시간대'].fillna(YDPstationRentalReturn_data['반납시간대'])
YDPstationRentalReturn_data['대여소번호'] = YDPstationRentalReturn_data['대여대여소번호'].fillna(YDPstationRentalReturn_data['반납대여소번호'])
YDPstationRentalReturn_data['대여소번호'] = YDPstationRentalReturn_data['반납대여소번호'].fillna(YDPstationRentalReturn_data['대여대여소번호'])
YDPstationRentalReturn_data.drop(columns=['대여시간대', '반납시간대', '대여대여소번호', '반납대여소번호'], inplace=True)

# 결측치(반납/대여 중 한쪽에만 있는 경우) 0으로 채우기
YDPstationRentalReturn_data['대여건수'] = YDPstationRentalReturn_data['대여건수'].fillna(0)
YDPstationRentalReturn_data['반납건수'] = YDPstationRentalReturn_data['반납건수'].fillna(0)
YDPstationRentalReturn_data['대여반납비율']=(YDPstationRentalReturn_data['대여건수']+1)/(YDPstationRentalReturn_data['반납건수']+1) # 대여반납비율 계산, 분모가 0이 되는 것을 방지하기 위해 1을 더함(1보다 큰 경우 대여가 더 많은 것)
YDPstationRentalReturn_data=YDPstationRentalReturn_data[['대여소번호', '시간대', '대여건수', '반납건수', '대여반납비율']]
YDPstationRentalReturn_data.astype({'대여소번호':int, '대여건수':int, '반납건수':int, '대여반납비율':float})

# 대여소-시간대별 대여/반납건수 및 대여반납비율 데이터 저장, (159*24, 5)=(22285, 5)
YDPstationRentalReturn_data.to_csv('YDP_station_rental_return_dataset.csv', encoding='cp949', index=False)
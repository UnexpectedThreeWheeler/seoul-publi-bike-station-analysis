# 기상청 5분단위 날씨 데이터 활용
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
    
# read temporature csv file
temporature_2303 = pd.read_csv('SYNOP_AWOS_1209_MI_2023-03_2023-03_2023.csv',
                           encoding='cp949',
                           usecols=['일시', '기온(℃)']
                           )

temporature_2306 = pd.read_csv('SYNOP_AWOS_1209_MI_2023-06_2023-06_2023.csv',
                           encoding='cp949',
                           usecols=['일시', '기온(℃)']
                           )

temporature_2309 = pd.read_csv('SYNOP_AWOS_1209_MI_2023-09_2023-09_2023.csv',
                           encoding='cp949',
                           usecols=['일시', '기온(℃)']
                           )

temporature_2312 = pd.read_csv('SYNOP_AWOS_1209_MI_2023-12_2023-12_2023.csv',
                           encoding='cp949',
                           usecols=['일시', '기온(℃)']
                           )

# 4개월 데이터 합치기
temporature_23 = pd.concat([temporature_2303, temporature_2306, temporature_2309, temporature_2312])
temporature_23=temporature_23.reset_index(drop=True)

# 데이터 전처리
temporature_23=temporature_23.rename(columns={'기온(℃)':'기온(°C)'}) # 컬럼명 변경
temporature_23['시간대']=temporature_23['일시'].str.split(' ').str[1].str.split(':').str[0].astype(int) # 데이터 컬럼 분할(날짜, 시간대)
temporature_23['일시']=temporature_23['일시'].str.split(' ').str[0]

# 데이터 온도가 5분단위 측정 기록이므로 일시, 시간당 평균값으로 변경
temporature_23=temporature_23.groupby(['일시', '시간대']).mean().reset_index()
temporature_23['기온(°C)']=temporature_23['기온(°C)'].fillna(method='ffill') # 기온 결측치 앞 값으로 채우기(기온만 결측치 존재)
temporature_23=temporature_23[['일시', '시간대', '기온(°C)']] # 컬럼 순서 변경

# read percipitation csv file
percipitation_2303 = pd.read_csv('서울(108) 강수량분석 일 자료_2303.csv', 
                            encoding='cp949',
                            usecols=['일시', '강수량(mm)']
                            )

percipitation_2306 = pd.read_csv('서울(108) 강수량분석 일 자료_2306.csv', 
                            encoding='cp949',
                            usecols=['일시', '강수량(mm)']
                            )

percipitation_2309 = pd.read_csv('서울(108) 강수량분석 일 자료_2309.csv', 
                            encoding='cp949',
                            usecols=['일시', '강수량(mm)']
                            )

percipitation_2312 = pd.read_csv('서울(108) 강수량분석 일 자료_2312.csv', 
                            encoding='cp949',
                            usecols=['일시', '강수량(mm)']
                            )

# 4개월 데이터 합치기
# 강수량 없는 경우 nan으로 표시됨
percipitation_23 = pd.concat([percipitation_2303, percipitation_2306, percipitation_2309, percipitation_2312])
percipitation_23=percipitation_23.reset_index(drop=True)

# 데이터 전처리
percipitation_23=percipitation_23.rename(columns={'강수량(mm)':'일 강수량'})
percipitation_23.fillna(0, inplace=True) # 강수량 결측치 0으로 채우기

# 두 데이터 일시를 기준으로 merge
weather_23 = pd.merge(temporature_23, percipitation_23, on='일시', how='left')
weather_23.fillna(0, inplace=True) # 결측치 0으로 채우기(04-01 00시, 10-01 00시 일 강수량이 없음)

# 데이터 저장
os.chdir(newDataset_path)
weather_23.to_csv('YDP_weather_dataset_2023.csv', encoding='cp949', index=False) # 시간대별 기온 + 일평균 강수량 데이터 저장
print(weather_23.head)
# 2024 Data science team 5   
# Analyze 따릉이 usage patterns and predict crowded rentals.       

##### We are Gachon Univ. students.
##### This project is for 2024 Data Science project.
##### Since 2024/03 ~

### Team Member
<table>
  <tbody>
    <tr>
      <td align="center"><img src="https://github.com/ExhaustedApes/coffee-maker/assets/118164288/88c77023-535a-48ab-b958-9c585ebdaaa9.png" width="100px;" alt=""/></td>
      <td align="center"><img src="https://github.com/ExhaustedApes/coffee-maker/assets/118164288/714f4fa4-1d3c-433a-8e62-fbe5f86d30a0.png" width="100px;" alt=""/></td>
      <td align="center"><img src="https://github.com/ExhaustedApes/coffee-maker/assets/118164288/e72dd819-6a77-43af-8397-435b6b6ff01d.png" width="100px;" alt=""/></td>
      <td align="center"><a href="https://github.com/KingHamster"><sub><b>KingHamster</b></sub></a></td>
      <td align="center"><a href="https://github.com/"><sub><b>member1</b></sub></a></td>
      <td align="center"><a href="https://github.com/"><sub><b>member2</b></sub></a></td>
    </tr>
  </tbody>
</table>

- 202135846 최지예   
- 202235082 이민서   
- 202235873 유도연   

## Dataset used   
Data from March, June, June, and December 2023 from 서울 열린데이터광장, 기상청 기상자료개방포털      
- 서울특별시 공공자전거 이용정보(시간대별)   
- 서울특별시 공공자전거 대여이력 정보   
- 공공자전거 대여소 정보   
- SYNOP_AWOS_1209_MI(temperature)   
- 서울(108) 강수량분석 일 자료   

## 1. Data preprocessing   
### **bikeRenstalData_init.py**   
Preprocesses public bicycle usage data by time zone in Seoul   

### **bikeStationData_init.py**   
Extract rental station numbers located in Yeongdeungpo-gu from Seoul's public bicycle rental station information      

### **weatherData_init.py**   
Get Seoul temperature and precipitation data       

### **stationPropertyData_init.py**   
Extract the number of rentals and returns      

### **addSationPropertyToRentalData.py**   
Merge rental station properties with rental history information in Yeongdeungpo       

## 2. Data Modeling and evaluation   
### **station_kMeans.py**   
Perform KMeans clustering by number of rentals, number of returns, and rental-return ratio to divide into 3 clusters      

### **station_SVM.py**   
Evaluate KMeans clustering results using soft vector machine   

### Feature and target value   
X=data[['대여소번호', '대여월', '대여시간대', '일 강수량', '기온(°C)']]   
y = data['cluster']   

### **DecisionTree.py**      
Modeling and evaluation using a decision tree classifier.      

### **RandomForest.py**   
Modeling and evaluation using a random forest classifier.        

### **KNN.py**   
Modeling and evaluation using KNN classifier.    

  
### **GridSearchDT.py**  
Finds the best combination of parameters through a grid search, then runs the decision tree classifier once again and evaluates.      

### **GridSearchRF.py**   
Runs and evaluates a Random forest classifier once again after finding the optimal parameter combination via grid search.   

### **DecisionTreeClassifier_OpenSourceSW.py**   
Functionalizes the process of running and evaluating a grid search and decision tree classifier.   

**RandomForestClassifier_OpenSourceSW.py**    
Functionalizes the process of Dolly over-evaluating grid search and random forest classifier.      

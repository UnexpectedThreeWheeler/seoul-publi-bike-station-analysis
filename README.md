# 2024 Data science team 5   
# Analyze ������ usage patterns and predict crowded rentals.       
- 202135846 ������   
- 202235082 �̹μ�   
- 202235873 ������   

## Dataset used   
Data from March, June, June, and December 2023 from ���� ���������ͱ���, ���û ����ڷᰳ������      
- ����Ư���� ���������� �̿�����(�ð��뺰)   
- ����Ư���� ���������� �뿩�̷� ����   
- ���������� �뿩�� ����   
- SYNOP_AWOS_1209_MI(temperature)   
- ����(108) �������м� �� �ڷ�   

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
X=data[['�뿩�ҹ�ȣ', '�뿩��', '�뿩�ð���', '�� ������', '���(��C)']]   
y = data['cluster']   

### **SVM.py**   
Classifies and evaluates a bike rental dataset using SVM.   
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

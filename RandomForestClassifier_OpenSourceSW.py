import os
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_squared_error, mean_absolute_error
import numpy as np
from math import sqrt

def check_and_change_directory(directory_name):
    current_path = os.getcwd()
    newDataset_path = os.path.join(current_path, directory_name)

    if os.path.exists(newDataset_path):
        os.chdir(newDataset_path)
    else:
        print(f'No directory named "{directory_name}"')
        exit()

def read_and_preprocess_data(file_name):
    data = pd.read_csv(file_name, encoding='cp949')
    data['대여월'] = data['대여일자'].str.split('-').str[1].astype(int)
    data['대여일'] = data['대여일자'].str.split('-').str[2].astype(int)
    return data

def split_and_scale_data(data):
    X = data[['대여소번호', '대여월', '대여시간대', '일 강수량', '기온(°C)']]
    y = data['cluster']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    logging.warning('Train test split done')

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    logging.warning('Standard scaler done')
    
    return X_train_scaled, X_test_scaled, y_train, y_test, X, y

def perform_grid_search(X_train, y_train):
    rf = RandomForestClassifier(random_state=0)
    params = {
        'n_estimators': [100, 300],
        'max_depth': [None, 10, 20]
    }

    grid_cv = GridSearchCV(rf, param_grid=params, cv=2, n_jobs=-1)
    grid_cv.fit(X_train, y_train)
    logging.warning('Grid search done')
    
    return grid_cv.best_estimator_, grid_cv.best_params_, grid_cv.best_score_

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    
    return accuracy, conf_matrix, class_report, rmse, mae

def cross_validate_model(model, X, y):
    scores = cross_val_score(model, X, y, cv=5)
    return scores, np.mean(scores)

def main():
    logging.basicConfig(level=logging.WARNING)

    check_and_change_directory('newDataset')
    data = read_and_preprocess_data('clustered_rental_dataset.csv')
    X_train_scaled, X_test_scaled, y_train, y_test, X, y = split_and_scale_data(data)
    best_model, best_params, best_score = perform_grid_search(X_train_scaled, y_train)

    print('Best hyper parameter:\n', best_params)
    print('Best accuracy:\n', best_score)

    accuracy, conf_matrix, class_report, rmse, mae = evaluate_model(best_model, X_test_scaled, y_test)
    print('Accuracy:', accuracy)
    print('Confusion matrix:\n', conf_matrix)
    print('Classification report:\n', class_report)
    print('RMSE:', rmse)
    print('MAE:', mae)

    scores, mean_score = cross_validate_model(best_model, X, y)
    print('Cross-validation scores:', scores)
    print('Cross-validation mean score:', mean_score)

if __name__ == "__main__":
    main()

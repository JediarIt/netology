# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
import sys
from joblib import dump
from sklearn.metrics import confusion_matrix

def fit_save(train, test):
	columns = [c for c in train.columns if c != 'quality'];
	X_train = train[columns]
	y_train = train['quality']

	X_test = test[columns]
	y_test = test['quality']

	model = RandomForestClassifier(n_estimators=300, max_depth=15, random_state=23)
	model.fit(X_train, y_train)
	model.score

	dump(model, './model.joblib')
	
	y_pred = model.predict(X_test)
	score = model.score(X_test, y_test)
	print(f'Accuracy: {score}')
	print(confusion_matrix(y_test, y_pred))

if __name__ == '__main__':
	train = pd.read_csv(sys.argv[1])
	test = pd.read_csv(sys.argv[2])
	fit_save(train, test)
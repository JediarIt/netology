# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
import sys
from joblib import dump

def fit_save(train, test):
	columns = [c for c in train.columns if c != 'quality'];
	X_train = train[columns]
	y_train = train['quality']

	X_test = test[columns]
	y_test = test['quality']

	model = RandomForestClassifier(n_estimators=300, max_depth=15, random_state=23)
	model.fit(X_train, y_train)

	dump(model, './model.joblib')

if __name__ == '__main__':
	train = pd.read_csv(sys.argv[1])
	test = pd.read_csv(sys.argv[2])
	fit_save(train, test)
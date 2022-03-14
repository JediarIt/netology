# -*- coding: utf-8 -*-
import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope

from sklearn.model_selection import StratifiedShuffleSplit
from imblearn.over_sampling import RandomOverSampler

import sys

def process(data, save=False):
	## Удаляем пропуски

	data = data.dropna()

	##Кодирование категориальных перменных

	data = pd.get_dummies(data, columns=['type'])

	##Работа с выбросами

	data['lof'] = LocalOutlierFactor().fit_predict(data)
	data['isol'] = IsolationForest().fit_predict(data)
	data['env'] = EllipticEnvelope().fit_predict(data)
	data['svm'] = OneClassSVM().fit_predict(data)
	data['anomaly'] = data['lof'] + data['isol'] + data['env'] + data['svm']

	data[data['anomaly'] == -4]

	data = data[data['anomaly'] != -4]
	data = data.drop(columns=['anomaly', 'lof', 'isol', 'env', 'svm'])


	##На основе свободных диокидов серы и общего количества можем осздать признак процентного содержания свободных диокисдов серы
	data['free sulfur dioxide, %'] = data['free sulfur dioxide'] / data['total sulfur dioxide']
	data = data.drop(columns=['free sulfur dioxide', 'total sulfur dioxide'])

	##Удаление типа вина

	data = data.drop(columns=['type_red', 'type_white'])

	##train/test split

	columns = [c for c in data.columns if c != 'quality'];
	X = data[columns]
	y = data['quality']

	sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2)
	for trn_idx, tst_idx in sss.split(X, y):
	  train = data.iloc[trn_idx]
	  test = data.iloc[tst_idx]

	if save:
		train.to_csv('./train.csv')
		test.to_csv('./test.csv')
		
	return train, test

if __name__ == '__main__':
	data = pd.read_csv(sys.argv[1])
	process(data, True)
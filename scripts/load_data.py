import pandas as pd
import sys

def load(path=None):
	data = pd.read_csv('https://storage.googleapis.com/kagglesdsdata/datasets/35901/52633/winequalityN.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220314%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220314T070716Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=62f885d47c24b727f233076030ee011c93d7aa6f7d1ea3606ff57a2ab27b0d223f4cf344c6a0d7b584cb17e56daf5a788fead3b7ce5c1c5c41f08c9e52ed57729ba51e81ab501456ce2b3fb5c2608231aa53044e30d37f58b45fc0dcb16b517ec2c4c8c0bdc14db9291d57be6b68290b3925bc3ba9c7977e463dd1a5bb6a8a96b5c330f2bab79c6941ca87a8d69c19b3fb9c1bb840377c8a34287034ed584808265b76d81c6b00a512448c34ff5f0913e9142803d0e972c3440cb483444116eaec288b3a117fde171bdc4fc1beaaef2052301c8cae668b3098aaa66fa4554210d2c0f716bdd6bd8c42412d513a93ad77b0c10c8bfbbf41aff08edcd9b5fd5be4')
	if path is not None:
		data.to_csv(path)
	
	return data

if __name__ == '__main__':
    load_data(sys.argv[1])
import load_data
import kvg_preprocessing_1_0 as proc
import kvg_fit_1_0 as fit

data = load_data.load()
train, test = proc.process(data)
fit.fit_save(train, test)
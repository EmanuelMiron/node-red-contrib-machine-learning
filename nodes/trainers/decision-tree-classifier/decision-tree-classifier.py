import json
import pickle
import pandas
from sklearn.tree import DecisionTreeClassifier
import os
import sys

try:
	config = os.path.split(os.path.abspath(__file__))[0] + "\\config.json"
except:
	print('Cannot load config file.', end='')
	sys.exit()

try:
	dataset = json.load(open(config, 'r'))
except:
	print('Cannot load dataset file.', end='')
	sys.exit()

try:
	df = pandas.read_csv(dataset['path'], header=None)

	r, c = df.shape

	x = df.iloc[: r * dataset['amount'], dataset['input']]
	y = df.iloc[: r * dataset['amount'], dataset['output']]

	dtc = DecisionTreeClassifier(max_depth=dataset['depth'])
	dtc.fit(x, y)

	pickle.dump(dtc, open(dataset['save'], "wb"));
except:
	print('Cannot complete training.', end='')
	sys.exit()

print('Training completed.', end='')
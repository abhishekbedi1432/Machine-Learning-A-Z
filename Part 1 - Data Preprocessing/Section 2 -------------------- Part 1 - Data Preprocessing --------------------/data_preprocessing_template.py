# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #Library to import datasets

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values # country,age,salary
#X1 = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values # purchased

#Taking care of missing data NAN stuff
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

 # We are fitting the corrected data to X for all rows and 
# columns starting from 1 to 3 (3 is excluded hence we 1:3)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


#Categorical data Section 2 Lecture 13
# LabelEncoder actually encodes the countries to numerals like 0,1,2
# but that should not mean the 2 > 1 > 0, these are just numeral representation of categories
# so now we user <OneHotEncoder> to split the categories of these 3 countries in 3 different columns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Now we represent column <Purchased> which has YES and NO to binary 0 and 1
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
# One liner
y = LabelEncoder().fit_transform(y)

#You can apply both transformations (from text categories to integer categories, 
#then from integer categories to one-hot vectors) in one shot using the LabelBinarizer class:
from sklearn.preprocessing import LabelBinarizer
cat_features = ['color', 'director_name', 'actor_2_name']
encoder = LabelBinarizer()
new_cat_features = encoder.fit_transform(cat_features)
new_cat_features




# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)
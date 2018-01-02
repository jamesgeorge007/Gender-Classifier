from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

tree_classifier = DecisionTreeClassifier()

neighbor_classifier = KNeighborsClassifier()

discriminant_classifier = QuadraticDiscriminantAnalysis()

# Data-sets

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# Training the model with datasets.

tree_model = tree_classifier.fit(X, Y)

neighbor_model = neighbor_classifier.fit(X, Y)

discriminant_model = discriminant_classifier.fit(X, Y)

# Predicting based on the given input. 

tree_prediction = tree_model.predict([[190, 70, 43]])

neighbor_prediction = neighbor_model.predict([[190, 70, 43]])

discriminant_prediction = discriminant_model.predict([[190, 70, 43]]) 

print(tree_prediction)

print(neighbor_prediction)

print(discriminant_prediction)


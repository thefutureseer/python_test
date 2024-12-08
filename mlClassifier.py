# Importing the Iris dataset, 
# a standard dataset provided 
# by scikit-learn for classification problems.
from sklearn.datasets import load_iris

# Importing the function to split 
# data into training and testing sets.
# This helps evaluate the model's 
# performance on unseen data.
from sklearn.model_selection import train_test_split

# Importing the Random Forest 
# Classifier, an ensemble learning 
# method that builds multiple decision trees.
# It combines their outputs for 
# better accuracy and robustness.
from sklearn.ensemble import RandomForestClassifier

# Importing a metric to evaluate 
# the accuracy of predictions made 
# by the model. Accuracy is calculated 
# as the proportion of correct predictions 
# out of the total predictions.
from sklearn.metrics import accuracy_score

# Load the Iris dataset, which 
# contains measurements of iris 
# flowers along with their species labels.
iris = load_iris()
X, y = iris.data, iris.target  # Splitting the dataset into features (X) and labels (y).

# Split the data into training and testing sets.
# `test_size=0.3` means 30% of the 
# data will be used for testing, 
# while the remaining 70% is for training.
# `random_state=42` ensures reproducibility 
# by controlling the randomness of the split.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize a Random Forest Classifier.
model = RandomForestClassifier()  # Default parameters are used here.

# Train the model using the training data.
# The `fit` method allows the model to 
# learn the relationship between 
# features (X_train) and labels (y_train).
model.fit(X_train, y_train)

# Use the trained model to predict 
# the labels for the testing data.
y_pred = model.predict(X_test)

# Evaluate the model's performance 
# using accuracy as the metric.
# `accuracy_score` compares the 
# predicted labels (y_pred) with the true labels (y_test).
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy percentage of the model.
print(f"Model Accuracy: {accuracy * 100:.2f}%")
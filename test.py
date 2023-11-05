Recursive Feature Elimination - Example

Step 1: Import Libraries and Load the Dataset First, you need to import the necessary libraries and load the diabetes dataset.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

Step 2: Split the Dataset Split the dataset into training and testing sets to evaluate the model later.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

Step 3: Create a Linear Regression Model Create a linear regression model that will be used for feature selection.
model = LinearRegression()

Step 4: Initialize RFE with the Model and Desired Number of Features Initialize RFE with the linear regression model and specify the number of features you want to select.
num_features_to_select = 5  # You can change this to the desired number of features
rfe = RFE(model, num_features_to_select)

Step 5: Fit RFE to the Training Data Fit RFE to the training data to perform feature selection.
rfe.fit(X_train, y_train)

Step 6: Get the Selected Features Retrieve the indices of the selected features using rfe.support_.
selected_features = np.where(rfe.support_)[0]
print("Selected Feature Indices:", selected_features)

Step 7: Train a Model Using the Selected Features Train a linear regression model using the selected features.
X_train_selected = X_train[:, selected_features]
X_test_selected = X_test[:, selected_features]

model.fit(X_train_selected, y_train)

Step 8: Make Predictions and Evaluate the Model Make predictions on the test set and calculate the mean squared error to evaluate the model's performance.
y_pred = model.predict(X_test_selected)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Initialize and Train the Lasso Regression Model Create a <Lasso Regression model>, and specify the strength of the regularization penalty, typically denoted as alpha. 
Larger alpha values lead to stronger regularization, which results in more feature selection. You can use techniques like cross-validation to choose an appropriate alpha value.

alpha = 0.01  # Adjust the value of alpha based on your data and requirements
lasso_model = Lasso(alpha=alpha)
lasso_model.fit(X_train, y_train)

selected_features = X.columns[lasso_model.coef_ != 0]

Random Forest

Train a Random Forest Model Create and train a Random Forest classifier using your training data.
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)
Feature Importance Calculation Retrieve the feature importances from the trained Random Forest model.
feature_importances = rf_classifier.feature_importances_

Rank Features Rank the features based on their importance scores, in descending order. You can use this ranking to select the top features for your model.
feature_ranking = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances}) 
feature_ranking = feature_ranking.sort_values(by='Importance', ascending=False)

Select Top Features Choose the top N features based on your requirements. You can select a fixed number of features or use a threshold on the importance score.
top_n_features = feature_ranking.head(N)  # Replace N with the desired number of features
selected_features = top_n_features['Feature'].tolist()

Train and Evaluate the Model with Selected Features Train a Random Forest model using only the selected features and evaluate its performance.
X_train_selected = X_train[selected_features]
X_test_selected = X_test[selected_features]

rf_classifier.fit(X_train_selected, y_train)
y_pred = rf_classifier.predict(X_test_selected)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy with Selected Features:", accuracy)




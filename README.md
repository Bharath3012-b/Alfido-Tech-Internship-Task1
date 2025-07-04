Name: BHARATH BABU
Company: Alfido-Tech
ID:  BS/REG/105850
Domain: Machine Learning 


Project Overview: Iris Flower Classification
Objective:
The main goal of this project is to build a machine learning model that can classify iris flowers into one of three species — Setosa, Versicolor, or Virginica — based on their sepal length, sepal width, petal length, and petal width.

This is a classic beginner-friendly ML problem that helps in understanding:

Data preprocessing

Exploratory data analysis (EDA)

Feature selection

Model training and evaluation using supervised learning

Key Activities:
Data Loading

Used Pandas to load the Iris dataset from a CSV file.

Exploratory Data Analysis (EDA)

Plotted histograms using Matplotlib and Seaborn to understand feature distributions.

Verified that there are 3 unique species in the dataset.

Data Preparation

Extracted feature columns (sepal_length, sepal_width, petal_length, petal_width) and the target (species).

Split the dataset into training and testing sets using train_test_split.

Model Building

Built a Decision Tree Classifier using Scikit-learn.

Trained the model on the training set.

Model Evaluation

Predicted results on the test set.

Evaluated using accuracy score, classification report, and confusion matrix.

Plotted the confusion matrix using Seaborn.

Modules Used:
Module/Library	Purpose
Pandas	Data loading and manipulation
NumPy	Numerical computations and array support
Matplotlib	Plotting feature distributions and confusion matrix
Seaborn	Enhanced visualization of histograms and confusion matrix
Scikit-learn	Model training (DecisionTreeClassifier), evaluation, data splitting

Main Components (Modules of Code):
Data Input Module – Loads and verifies the dataset.

Visualization Module – Plots histograms of features.

Preprocessing Module – Prepares input (X) and output (y) variables.

Modeling Module – Trains a decision tree model.

Evaluation Module – Outputs accuracy, classification report, and confusion matrix.


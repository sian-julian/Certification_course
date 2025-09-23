import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# --- 1. Load the Dataset ---
# Load the data from the CSV file into a pandas DataFrame
try:
    df = pd.read_csv('Student Mental Health Analysis\student_depression_dataset.csv')
except FileNotFoundError:
    print("Error: 'student_depression_dataset.csv' not found.")
    print("Please make sure the dataset file is in the same directory as the script.")
    exit()

# --- 2. Data Cleaning and Preprocessing ---

# Drop the 'id' column as it is not a useful feature for prediction
df = df.drop('id', axis=1)

# Identify categorical and numerical columns
categorical_cols = df.select_dtypes(include=['object']).columns
numerical_cols = df.select_dtypes(include=np.number).columns

# Handle missing values in numerical columns by filling them with the mean
for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mean(), inplace=True)

# Convert categorical columns to numerical using Label Encoding
# This is necessary for the machine learning model to process the data
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

print("Data preprocessing complete. Categorical features have been encoded.")

# --- 3. Feature Selection and Data Splitting ---

# Define the features (X) and the target variable (y)
X = df.drop('Depression', axis=1)
y = df['Depression']

# Split the data into training (80%) and testing (20%) sets
# The random_state ensures that the split is the same every time the code is run
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Data split into {len(X_train)} training samples and {len(X_test)} testing samples.")

# --- 4. Model Training ---

# Initialize the GradientBoostingClassifier for higher accuracy
# n_estimators: Number of boosting stages to be run.
# learning_rate: Shrinks the contribution of each tree.
# max_depth: Maximum depth of the individual regression estimators.
model = GradientBoostingClassifier(n_estimators=300, learning_rate=0.1, max_depth=5, random_state=42, subsample=0.8)

print("\nTraining the Gradient Boosting model...")
# Train the model on the training data
model.fit(X_train, y_train)
print("Model training complete.")

# --- 5. Model Evaluation ---

print("\nEvaluating the model on the test set...")
# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Display a detailed classification report
print('\nClassification Report:')
print(classification_report(y_test, y_pred))

# Display the confusion matrix
print('\nConfusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# --- 6. Feature Importance ---
# This shows which features were most influential in the model's predictions
print("\nTop 10 Most Important Features:")
feature_importances = pd.DataFrame(model.feature_importances_,
                                   index = X_train.columns,
                                   columns=['importance']).sort_values('importance', ascending=False)
print(feature_importances.head(10))


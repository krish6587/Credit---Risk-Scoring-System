import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def generate_synthetic_data(num_samples=1000):
    np.random.seed(42)
    # Features: Age, Income, Loan Amount, Credit Score, Employment Length
    age = np.random.randint(18, 70, size=num_samples)
    income = np.random.randint(20000, 150000, size=num_samples)
    loan_amount = np.random.randint(1000, 50000, size=num_samples)
    credit_score = np.random.randint(300, 850, size=num_samples)
    employment_length = np.random.randint(0, 40, size=num_samples)
    
    # Target: 0 = Default, 1 = Paid
    # A simple logic: High income + high credit score -> likely to pay
    score = (income / 10000) + (credit_score / 100) - (loan_amount / 5000) + employment_length
    # Add some noise
    score += np.random.normal(0, 5, size=num_samples)
    
    # Threshold for approval
    threshold = np.median(score)
    target = (score > threshold).astype(int)
    
    df = pd.DataFrame({
        'age': age,
        'income': income,
        'loan_amount': loan_amount,
        'credit_score': credit_score,
        'employment_length': employment_length,
        'target': target
    })
    return df

def train_model():
    print("Generating synthetic dataset...")
    df = generate_synthetic_data(1500)
    
    X = df.drop('target', axis=1)
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("Classification Report:")
    print(classification_report(y_test, predictions))
    
    # Save the model
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()

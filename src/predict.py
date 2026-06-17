import os
import pickle
import pandas as pd

class CreditRiskModel:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
        if os.path.exists(model_path):
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
        else:
            print(f"Warning: Model not found at {model_path}. Please train the model first.")

    def predict(self, data: dict):
        if not self.model:
            raise Exception("Model is not loaded.")
        
        # Convert dictionary to DataFrame
        df = pd.DataFrame([data])
        
        # Ensure column order matches training
        # Features: Age, Income, Loan Amount, Credit Score, Employment Length
        features = ['age', 'income', 'loan_amount', 'credit_score', 'employment_length']
        df = df[features]
        
        prediction = self.model.predict(df)[0]
        probability = self.model.predict_proba(df)[0].max()
        
        return {
            "prediction": int(prediction),
            "status": "Approved" if prediction == 1 else "Rejected",
            "confidence": float(probability)
        }

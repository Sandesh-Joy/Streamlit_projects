from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

X, y = load_iris(return_X_y=True)
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X, y)
joblib.dump(model, "iris_model.joblib")
print("Iris model saved to iris_model.joblib")

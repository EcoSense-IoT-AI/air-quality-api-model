# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Re-création du dataset
np.random.seed(42)
rows = []
for i in range(100):
    target = 0 if i < 50 else 1
    if target == 0:
        co2 = np.random.randint(380, 800)
        pm25 = np.random.randint(5, 25)
        temp = np.random.randint(18, 24)
        hum = np.random.randint(35, 50)
    else:
        co2 = np.random.randint(1000, 2500)
        pm25 = np.random.randint(35, 120)
        temp = np.random.randint(24, 35)
        hum = np.random.randint(55, 80)
    rows.append([co2, pm25, temp, hum, target])

df = pd.DataFrame(rows, columns=['co2', 'pm25', 'temp', 'hum', 'target'])

# Séparer les features et la target
X = df[['co2', 'pm25', 'temp', 'hum']]
y = df['target']

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Sauvegarder le modèle
joblib.dump(model, "model_air_quality.joblib")
print("Modèle entraîné et sauvegardé ✅")

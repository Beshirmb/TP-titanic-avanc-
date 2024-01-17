 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
 
# Chargement de données
 
 
df = pd.read_csv ('train.csv')
 
 
 
 
# Séparation des caractéristiques et de la cible
X = df.drop("Survived", axis=1)
y = df["Survived"]
 
# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 
 
# Création du pipeline de classification
rf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', RandomForestClassifier())])
 
# Entraînement du modèle
rf.fit(X_train, y_train)
 
# Prédiction sur l'ensemble de test
df = pd.read_csv ('test.csv')
y_pred = rf.predict(X_test)
 
# Calcul de la précision
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle: ", accuracy)
import pandas as pd
import numpy as np
from sklearn.svm import SVC
import lightgbm as lgb
import xgboost as xgb
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_selector
from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
import joblib
from components.titanic import X, y
from sklearn.model_selection import train_test_split

# Creation de pipeline

# Choix des colonnes
numerical_features = make_column_selector(dtype_include=np.number)
categorical_features = make_column_selector(dtype_exclude=np.number)

# Choix des transformations
numerical_pipelines = make_pipeline(SimpleImputer(), StandardScaler())
categorical_pipelines = make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder())

# Assemblage des deux
preprocessor = make_column_transformer((numerical_pipelines, numerical_features), (categorical_pipelines, categorical_features))

filename = "ML/preprocessor.joblib"
joblib.dump(preprocessor, filename)

# Application des pipelines au dataframe
df_titanic_clean = pd.DataFrame(preprocessor.fit_transform(X))

df_titanic_clean.to_csv("data/titanic_clean.csv", index=False)

print(df_titanic_clean)

X_train, X_test, y_train, y_test = train_test_split(df_titanic_clean, y, test_size=0.2, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

param_grid_model = { 
    GradientBoostingClassifier : {'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.1, 0.005],
    'max_depth': [3, 5, 8]},
    lgb.LGBMClassifier : {'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.1, 0.005],
    'max_depth': [3, 5, 8]},
    xgb.XGBClassifier : { 'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.1, 0.005],
    'max_depth': [3, 5, 8]},
    LogisticRegression : {'max_iter' : [50, 100 , 200 , 500],
    'solver' : ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']},
    SVC : {'kernel' : ['linear', 'poly','rbf', 'sigmoid']},
    Perceptron : {'max_iter' : [100, 200, 500, 1000],
    'eta0' : [0.5, 1, 1.5]}
}
param_grid_model = { 
    GradientBoostingClassifier : {'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.1, 0.005],
    'max_depth': [3, 5, 8]},
    lgb.LGBMClassifier : {'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.1, 0.005],
    'max_depth': [3, 5, 8]},
    xgb.XGBClassifier : { 'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.1, 0.005],
    'max_depth': [3, 5, 8]},
    LogisticRegression : {'max_iter' : [50, 100 , 200 , 500],
    'solver' : ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']},
    SVC : {'kernel' : ['linear', 'poly','rbf', 'sigmoid']},
    Perceptron : {'max_iter' : [100, 200, 500, 1000],
    'eta0' : [0.5, 1, 1.5]}
}
models = {"GradientBoostingClassifier" : GradientBoostingClassifier,
          "LGBMClassifier" : lgb.LGBMClassifier,
          "XGBClassifier" : xgb.XGBClassifier,
          "LogisticRegression" : LogisticRegression,
          "SVC" : SVC,
          "Perceptron" : Perceptron}

# Testons le modèle et mettons le en fonction
def test_model(X_train, X_test, y_train, y_test, models, param_grids):
  metrics = {}
  for nom, model in models.items():
  # Crééons un grid search cv
    grid_search = GridSearchCV(model(), param_grid=param_grids[model], cv=5, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)
    # Meilleurs hyperparamètres trouvés
    best_params = grid_search.best_params_
    best_model = model(**best_params)
    best_model.fit(X_train, y_train)
    filename = f"ML/{nom}.joblib"
    joblib.dump(best_model, filename)
    y_pred = best_model.predict(X_test)
    # Plot the classification report
    classification_report_dict = classification_report(y_test, y_pred, output_dict=True)
    class_metrics = {}
    # Loop through classification report dictionnary items
    for k, v in classification_report_dict.items():
      if k == "accuracy": # stop once we get to accuracy key
        class_metrics["accuracy"] = v
        break
      else:
        # Ajout des noms et des scores
        class_metrics["precision"] = v["precision"]
        class_metrics["recall"] = v["recall"]
        class_metrics["f1-score"] = v["f1-score"]
    metrics[nom] = class_metrics
  metrics = pd.DataFrame.from_dict(metrics, orient='index')
  return metrics.style.highlight_max(color="red")
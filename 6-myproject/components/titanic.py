# Commençons par faire les imports nécessaire
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Récupérer les données
df_titanic = pd.read_csv('data/titanic.csv')
print(df_titanic.head())

# Exploration des données
print(df_titanic.info())

# Affichons les survivants 
survived = df_titanic['Survived'].value_counts()
stat_survive = {}
stat_survive["non_survived"] = survived[0] / (survived[0] + survived[1])
stat_survive["survived"] = survived[1] / (survived[0] + survived[1])

# Faisons deux classes hommes et femmes

df_titanic_hommes = df_titanic[df_titanic.Sex == 'male']

# Faisons une fonction
def stat_survive(categorie = "Age", sexe = None):
    if sexe == "female":
        df_titanic_femmes = df_titanic[df_titanic.Sex == 'female']
        age_survived = pd.crosstab(df_titanic_femmes.Age, df_titanic.Survived)
        age_survived.columns = ["non_survived", "survived"]
        stat_survive = {}
        for i in range(10, 71, 10):
            stat_survive[f"Personne entre {i -10} et {i} ans"] = age_survived[(age_survived.index <= i) & (age_survived.index > i - 10)]["survived"].sum() / (age_survived[(age_survived.index <= i) & (age_survived.index > i - 10)]['survived'].sum() + age_survived[(age_survived.index <= i) & (age_survived.index > i - 10)]['non_survived'].sum())
    elif sexe == "male":
        # Maintenant pour les hommes
        age_survived = pd.crosstab(df_titanic_hommes.Age, df_titanic.Survived)
        age_survived.columns = ["non_survived", "survived"]
        stat_survive = {}
        for i in range(10, 81, 10):
            stat_survive[f"Personne entre {i -10} et {i} ans"] = age_survived[(age_survived.index <= i) & (age_survived.index > i - 10)]["survived"].sum() / (age_survived[(age_survived.index <= i) & (age_survived.index > i - 10)]['survived'].sum() + age_survived[(age_survived.index <= i) & (age_survived.index > i - 10)]['non_survived'].sum())
    else:
        survived = pd.crosstab(df_titanic.categorie, df_titanic.Survived)
        survived.columns = ["non_survived", "survived"]
        stat_survive = {}
        if categorie == "age":
            for i in range(10, 81, 10):
                stat_survive[f"Personne entre {i -10} et {i} ans"] = survived[(survived.index <= i) & (survived.index > i - 10)]["survived"].sum() / (survived[(survived.index <= i) & (survived.index > i - 10)]['survived'].sum() + survived[(survived.index <= i) & (survived.index > i - 10)]['non_survived'].sum())
        elif categorie == "sexe":
            for i in range(0, 2):
                stat_survive[survived.index[i]] = survived[survived.index == survived.index[i]]["survived"].sum() / (survived[survived.index == survived.index[i]]["survived"].sum() + survived[survived.index == survived.index[i]]['non_survived'].sum())
        elif categorie == "Pclass":
            for i in range(3):
                stat_survive[survived.index[i]] = survived[survived.index == i + 1]["survived"].sum() / (survived[survived.index == i + 1]["survived"].sum() + survived[survived.index == i + 1]['non_survived'].sum())
    return stat_survive
# ============================================================================== Nettoyage des données ===============================================================================================================================================

# Supprimons la colonne cabin avec peu de données
df_titanic_sans_null =  df_titanic.drop("Cabin", axis=1)

# Supprimons les colonnes inutiles
df_titanic_sans_null = df_titanic_sans_null.drop(["PassengerId", "Name", "Ticket"], axis=1)
df_titanic_sans_null

# Découpons le dataframe en features et target
X = df_titanic_sans_null.drop("Survived", axis=1)
y = df_titanic_sans_null.Survived









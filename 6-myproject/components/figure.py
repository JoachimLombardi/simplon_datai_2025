import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from components.titanic import stat_survive

def figure(stat_survive, categorie = "Age", sexe = None):
        plt.figure(1)
        fig, ax = plt.subplots(figsize=(4, 5))
        if sexe == "female":
             sns.barplot(x=list(stat_survive("Age", "female").keys()), y=list(stat_survive("Age", "female").values()))
             ax.set_xticklabels(list(stat_survive("Age", "female").keys()), rotation = 45)
             ax.set(title="Taux de survie des femmes par tranche d'âge",
                    xlabel="tranche d'âge",
                    ylabel="taux de survie")
             ax.set(title="Taux de survie des personnes")
             for i, v in enumerate(list(stat_survive("Age", "female").values())):
                ax.annotate(f"{v * 100:.2f}%", (i, v), ha='center', va='bottom', fontsize=10)
        elif sexe == "male":
            sns.barplot(x=list(stat_survive("Age", "male").keys()), y=list(stat_survive("Age", "male").values()))
            ax.set_xticklabels(list(stat_survive("Age", "male").keys()), rotation = 45)
            ax.set(title="Taux de survie des hommes par tranche d'âge",
                   xlabel="tranche d'âge",
                   ylabel="taux de survie")
            for i, v in enumerate(list(stat_survive("Age", "male").values())):
                ax.annotate(f"{v * 100:.2f}%", (i, v), ha='center', va='bottom', fontsize=10)
        else:
             if categorie == "Age":
                sns.barplot(x=list(stat_survive("Age").keys()), y=list(stat_survive("Age").values()))
                ax.set_xticklabels(list(stat_survive("Age").keys()), rotation = 45)
                ax.set(title="Taux de survie des personnes par tranche d'âge",
                       xlabel="tranche d'âge",
                       ylabel="taux de survie")
                for i, v in enumerate(list(stat_survive("Age").values())):
                    ax.annotate(f"{v * 100:.2f}%", (i, v), ha='center', va='bottom', fontsize=10)            
             elif categorie == "Sex":
                sns.barplot(x=list(stat_survive("Sex").keys()), y=list(stat_survive("Sex").values()))
                ax.set(title="Taux de survie des personnes par sexe",
                       xlabel="sexe",
                       ylabel="taux de survie")
                for i, v in enumerate(list(stat_survive("Sex").values())):
                    ax.annotate(f"{v * 100:.2f}%", (i, v), ha='center', va='bottom', fontsize=10)
             elif categorie == "Pclass":
                sns.barplot(x=list(stat_survive("Pclass").keys()), y=list(stat_survive("Pclass").values()))
                ax.set(title="Taux de survie des personnes par classe",
                xlabel="classe",
                ylabel="taux de survie")
                for i, v in enumerate(list(stat_survive("Pclass").values())):
                     ax.annotate(f"{v * 100:.2f}%", (i, v), ha='center', va='bottom', fontsize=10)
        fig.savefig(f"figure/{sexe}_{categorie}")
  
    
                  

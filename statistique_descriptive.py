import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def Statistique_Descriptives(
    data, 
    var_num, 
    bins=30,
    color_hist="skyblue", 
    color_mean="red", 
    color_median="green",
    show_kde=False
):
    # Vérification
    if var_num not in data.columns:
        raise ValueError(f"La variable '{var_num}' n'existe pas dans le dataset.")
    
    values = data[var_num].dropna()
    
    if values.empty:
        raise ValueError(f"La variable '{var_num}' ne contient pas de valeurs exploitables.")
    
    # Statistiques
    mean = values.mean()
    median = values.median()
    std = values.std()
    skew = values.skew()
    
    # Figure
    plt.figure(figsize=(10, 6))
    
    # Histogramme
    plt.hist(values, bins=bins, color=color_hist, edgecolor="black", alpha=0.7)
    
    # Lignes statistiques
    plt.axvline(mean, color=color_mean, linestyle="--", linewidth=2, label=f"Moyenne: {mean:.2f}")
    plt.axvline(median, color=color_median, linestyle="--", linewidth=2, label=f"Médiane: {median:.2f}")
    
    # Titre + labels
    plt.title(f"Distribution de {var_num}", fontsize=14, fontweight="bold")
    plt.xlabel(var_num)
    plt.ylabel("Fréquence")
    
    # Ajout d'un résumé statistique dans le graphe
    stats_text = (
        f"N = {len(values)}\n"
        f"Std = {std:.2f}\n"
        f"Skew = {skew:.2f}"
    )
    
    plt.text(
        0.95, 0.95, stats_text,
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
    )
    
    plt.legend()
    plt.tight_layout()
    plt.show()

def detection_outliers(data, var):
    
    
    values = data[var].dropna()
        
    # Calcul des quartiles
    Q1 = values.quantile(0.25)
    Q3 = values.quantile(0.75)
    IQR = Q3 - Q1
        
    # Bornes des outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
        
    # Détection des valeurs aberrantes
    outliers = values[(values < lower_bound) | (values > upper_bound)]
        
    # Affichage graphique
    plt.figure()
    plt.boxplot(values, patch_artist=True,
        boxprops=dict(facecolor="skyblue"),
        flierprops=dict(marker='o', markerfacecolor='red', markersize=5))
    plt.title(f"Boxplot de {var}")
    plt.ylabel(var)
    plt.show()
        
        # Affichage des résultats
    print(f"--- {var} ---")
    print(f"Nombre de valeurs aberrantes : {len(outliers)}")
    print(f"Bornes : [{lower_bound:.2f}, {upper_bound:.2f}]")
    print(f"Exemples de valeurs aberrantes :")
    print(outliers.head())
    print("\n")






def analyse_categorielle(data, var, normalize=False, top_n=None, figsize=(8,5)):
    """
    Analyse une variable catégorielle avec visualisation et statistiques.

    Paramètres :
    - data : DataFrame pandas
    - var : variable catégorielle (str)
    - normalize : bool (affiche les proportions si True)
    - top_n : int (affiche uniquement les top modalités)
    - figsize : tuple (taille du graphique)
    """

    # Vérification
    if var not in data.columns:
        print(f"⚠️ La variable '{var}' n'existe pas dans le dataset.")
        return

    # Comptage
    counts = data[var].value_counts(dropna=False, normalize=normalize)

    # Top N si demandé
    if top_n is not None:
        counts = counts.head(top_n)

    # Graphique
    plt.figure(figsize=figsize)
    sns.barplot(x=counts.index, y=counts.values)

    plt.title(f"Distribution de {var}", fontsize=14, fontweight="bold")
    plt.xlabel(var)
    plt.ylabel("Proportion" if normalize else "Nombre d'observations")
    plt.xticks(rotation=45)
    
    # Ajouter les valeurs sur les barres
    for i, v in enumerate(counts.values):
        plt.text(i, v, f"{v:.2f}" if normalize else int(v), 
                 ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

    # Affichage texte
    print(f"\n--- Analyse de {var} ---")
    print(counts)

    # Info supplémentaire
    print(f"\nNombre de modalités : {data[var].nunique(dropna=False)}")
def bivarié_num_num(data, var1, var2):
    
    plt.figure()
    plt.scatter(data[var1], data[var2], alpha=0.5)
    plt.title(f"{var1} vs {var2}")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.show()
    
    corr = data[[var1, var2]].corr().iloc[0,1]
    print(f"Corrélation ({var1}, {var2}) = {corr:.3f}")


def bivarié_cat_num(data, cat_var, num_var):
    
    plt.figure(figsize=(8,4))
    data.boxplot(column=num_var, by=cat_var)
    
    plt.title(f"{num_var} selon {cat_var}")
    plt.suptitle("")
    plt.xlabel(cat_var)
    plt.ylabel(num_var)
    plt.xticks(rotation=45)
    
    plt.show()
    
    print(data.groupby(cat_var)[num_var].describe())




def bivariate_cat_cat(data, var, target, normalize='index', figsize=(10,5)):
    """
    Analyse bivariée entre une variable catégorielle et une cible binaire.

    Paramètres :
    - data : DataFrame
    - var : variable catégorielle
    - target : variable cible (0/1)
    - normalize : 'index' pour taux, None pour effectifs
    """

    # Table croisée
    table = pd.crosstab(data[var], data[target])
    
    # Taux de défaut
    rate = pd.crosstab(data[var], data[target], normalize='index')

    # 🔹 Graphique 1 : Heatmap des effectifs
    plt.figure(figsize=figsize)
    sns.heatmap(table, annot=True, fmt="d", cmap="Blues")
    plt.title(f"Effectifs : {var} vs {target}")
    plt.show()

    # 🔹 Graphique 2 : Taux de défaut (LE PLUS IMPORTANT)
    plt.figure(figsize=figsize)
    rate[1].sort_values(ascending=False).plot(kind='bar')
    
    plt.title(f"Taux de défaut selon {var}", fontweight="bold")
    plt.ylabel("Taux de défaut")
    plt.xlabel(var)
    plt.xticks(rotation=45)

    # Ajouter les valeurs
    for i, v in enumerate(rate[1].sort_values(ascending=False)):
        plt.text(i, v, f"{v:.2f}", ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

    # Affichage console
    print("\n--- Table des effectifs ---")
    print(table)
    
    print("\n--- Taux de défaut ---")
    print(rate)

def default_summary(df, group_col):
    return df.groupby(group_col).agg(
        # Total number of borrowers in each group (sample size — critical for reliability)
        total=('Default Status', 'count'),

        # Number of borrowers who defaulted (sum of 1s in the binary target)
        defaults=('Default Status', 'sum'),

        # Default rate = mean of the binary target = proportion of defaults in the group
        default_rate=('Default Status', 'mean'),

        # Lower bound of the 95% confidence interval for the default rate.
        # Uses a normal-approximation (Wald) interval via statsmodels' proportion_confint.
        # Wider intervals signal less reliable estimates (typically small groups).
        ci_lower=('Default Status', lambda x: proportion_confint(x.sum(), len(x), alpha=0.05)[0]),

        # Upper bound of the 95% confidence interval for the default rate.
        ci_upper=('Default Status', lambda x: proportion_confint(x.sum(), len(x), alpha=0.05)[1])
    ).reset_index()  # Flatten the groupby index back into a regular column for easy display



from scipy.stats import chi2_contingency

def chi2_test(data, target, cat_vars):
    
    results = []

    for var in cat_vars:
        table = pd.crosstab(data[var], data[target])
        chi2, p, dof, _ = chi2_contingency(table)

        results.append([var, chi2, p])

    res_df = pd.DataFrame(results, columns=["Variable", "Chi2", "p-value"])
    res_df = res_df.sort_values("p-value")

    return res_df

from scipy.stats import ttest_ind

def t_test(data, target, num_vars):

    results = []

    for var in num_vars:
        g0 = data[data[target] == 0][var]
        g1 = data[data[target] == 1][var]

        stat, p = ttest_ind(g0, g1, nan_policy='omit')

        results.append([var, stat, p])

    res_df = pd.DataFrame(results, columns=["Variable", "t-stat", "p-value"])
    res_df = res_df.sort_values("p-value")

    return res_df

from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

def compute_vif(X):
    vif = pd.DataFrame()
    vif["variable"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif.sort_values("VIF", ascending=False)
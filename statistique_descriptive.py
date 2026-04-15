import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


def Statistique_Descriptives(
    data, 
    var_num, 
    color_hist="skyblue", 
    color_mean="red", 
    color_median="green"
):
    values = data[var_num].dropna()
    
    plt.figure()
    
    # Histogramme
    plt.hist(values, bins=50, color=color_hist, edgecolor="black")
    
    # Stats
    mean = values.mean()
    median = values.median()
    
    plt.axvline(mean, color=color_mean, linestyle="dashed", linewidth=2, label=f"Moyenne: {mean:.2f}")
    plt.axvline(median, color=color_median, linestyle="dashed", linewidth=2, label=f"Médiane: {median:.2f}")
    
    plt.title(f"Distribution de {var_num}")
    plt.xlabel(var_num)
    plt.ylabel("Fréquence")
    
    plt.legend()
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




def analyse_categorielle(data, var):
    
    
    counts = data[var].value_counts(dropna=False)
        
    plt.figure()
    counts.plot(kind="bar", color="skyblue", edgecolor="black")
        
    plt.title(f"Distribution de {var}")
    plt.xlabel(var)
    plt.ylabel("Nombre d'observations")
    plt.xticks(rotation=45)
        
    plt.show()
        
    print(f"--- {var} ---")
    print(counts)
    print("\n")


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



def bivarié_cat_cat(data, var1, var2):
    
    table = pd.crosstab(data[var1], data[var2])
    
    plt.figure(figsize=(6,4))
    sns.heatmap(table, annot=True, fmt="d", cmap="Blues")
    
    plt.title(f"{var1} vs {var2}")
    plt.show()
    
    print(table)
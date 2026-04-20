Explication
----
![Texte alternatif](images/correlation_heatmap.png)

---

![Texte alternatif](images/image1.png)
## Trois tendances distinctes émergent :

### 1. Grade
Le défaut antérieur apporte une information incrémentale limitée au sein des grades D à G — le grade capture déjà l’essentiel du signal de risque comportemental  
(R² = 28,76 % entre le grade et le défaut antérieur).

### 2. LTI (Loan-to-Income)
Le défaut antérieur se combine fortement avec le niveau d’endettement — un écart d’environ **15 à 20 points de pourcentage** est observé dans tous les groupes de LTI, et cet écart s’élargit pour les niveaux de LTI très élevés.

### 3. Revenu
Le défaut antérieur est indépendant du revenu — même les emprunteurs à revenu élevé ayant déjà fait défaut présentent un taux de défaut de **23 %**, soit près de **4 fois plus élevé** que leurs homologues sans défaut antérieur (6 %).

---

## Implication
Le défaut antérieur constitue un signal comportemental indépendant du revenu et du LTI, mais il est largement déjà intégré dans la variable *grade de crédit*.  
Sa contribution marginale dans un modèle incluant le grade doit donc être vérifiée : sa valeur ajoutée pourrait être limitée aux segments mal différenciés par le grade seul.

---

![Texte alternatif](images/previous_default_plot.png)

## Le comportement de défaut antérieur est un signal comportemental fort du risque futur de défaut.

La différence marquée entre les deux groupes indique que le comportement financier passé reflète des caractéristiques sous-jacentes des emprunteurs, telles que la discipline de remboursement et la stabilité financière.

Contrairement à de nombreuses variables financières qui nécessitent des transformations ou des regroupements, cette variable fournit une séparation claire et directe entre les niveaux de risque.

Cela suggère que le comportement historique capture des facteurs de risque qui ne sont pas entièrement observables à travers le revenu ou les caractéristiques du prêt uniquement.
---
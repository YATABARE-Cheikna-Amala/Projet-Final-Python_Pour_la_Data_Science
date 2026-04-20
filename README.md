Explication


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

## Implication

Le défaut antérieur agit comme un signal comportemental indépendant par rapport au revenu et au ratio LTI, mais il est en grande partie déjà intégré dans la variable *grade de crédit*.

Sa contribution marginale dans un modèle incluant le grade doit donc être validée : sa valeur ajoutée pourrait être limitée aux segments qui ne sont pas suffisamment discriminés par le grade seul.

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
![Texte alternatif](images/correlation_heatmap.png)*

## Corrélations clés avec le statut de défaut

Les résultats montrent plusieurs relations importantes entre les variables explicatives et le défaut de paiement.

Tout d’abord, le *Loan Grade* (codé numériquement) présente une corrélation positive relativement élevée avec le défaut (0,38), ce qui signifie que les grades plus risqués sont associés à une probabilité plus forte de défaut.

De manière similaire, le ratio *Loan / Income* est également positivement corrélé au défaut (0,38), indiquant que les emprunteurs qui consacrent une plus grande part de leur revenu au remboursement ont un risque plus élevé.

Le *taux d’intérêt* suit la même logique avec une corrélation positive de 0,34, suggérant que les prêts plus coûteux sont associés à des emprunteurs plus risqués.


---

## Redondance et multicolinéarité

L’analyse met également en évidence des problèmes de multicolinéarité entre certaines variables.

On observe une corrélation très forte entre le *taux d’intérêt* et le *Loan Grade* (0,94), ce qui suggère que ces deux variables capturent quasiment la même information de risque.

De même, l’*âge* et la *durée d’historique de crédit* sont fortement corrélés (0,88), indiquant une redondance dans la mesure de l’expérience financière des emprunteurs.

---

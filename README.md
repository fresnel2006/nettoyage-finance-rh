# Nettoyage de données Finance et RH (pandas + PySpark)

Nettoyage de deux jeux de données volontairement "sales" : les dépenses d'un service finance et les données RH d'une entreprise.

## Scripts
### `depense_finance.py` (pandas)
- Normalisation des colonnes texte (catégorie, service demandeur, mode et statut de paiement...)
- Montants invalides (contenant des lettres) remplacés par des valeurs vides, puis conversion en nombres
- Nettoyage de la devise
- Conversion des dates au format jour/mois/année
- Suppression des lignes vides et des doublons

### `rh.py` (PySpark)
- Lecture de `donnees_rh_sale.csv` avec Spark
- Normalisation de la colonne `prenom_nom`

## Lancer le projet
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python depense_finance.py
python rh.py
```
PySpark demande Java (JDK 8, 11 ou 17) installé sur la machine.

## Stack
Python, pandas, numpy, tabulate, PySpark

## Auteur
Ange Fresnel Traoré - ESATIC, Abidjan

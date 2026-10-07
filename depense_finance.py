import pandas as pd
from tabulate import tabulate
import numpy as np

depense_finance=pd.read_csv("depenses_finance_sale.csv")

depense_finance["categorie"]=depense_finance["categorie"].str.lower().str.strip()

depense_finance["sous_categorie"]=depense_finance["sous_categorie"].str.lower().str.strip()

depense_finance["service_demandeur"]=depense_finance["service_demandeur"].str.lower().str.strip()

depense_finance["montant"]=np.where(depense_finance["montant"].str.contains("[a-zA-Z]+",regex=True),pd.NA,depense_finance["montant"])
depense_finance["montant"]=depense_finance["montant"].astype(float)

depense_finance["devise"]=depense_finance["devise"].str.lower().str.replace(r"\s+",'',regex=True)

depense_finance["mode_paiement"]=depense_finance["mode_paiement"].str.lower().str.strip()

depense_finance["statut_paiement"]=depense_finance["statut_paiement"].str.lower().str.strip()
depense_finance["approuve_par"]=depense_finance["approuve_par"].str.lower().str.strip()
depense_finance["justificatif_fourni"]=depense_finance["justificatif_fourni"].str.lower().str.strip()

depense_finance["date_depense"]=pd.to_datetime(depense_finance["date_depense"], format="mixed", dayfirst=True, errors="coerce")

depense_finance=depense_finance.dropna()
depense_finance=depense_finance.drop_duplicates()
print(tabulate(depense_finance, tablefmt="psql",headers="keys",showindex=False))
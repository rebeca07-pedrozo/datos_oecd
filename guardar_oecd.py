import pandas as pd
import pickle

with open("datos_oecd.pkl", "rb") as f:
    datos_extraidos = pickle.load(f)

if isinstance(datos_extraidos, list) and all(isinstance(i, dict) for i in datos_extraidos):
    df = pd.DataFrame(datos_extraidos)
else:
    print(" Error: Los datos no tienen el formato correcto.")
    exit()

print(df.head())

df.to_csv("oecd_data.csv", index=False, encoding="utf-8")

print("Datos guardados correctamente en 'oecd_data.csv'")

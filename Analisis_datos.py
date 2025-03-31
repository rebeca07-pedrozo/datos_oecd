import pickle
import pandas as pd

with open("datos_oecd.pkl", "rb") as f:
    datos_cargados = pickle.load(f)

df = pd.DataFrame(datos_cargados)

print(" Datos cargados desde 'datos_oecd.pkl':")
print(df.head())

print("\n Estadísticas de los datos:")
print(df.describe())

print("\n Cantidad de datos por país:")
print(df["País"].value_counts())

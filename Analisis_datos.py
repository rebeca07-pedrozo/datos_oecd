import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("datos_oecd.pkl", "rb") as f:
    datos_cargados = pickle.load(f)

df = pd.DataFrame(datos_cargados)

print(" Datos cargados desde 'datos_oecd.pkl':")
print(df.head())

print("\n Estadísticas de los datos:")
print(df.describe())

print("\n Cantidad de datos por país:")
print(df["País"].value_counts())

plt.figure(figsize=(10, 6))
df["País"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Cantidad de Datos por País")
plt.xlabel("País")
plt.ylabel("Cantidad de Datos")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
df.describe().transpose()[['mean', 'std', 'min', '50%', 'max']].plot(kind='bar', color=sns.color_palette("Blues", 6))
plt.title("Estadísticas Descriptivas de las Columnas Numéricas")
plt.ylabel("Valor")
plt.xticks(rotation=45)
plt.show()

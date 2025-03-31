import pandas as pd
import mysql.connector

df = pd.read_pickle(r"C:\Users\USUARIO\OneDrive\Documentos\5toSemestre\BD\bd2.0\ConTrade\venv\datos_oecd.pkl")

if isinstance(df, list):
    df = pd.DataFrame(df)

conn = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="Rb31415926535",  
    database="DatosAPI"
)
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO oecd_data (Año, País, Valor)
        VALUES (%s, %s, %s)
    """, (row["Año"], row["País"], row["Valor"]))

conn.commit()
cursor.close()
conn.close()

print("Datos insertados correctamente en MySQL.")

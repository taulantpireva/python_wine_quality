# Importieren der notwendigen Bibliotheken
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Funktion zum Laden der Daten mit Fehlerüberprüfung
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Datensatz erfolgreich geladen! Form des Datensatzes: {data.shape}")
        
        # Überprüfen, ob die 'type'-Spalte vorhanden ist
        if 'type' in data.columns:
            wine_counts = data['type'].value_counts()
            print("\nAnzahl der Rot- und Weissweine im Datensatz:")
            print(wine_counts)
        else:
            print("\nDie Spalte 'type' ist nicht im Datensatz enthalten. Kann Rot- und Weissweine nicht zählen.")
        
        return data
    except FileNotFoundError:
        print("Fehler: Die angegebene Datei wurde nicht gefunden.")
    except pd.errors.ParserError:
        print("Fehler: Der Datensatz konnte nicht geparst werden. Bitte prüfen Sie die Datei.")
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return None

# Lade den Datensatz
file_path = "data/raw/wine_quality_raw.csv"
data = load_data(file_path)

# Prüfen, ob die Daten geladen wurden
if data is not None:
    display(data.head())

def overview_data(data):
    try:
        print("\nAllgemeine Informationen über den Datensatz:")
        data.info()
        print("\nStatistische Übersicht:")
        display(data.describe())
    except Exception as e:
        print(f"Fehler bei der Übersicht des Datensatzes: {e}")

if data is not None:
    overview_data(data)
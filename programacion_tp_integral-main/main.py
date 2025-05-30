import pandas as pd
from core.logging_config import logger
from preprocessing_data import preprocessing_data
from sklearn.model_selection import train_test_split

logging = logger

# 1. Cargar y preprocesar los datos
df = preprocessing_data(path_data='data/data.csv')

if df is None or df.empty:
    logging.error("No se pudo cargar el DataFrame. Finalizando ejecución.")
    exit(1)

# 2. Filtrar solo las filas entre las 20 y 22 hs inclusive
df = df[(df['hour'] >= 20) & (df['hour'] <= 22)]

# 3. Calcular los 10 canales más vistos en esa franja horaria
top_channels = (
    df.groupby('channel_name')['concurrent_view_count']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .index
)

# 4. Filtrar el DataFrame para quedarnos solo con esos 10 canales
df = df[df['channel_name'].isin(top_channels)]

# 5. Calcular el promedio de viewers por canal y definir la clase objetivo
df['avg_concurrent_views'] = df.groupby('channel_name')['concurrent_view_count'].transform('mean')
df['success'] = (df['avg_concurrent_views'] > df['avg_concurrent_views'].median()).astype(int)

# 6. Definir la clase Nodo para el árbol de decisión
class Nodo:
    def __init__(self, atributo=None, umbral=None, izquierda=None, derecha=None, clase=None):
        self.atributo = atributo
        self.umbral = umbral
        self.izquierda = izquierda
        self.derecha = derecha
        self.clase = clase

# 7. Función para calcular la entropía de un conjunto de etiquetas
def entropia(y):
    from collections import Counter
    import numpy as np
    total = len(y)
    if total == 0:
        return 0
    counts = Counter(y)
    return -sum((count / total) * np.log2(count / total) for count in counts.values() if count > 0)

# 8. Función para calcular la ganancia de información de una división
def ganancia_info(X_col, y, umbral):
    parent_entropy = entropia(y)
    left_indices = X_col <= umbral
    right_indices = X_col > umbral
    if len(y[left_indices]) == 0 or len(y[right_indices]) == 0:
        return 0
    n = len(y)
    n_left = len(y[left_indices])
    n_right = len(y[right_indices])
    weighted_entropy = (n_left / n) * entropia(y[left_indices]) + (n_right / n) * entropia(y[right_indices])
    return parent_entropy - weighted_entropy

# 9. Función para encontrar la mejor división de los datos
def mejor_division(X, y):
    mejor_ganancia = 0
    mejor_atributo = None
    mejor_umbral = None
    for atributo in X.columns:
        if X[atributo].dtype.name == 'category':
            continue  # Saltar variables categóricas para este árbol simple
        umbrales = X[atributo].unique()
        for umbral in umbrales:
            ganancia = ganancia_info(X[atributo], y, umbral)
            if ganancia > mejor_ganancia:
                mejor_ganancia = ganancia
                mejor_atributo = atributo
                mejor_umbral = umbral
    return mejor_atributo, mejor_umbral

# 10. Función recursiva para construir el árbol de decisión
def construir_arbol(X, y):
    if len(set(y)) == 1:
        return Nodo(clase=y.iloc[0])
    if X.empty:
        return Nodo(clase=y.mode()[0])
    atributo, umbral = mejor_division(X, y)
    if atributo is None:
        return Nodo(clase=y.mode()[0])
    left_indices = X[atributo] <= umbral
    right_indices = X[atributo] > umbral
    izquierda = construir_arbol(X[left_indices], y[left_indices])
    derecha = construir_arbol(X[right_indices], y[right_indices])
    return Nodo(atributo=atributo, umbral=umbral, izquierda=izquierda, derecha=derecha)

# 11. Preparar los datos para el árbol (eliminar columnas no numéricas y la clase objetivo)
X = df.drop(columns=['success', 'avg_concurrent_views', 'channel_name', 'channel_type', 'date', 'datetime_now'])
y = df['success']

# 12. Entrenar el árbol de decisión
arbol = construir_arbol(X, y)

# 13. Dividir el conjunto de datos para entrenamiento y validación
train_df, test_df = train_test_split(df, test_size=0.2, stratify=df['success'], random_state=42)

print("Conjunto de entrenamiento:", train_df.shape)
print("Conjunto de validación:", test_df.shape)
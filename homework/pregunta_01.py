"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    archivo_entrada = 'files/input/solicitudes_de_credito.csv'
    archivo_salida = 'files/output/solicitudes_de_credito.csv'
    

    datos = pd.read_csv(archivo_entrada, sep=';', index_col=0)

    # Eliminar valores nulos
    datos.dropna(inplace=True)
    
    # Normalización columna sexo
    datos['sexo'] = datos['sexo'].str.lower()
    
    # Normalizacion y limpieza tipo_de_emprendimiento
    datos['tipo_de_emprendimiento'] = datos['tipo_de_emprendimiento'].str.lower().str.strip()
    

    # Normalizacion y limpieza barrio
    datos['barrio'] = datos['barrio'].str.lower()
    datos['barrio'] = datos['barrio'].str.replace('_', ' ').str.replace('-', ' ')
    
    # Normalizacion y limpieza idea_negocio
    datos['idea_negocio'] = datos['idea_negocio'].str.lower()
    datos['idea_negocio'] = datos['idea_negocio'].str.replace('_', ' ').str.replace('-', ' ').str.strip()
    
    # Normalizacion y limpieza monto_del_credito
    datos['monto_del_credito'] = datos['monto_del_credito'].str.strip()
    datos['monto_del_credito'] = datos['monto_del_credito'].str.replace('$', '')
    datos['monto_del_credito'] = datos['monto_del_credito'].str.replace(',', '')
    datos['monto_del_credito'] = datos['monto_del_credito'].str.replace('.00', '')
    datos['monto_del_credito'] = pd.to_numeric(datos['monto_del_credito'], errors='coerce')
    
    # Normalizacion y limpieza linea_credito
    datos['línea_credito'] = datos['línea_credito'].str.lower()
    datos['línea_credito'] = datos['línea_credito'].str.replace('_', ' ').str.replace('-', ' ').str.strip()
    

    # Conversion fecha
    datos["fecha_de_beneficio"] = pd.to_datetime(
            datos["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
        ).combine_first(pd.to_datetime(datos["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))
    
    # Normalizacion comuna_ciudadano
    datos["comuna_ciudadano"] = datos["comuna_ciudadano"].astype(int)

    # Eliminacion de duplicados y nulos
    datos=datos.drop_duplicates()
    datos.dropna(inplace=True)
    
    output_directory = os.path.dirname(archivo_salida)
    os.makedirs(output_directory, exist_ok=True)
    datos.to_csv(archivo_salida, sep=';', index=False)

pregunta_01()
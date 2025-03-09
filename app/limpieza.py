import numpy as np
import pandas as pd


def excel_a_df (ruta, cols_especiales):
    data = pd.read_excel(ruta, dtype=cols_especiales)
    return data


def info_df(df, n_filas):
    print(df.head(n_filas))
    print(df.info())



def limpiar_vacios(df):
    return df.dropna(how='all')


def limpiar_nulos(df)
    df.iva = df.iva.fillna(0.12)
    df.costo = df.costo.fillna(0)
    df.unidadMedida = df.unidadMedida.fillna('DESCONOCIDO')
    df.nombreCli = df.nombreCli.fillna('DESCONOCIDO')
    return df


def imp_nulos_por_columna(df):
    print(df.isnull().sum().sort_values(ascending=False))


def ordenar_cols(df):
    df.nombreProducto.sort_values().unique().tolist()
    return df


def transformar_cols(df):
    df.cantidad = pd.to_numeric(df.cantidad, errors='coerce')
    df.cantidad = df.cantidad.fillna(0)
    return df


def exportar_en_excel(ruta):
    df.to_excel(ruta, index=False)
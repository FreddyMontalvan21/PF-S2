import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def excel_a_df (ruta, cols_especiales):
    data = pd.read_excel(ruta, dtype=cols_especiales)
    return data


def obtener_prediccion(model, X, y, test_size):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    res = X_test.copy()

    res['y_test'] = y_test
    res['y_pred'] = y_pred

    return res, y


def reg_lineal(x, y, preprocessor):
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    pred_stock_rlineal = obtener_prediccion(model, x, y, 0.2)

    pred_stock_rlineal[0].head()

    return pred_stock_rlineal



def arb_decision(x, y, preprocessor):
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', DecisionTreeRegressor(random_state=42))
    ])

    pred_stock_ardecision = obtener_prediccion(model, x, y, 0.15)
    pred_stock_ardecision[0].head()
    return pred_stock_ardecision



def rand_forest(x, y, preprocessor):
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    pred_stock_rforest = obtener_prediccion(model, x, y, 0.15)
    print(pred_stock_rforest[0].head())
    return pred_stock_rforest



def evaluar_modelo(model_pred_res):
    mse = mean_squared_error(model_pred_res[0].y_test, model_pred_res[0].y_pred)
    mae = mean_absolute_error(model_pred_res[0].y_test, model_pred_res[0].y_pred)
    r2 = r2_score(model_pred_res[0].y_test, model_pred_res[0].y_pred)

    print(f'Error Absoluto Medio (MAE): {mae}')
    print(f'Error Cuadrático Medio (MSE): {mse}')
    print(f'R² Score: {r2}')


def pred_vs_reales(model_pred_res, lbl_modelo):
    pred = model_pred_res[0]
    y = model_pred_res[1]

    plt.figure(figsize=(10, 6))
    plt.scatter(pred.y_test, pred.y_pred, color='blue', label='Predicciones')
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', label='Línea de referencia')
    plt.xlabel('Valores Reales')
    plt.ylabel('Valores Predichos')
    plt.title(f'Predicciones vs. Valores Reales en el modelo {lbl_modelo}')
    plt.legend()
    plt.show()


def distrib_err(model_pred_res):
    pred = model_pred_res[0]

    errors = pred.y_test - pred.y_pred

    plt.figure(figsize=(10, 6))
    sns.histplot(errors, kde=True)
    plt.xlabel('Error')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de Errores')
    plt.show()


def exportar_excel(ruta, df):
    df.to_excel(ruta, engine='openpyxl', index=False)
    print(f'DataFrame guardado exitosamente en {ruta}!')
     

def main():

    df = excel_a_df('datosLimpios.xlsx', {'rucCICli': str, 'telefono': str, 'climaPrecipitaciones': float, 'mes': int})
    x_stock = df[['nombreProducto', 'mes', 'anio']]
    y_stock = df['stockMensual']

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['nombreProducto']),
            ('num', 'passthrough', ['mes', 'anio'])
    ])
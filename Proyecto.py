#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 08:11:13 2024

@author: jaimeunriza
"""


import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Función para extraer datos de MetroCuadrado
def obtener_datos_metrocuadrado():
    url = "https://www.metrocuadrado.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    locales = []
    # Aquí deberías adaptar el scraping según la estructura real de la página
    for item in soup.find_all('div', class_='result-item'):
        try:
            ubicacion = item.find('span', class_='location').text.strip()
            precio = item.find('span', class_='price').text.strip()
            tamaño = item.find('span', class_='size').text.strip()
            descripcion = item.find('p', class_='description').text.strip()
            imagen = item.find('img')['src']
            locales.append({
                'Ubicación': ubicacion,
                'Precio': precio,
                'Tamaño': tamaño,
                'Descripción': descripcion,
                'Imagen': imagen
            })
        except Exception as e:
            print(f"Error al extraer un elemento: {e}")

    return pd.DataFrame(locales)

# Función para extraer datos de CienCuadras
def obtener_datos_ciencuadras():
    url = "https://www.ciencuadras.com/venta"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    locales = []
    # Aquí deberías adaptar el scraping según la estructura real de la página
    for item in soup.find_all('div', class_='result-item'):
        try:
            ubicacion = item.find('span', class_='location').text.strip()
            precio = item.find('span', class_='price').text.strip()
            tamaño = item.find('span', class_='size').text.strip()
            descripcion = item.find('p', class_='description').text.strip()
            imagen = item.find('img')['src']
            locales.append({
                'Ubicación': ubicacion,
                'Precio': precio,
                'Tamaño': tamaño,
                'Descripción': descripcion,
                'Imagen': imagen
            })
        except Exception as e:
            print(f"Error al extraer un elemento: {e}")

    return pd.DataFrame(locales)

# Función principal de la aplicación
def main():
    st.title('Análisis de Locales Comerciales en Bogotá')
    
    st.header('Datos de MetroCuadrado')
    df_metrocuadrado = obtener_datos_metrocuadrado()
    st.dataframe(df_metrocuadrado)

    st.header('Datos de CienCuadras')
    df_ciencuadras = obtener_datos_ciencuadras()
    st.dataframe(df_ciencuadras)

# Ejecutar la aplicación
if __name__ == '__main__':
    main()
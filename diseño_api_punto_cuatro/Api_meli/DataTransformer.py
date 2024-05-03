import csv
import json
import pandas as pd

# Defino la clase DataTransformer
class DataTransformer:

    # Defino la funcion transform_to_excel
    def transform_to_excel(self, csv_file, excel_file):
        try:
            df = pd.read_csv(csv_file)
            df.to_excel(excel_file, index=False)
            print(f"Los datos se han transformado y guardado en {excel_file}.")
        except Exception as e:
            print(f"Error al transformar datos a formato Excel: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    
    # Nombre del archivo CSV de entrada
    csv_file1 = "celularesApi.csv"

    # Nombre del archivo CSV de entrada
    csv_file2 = "heladerasApi.csv"

    # Nombre del archivo CSV de entrada
    csv_file3 = "termosApi.csv"
    
    # Nombre del archivo Excel de salida
    excel_file1 = "productosTransform1.xlsx"

    # Nombre del archivo Excel de salida
    excel_file2 = "productosTransform2.xlsx"

    # Nombre del archivo Excel de salida
    excel_file3 = "productosTransform3.xlsx"
    
    # Crear instancia del transformador de datos
    transformer = DataTransformer()
    
    # Transformar y guardar los datos en un archivo Excel
    transformer.transform_to_excel(csv_file1, excel_file1)

    # Transformar y guardar los datos en un archivo Excel
    transformer.transform_to_excel(csv_file2, excel_file2)

    # Transformar y guardar los datos en un archivo Excel
    transformer.transform_to_excel(csv_file3, excel_file3)

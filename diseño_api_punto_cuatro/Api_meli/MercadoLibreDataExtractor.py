import csv
from MercadoLibreAPIClient import MercadoLibreAPIClient

# Defino la clase MercadoLibreDataExtractor
class MercadoLibreDataExtractor:
    
    # Defino la funcion __init__
    def __init__(self, api_client):
        self.api_client = api_client

    # Defino la funcion extract_items_data
    def extract_items_data(self, query, limit):
        items = self.api_client.search_items(query, limit)
        if items:
            return [self.extract_item_data(item) for item in items]
        else:
            return []

    # Defino la funcion extract_item_data
    def extract_item_data(self, item):
        return {
            'ID': item['id'],
            'Título': item['title'],
            'Precio': item['price'],
            'Precio Original': item.get('original_price', 'No disponible'),
            'Condición': item['condition'],
            'Cantidad disponible': item['available_quantity'],
            'Marca': item.get('marca', 'No disponible'),
            'Envío gratuito': item.get('free_shipping', False)  # Agrego un valor predeterminado
        }

    def export_to_csv(self, data, filename):
        try:
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Los datos se han exportado correctamente a '{filename}'.")
        except IOError as e:
            print(f"Error al exportar datos a CSV: {e}")

# Ejemplo de uso
client = MercadoLibreAPIClient("https://api.mercadolibre.com")
extractor = MercadoLibreDataExtractor(client)

# Extraer datos de los primeros 150 celulares
query = "celular"
limit = 150
items_data = extractor.extract_items_data(query, limit)

# Exportar datos a un archivo CSV
extractor.export_to_csv(items_data, "celularesApi.csv")

#----------------------------------------------------------------------

# Extraer datos de las primeras 150 heladeras
query = "heladera"
limit = 150
items_data = extractor.extract_items_data(query, limit)

# Exportar datos a un archivo CSV
extractor.export_to_csv(items_data, "heladerasApi.csv")

#----------------------------------------------------------------------

# Extraer datos de los primeros 150 termos
query = "termo"
limit = 150
items_data = extractor.extract_items_data(query, limit)

# Exportar datos a un archivo CSV
extractor.export_to_csv(items_data, "termosApi.csv")
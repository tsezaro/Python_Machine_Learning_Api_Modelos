import requests

# Defino la clase MercadoLibreAPIClient
class MercadoLibreAPIClient:
    
    # Defino la funcion __init__
    def __init__(self, base_url):
        self.base_url = base_url

    # Defino la funcion get_item_details
    def get_item_details(self, item_id):
        url = f"{self.base_url}/items/{item_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError para bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error al obtener los detalles del artículo: {e}")
            return None

    # Defino la funcion search_items
    def search_items(self, query, limit):
        items = []
        offset = 0
        count = 0  # Contador para llevar la cuenta de los artículos recuperados
        while count < limit:
            url = f"{self.base_url}/sites/MLA/search?q={query}&limit=50&offset={offset}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise HTTPError para bad responses
                results = response.json()['results']
                if not results:
                    break  # No mas resultados
                items.extend(results)
                offset += 50
                count += len(results)  # Incremento el contador
            except requests.RequestException as e:
                print(f"Error al buscar artículos: {e}")
                return None
        return items[:limit]  # Retorno solo la cantidad especificada de artículos

# Ejemplo de casos de uso
client = MercadoLibreAPIClient("https://api.mercadolibre.com")

# Obtengo detalles de un artículo específico
item_id = "MLA1658689660"  
item_details = client.get_item_details(item_id)
if item_details:
    print("Detalles del artículo:")
    print(item_details)
else:
    print("No se pudieron obtener los detalles del artículo.")

# Busco artículos por palabra clave para celulares
query = "celular"
limit = 150
items = client.search_items(query, limit)
if items:
    print(f"Resultados de la búsqueda de '{query}':")
    for item in items:
        print(item)
else:
    print("No se pudieron obtener resultados de la búsqueda.")

print(f"Total de artículos recuperados: {len(items)}")


# Busco artículos por palabra clave para heladeras
query = "heladera"
limit = 150
items = client.search_items(query, limit)
if items:
    print(f"Resultados de la búsqueda de '{query}':")
    for item in items:
        print(item)
else:
    print("No se pudieron obtener resultados de la búsqueda.")

print(f"Total de artículos recuperados: {len(items)}")


# Busco artículos por palabra clave para termos
query = "termo"
limit = 150
items = client.search_items(query, limit)
if items:
    print(f"Resultados de la búsqueda de '{query}':")
    for item in items:
        print(item)
else:
    print("No se pudieron obtener resultados de la búsqueda.")

print(f"Total de artículos recuperados: {len(items)}")
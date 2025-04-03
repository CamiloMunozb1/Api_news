import requests  # Importamos la librería requests para hacer solicitudes HTTP

class BuscadorNews:
    def __init__(self):
        """Inicializa la clase solicitando al usuario un tema de búsqueda y almacenando la API Key."""
        self.busqueda_usuario = str(input("Ingresa el tema del que quieras ver una noticia: ")).strip()
        
        # Verifica que el usuario haya ingresado algo, si no, muestra un mensaje de error y termina
        if not self.busqueda_usuario:
            print("No se pueden tener campos en blanco.")
            return
        
        # API Key para autenticarse en el servicio de NewsAPI
        self.api_key = "TU_API_KEY"

    def filtrador_noticias(self):
        """Realiza la solicitud a la API de noticias y muestra la primera noticia encontrada."""
        try:
            # Construimos la URL con la búsqueda del usuario y la clave de la API
            noticias_url = f"https://newsapi.org/v2/everything?q={self.busqueda_usuario}&apiKey={self.api_key}"
            
            # Hacemos la solicitud GET a la API
            respuesta = requests.get(noticias_url)
            
            # Convertimos la respuesta a formato JSON
            respuesta_json = respuesta.json()

            # Verificamos si la solicitud fue exitosa (códigos de estado HTTP 200-299)
            if 200 <= respuesta.status_code < 300:
                # Verificamos si hay noticias en la respuesta
                if respuesta_json['articles']:
                    primer_articulo = respuesta_json['articles'][0]  # Tomamos la primera noticia encontrada

                    # Mostramos la información de la noticia al usuario
                    print(f"La noticia buscada corresponde al medio: {primer_articulo['source']['name']}")
                    print(f"La noticia corresponde al titular {primer_articulo['title']}, y a la descripcion {primer_articulo['description']}")
                    print(f"Para ampliar la información puedes consultar en: {primer_articulo['url']}")
                else:
                    print("No se encontraron noticias para esta búsqueda.")
            else:
                # Si hubo un error en la solicitud, mostramos el código de error y la descripción
                print(f"Error: {respuesta.status_code}, {respuesta.text}.")

        except Exception as error:
            # Capturamos cualquier error inesperado y lo mostramos
            print(f"Error en el programa: {error}.")

# Punto de entrada del script
if __name__ == "__main__":
    # Creamos una instancia de la clase y ejecutamos la función de búsqueda
    busqueda = BuscadorNews()
    busqueda.filtrador_noticias()

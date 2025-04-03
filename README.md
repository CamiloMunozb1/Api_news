# Buscador de Noticias

Este es un proyecto en Python que permite buscar noticias sobre un tema específico utilizando la API de [NewsAPI](https://newsapi.org/). La aplicación toma como entrada un tema y devuelve la primera noticia relevante junto con su fuente, título, descripción y un enlace para obtener más información.

## 📌 Requisitos

- Python 3.x
- La biblioteca `requests` (se puede instalar con `pip install requests`)
- Una clave de API válida de [NewsAPI](https://newsapi.org/)

## 🚀 Instalación y Uso

1. Clona este repositorio o descarga el archivo.
2. Asegúrate de tener instalada la biblioteca `requests`. Si no la tienes, instálala con:
   ```sh
   pip install requests
   ```
3. Reemplaza `TU_API_KEY` en el código con tu clave de API de NewsAPI.
4. Ejecuta el script en la terminal o consola con:
   ```sh
   python Api_news.py
   ```
5. Ingresa el tema de la noticia que deseas buscar cuando se te solicite.

## 📌 Ejemplo de Uso

```
Ingresa el tema del que quieras ver una noticia: inteligencia artificial
La noticia buscada corresponde al medio: TechCrunch
La noticia corresponde al titular OpenAI lanza una nueva IA, y a la descripción OpenAI ha anunciado su última innovación...
Para ampliar la información puedes consultar en: https://techcrunch.com/example
```

## 🛠️ Tecnologías Utilizadas

- Python 3
- Requests (para realizar solicitudes HTTP a la API de noticias)

## ⚠️ Notas

- La API de NewsAPI puede tener limitaciones en su versión gratuita.
- Si la búsqueda no arroja resultados, el programa lo indicará.

## Autor

Proyecto realizado por Juan Camilo Muñoz

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes modificarlo y usarlo libremente.

---

¡Gracias por usar el Buscador de Noticias! 🚀


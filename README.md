Python, Machine Learning, Modelos predictivos y APIs

Objetivo 
Realizar un análisis sobre la oferta/vidriera de las opciones de productos que responden a distintas búsquedas en el sitio Mercadolibre.com.ar  utilizando el lenguaje Python y las bibliotecas que considere necesarias.

1) Barrer una lista de más de 150 ítems ids en el servicio público:
https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json 
En este caso particular y solo a modo de ejemplo, son resultados para la búsqueda “chromecast”, pero deberás elegir otros términos para el experimento que permitan enriquecer el análisis en un hipotético dashboard (ejemplo Google Home, Apple TV, Amazon Fire TV, o afines para poder comparar dispositivos portátiles, o bien elegir otros 3 que te interesen para comparar). 

2) Por cada resultado, realizar el correspondiente GET por Item_Id al recurso público:
https://api.mercadolibre.com/items/{Item_Id} 

3) Escribir los resultados:
Escribir los resultados en un archivo plano delimitado por comas, desnormalizando el JSON, en tantos campos como sea necesario para guardar las variables que te interesen modelar.

4) Elaborar el diseño y la documentación de la solución:
Presentar una solución para este escenario elaborando un diagrama de alto nivel de la solución y documentando los pasos necesarios para lograr este objetivo.

5) Análisis exploratorio:
Realizar un análisis exploratorio con las variables seleccionadas para el modelo a través de un notebook jupyter.


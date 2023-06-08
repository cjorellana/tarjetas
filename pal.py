import requests
import csv
import os
from bs4 import BeautifulSoup

url = "https://www.trollandtoad.com/scarlet-violet-paldea-evolved-singles/19618?Keywords=&min-price=&max-price=&items-pp=240&item-condition=&selected-cat=19618&sort-order=&page-no=1&view=list&subproduct=0&Rarity=&CardType=&minHitPoints=&maxHitPoints="

response = requests.get(url)

# Crea una lista vacía para almacenar los datos de las tarjetas
data = []
nombre = ""



# Define el nombre del archivo
nombre_archivo = "salida.csv"
# Si el archivo ya existe, lo borra
if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)

# Abre el archivo una vez al principio para escribir el encabezado
with open(nombre_archivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre","precio1","precio2","precio3","precio4","precio5","precio6","precio7","precio8"])  # Escribe el encabezado

if response.status_code == 200:
    html_content = response.text
    # print(html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Busca todas las etiquetas de contenedor de tarjetas
    card_containers = soup.find_all("div", class_="product-col col-12 p-0 my-1 mx-sm-1 mw-100")

    # Itera sobre las etiquetas de contenedor de tarjetas
    for index, card_container in enumerate(card_containers, start=1):    
        a_tag = card_container.find("a", class_="card-text")
        a_tag_text = a_tag.text if a_tag else "Etiqueta <a> no encontrada"



        #print(f"Tarjeta {index}: {a_tag_text}")
        nombre = {a_tag_text}
        nombre = str(nombre)
        nombre = nombre.replace("{", "").replace("}", "").replace("'", "").replace('"', '')
        precios = []


        #with open(nombre_archivo, mode='a', newline='') as file:
        #    writer = csv.writer(file)
        #    writer.writerow({a_tag_text})  # Escribe el índice

        # Encuentra todas las etiquetas <div> con la clase "col-2 text-center p-1" dentro del contenedor de tarjeta
        price_div_tags = card_container.find_all("div", class_="col-2 text-center p-1")

        # Itera sobre las etiquetas <div> encontradas e imprime el texto contenido en ellas
        for price_index, price_div_tag in enumerate(price_div_tags, start=1):
            price_div_text = price_div_tag.text.strip() if price_div_tag else "Etiqueta <div> no encontrada"

            texto= str({price_div_text})
           
            
            

            if texto.strip() == "{'Quantity'}":                            
                continue
            elif texto.strip() == "{'Price'}":
                continue
            elif texto.strip() == "{''}":
                continue
            else:
                texto = texto.replace("$", "").replace("'", "").replace("{", "").replace("}", "")  # Eliminamos los caracteres no numéricos
                valor = float(texto)  # Convertimos la cadena a float
                precios.append(valor)
                
                #print(texto)
                #print(f"{nombre} {texto}")

            #lse:
            #print(f"Precio {price_index}: {price_div_text}")
        else:
            #numeros_str = ', '.join(str(precio) for precio in precios)            
            #print(precios)
            
            tmp=[]
            tmp.append(nombre)
            for x in precios:
                tmp.append(x)
            
            #print(tmp)

            # imprimimos
            with open(nombre_archivo, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(tmp)  # Escribe el índice

          
                    
                


        #print("--------------------") # salto de linea
        #break # para que solo corra una vez
    
    
else:
    print(f"Error al obtener la página: {response.status_code}")
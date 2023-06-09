import requests
from bs4 import BeautifulSoup

# https://www.trollandtoad.com/pokemon/scarlet-violet-base-set-singles/19467?Keywords=&min-price=&max-price=&items-pp=240&item-condition=&selected-cat=19467&sort-order=&page-no=1&view=list&subproduct=0&Rarity=&CardType=&minHitPoints=&maxHitPoints=

# https://www.trollandtoad.com/pokemon/scarlet-violet-base-set-singles/19467?Keywords=&min-price=&max-price=&items-pp=240&item-condition=&selected-cat=19467&sort-order=&page-no=2&view=list&subproduct=0&Rarity=&CardType=&minHitPoints=&maxHitPoints=

url = "https://www.trollandtoad.com/pokemon/scarlet-violet-base-set-singles/19467?Keywords=&min-price=&max-price=&items-pp=240&item-condition=&selected-cat=19467&sort-order=&page-no=1&view=list&subproduct=0&Rarity=&CardType=&minHitPoints=&maxHitPoints=" 

response = requests.get(url)

# Crea una lista vacía para almacenar los datos de las tarjetas
cards_data = []

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

        




        print(f"Tarjeta {index}: {a_tag_text}")

        # Encuentra todas las etiquetas <div> con la clase "col-2 text-center p-1" dentro del contenedor de tarjeta
        price_div_tags = card_container.find_all("div", class_="col-2 text-center p-1")

        # Itera sobre las etiquetas <div> encontradas e imprime el texto contenido en ellas
        for price_index, price_div_tag in enumerate(price_div_tags, start=1):
            price_div_text = price_div_tag.text.strip() if price_div_tag else "Etiqueta <div> no encontrada"
            print(f"Precio {price_index}: {price_div_text}")

        print("--------------------")
    
    
else:
    print(f"Error al obtener la página: {response.status_code}")
# 1- Se parte de la premisa que ya tenemos instalados python 2.7 con django con su respectiva version
# 2- Instalar scraping haciendo uso de pip:
#     pip install scrapy --user
# 3- Establecer el path de python PATH="$HOME/Library/Python/2.7/bin/:$PATH"
# 4- ubicarse en la carpeta donde esta el proyecto haciendo uso del comando cd /
# 5- Ejecutar el proyecto con el siguiente comando 
#    scrapy runspider index.py -o scraped_data.json
#    nota: en casao de presentar el error 
#    from OpenSSL._util import lib as pyOpenSSLlib
#    ImportError: No module named _util
#    se debe actualizar pyopenssl con el comando sudo pip install pyopenssl --user --upgrade


Ejemplo:

PATH="$HOME/Library/Python/2.7/bin/:$PATH"
scrapy runspider index.py -o out.json



Nota: Puedes usar el shell para comprension de la lectura del scraping
# scrapy shell
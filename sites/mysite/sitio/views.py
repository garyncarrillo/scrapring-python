# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json, urllib
from django.http import JsonResponse

from django.template import loader, Context
from django.http import HttpResponse 



# importar los modelos
# ORM DJANGO
from sitio.models import menu
from sitio.models import informacion
from sitio.models import Planes
from sitio.models import Cabeceras
from sitio.models import mprincipal

# Create your views here.

def get_menu(request):
    pmenu = menu.objects.all()
    mi_template = loader.get_template("menu.html")
    mi_contexto = Context({'menus':pmenu}) 
    if pmenu:
    	print('Hola ***************')
    else:
    	print ('Vacio')
    return HttpResponse(mi_template.render(mi_contexto))
 
   
def get_principal(request):
    
    mi_template = loader.get_template("main.html")
    print mi_template
    return render(request, 'main.html')

def get_index(request):
    mi_template = loader.get_template("index.html")
    print mi_template
    return render(request, 'index.html')  


def set_json(request):
    estructura = request.GET['ruta']

    # Limpiar
    menu.objects.all().delete() 
 
    informacion.objects.all().delete() 
    Planes.objects.all().delete() 
    Cabeceras.objects.all().delete()
    mprincipal.objects.all().delete() 


    data = ' { "titulo":{"titulo": "Home", "link": "http://sindyk.com/"} }'
    #print "HOLA MY SONG LOVE...."
    #print estructura
    estructura = '{ "Estructura": '+estructura+' }'
    jsondata = json.loads(estructura)

    

    for key, value in jsondata.iteritems():
        #print key
        #print value
        #Para recorrer cada nodo dentro de los nodos principales


        for hijo in value:
            #print hijo

            t_menu = hijo["menu"]
            menu.objects.create( titulo=t_menu['titulo'], url=t_menu['link'])
            # ORM DJANGO

            t_menu_principal = hijo["menu_principal"]
            for i in t_menu_principal['titulo']:
                mprincipal.objects.create(titulo=i)

            t_titulo = hijo["informacion"]
            Cabeceras.objects.create(cabecera=t_titulo["img"])
            for i in t_titulo["titulo"]:
                print "***. "+i;
                informacion.objects.create( titulo= i, img =hijo["banner"])

        
            
            t_planes = hijo["planes_1"]
            Planes.objects.create( titulo= t_planes["titulo"], informacion =t_planes["sub_titulo"])
            for det in t_planes["detalle"]:
                print "+++ "+det
            
            t_planes = hijo["planes_2"]
            Planes.objects.create( titulo= t_planes["titulo"], informacion =t_planes["sub_titulo"])
            for det in t_planes["detalle"]:
                print "+++ "+det

            t_planes = hijo["planes_3"]
            Planes.objects.create( titulo= t_planes["titulo"], informacion =t_planes["sub_titulo"])
            for det in t_planes["detalle"]:
                print "+++ "+det
                
            
            t_planes = hijo["planes_4"]
            Planes.objects.create( titulo= t_planes["titulo"], informacion =t_planes["sub_titulo"])
            for det in t_planes["detalle"]:
                print "+++ "+det    


            #for sub_hijo in hijo:
                #print sub_hijo    
              #print otro["color"]
 
    return JsonResponse(jsondata)



def get_menu(request):
    data_menu = menu.objects.all()
    text = ''
    for i in data_menu.values():
        text=text+' { "titulo": "'+i['titulo']+'" , "url": "'+i['url']+'"} '
    
    
    text = '{ "json":'+text+'}'
    #data = ' { "titulo":{"titulo": "Home", "link": "http://sindyk.com/"} }'
    jsondata = json.loads(text)
    return JsonResponse(jsondata)

def get_planes(request):
    data_planes = Planes.objects.all()
    text=None
    for i in data_planes.values():
        if text is None:
          text=''
          text=text+' { "titulo": "'+i['titulo'].replace('\n', ' ').replace('\r', '') +'" , "sub_titulo": "'+i['informacion'].replace('\n', ' ').replace('\r', '') +'"} '
        else:
           text=text+' , { "titulo": "'+i['titulo'].replace('\n', ' ').replace('\r', '') +'" , "sub_titulo": "'+i['informacion'].replace('\n', ' ').replace('\r', '') +'"} '
    
    text = '{ "json":['+text+'] }'
    print text 
    jsondata = json.loads(text)
    return JsonResponse(jsondata)

def get_informacion(request):
    data_informacion = informacion.objects.all()
    text = None
    for i in data_informacion.values():
        if text is None:
          text=''
          text=text+' { "titulo": "'+i['titulo'].replace('\n', ' ').replace('\r', '') +'" , "img": "'+i['img'].replace('\n', ' ').replace('\r', '') +'"} '
        else:
           text=text+' , { "titulo": "'+i['titulo'].replace('\n', ' ').replace('\r', '') +'" , "img": "'+i['img'].replace('\n', ' ').replace('\r', '') +'"} '
    
    text = '{ "json":['+text+'] }'
    print text 
    jsondata = json.loads(text)
    return JsonResponse(jsondata)

def get_cabeceras(request):
    data_cab = Cabeceras.objects.all()
    text = ''
    for i in data_cab.values():
        text=text+' { "cabecera": "'+i['cabecera']+'" , "pie": "'+i['pie']+'"} '
    
    
    text = '{ "json":'+text+'}'
    #data = ' { "titulo":{"titulo": "Home", "link": "http://sindyk.com/"} }'
    jsondata = json.loads(text)
    return JsonResponse(jsondata)

def get_menu_principal(request):
    data_informacion = mprincipal.objects.all()
    text = None
    for i in data_informacion.values():
        if text is None:
          text=''
          text=text+' { "titulo": "'+i['titulo'].replace('\n', ' ').replace('\r', '') +'" , "url": "'+i['url'].replace('\n', ' ').replace('\r', '') +'"} '
        else:
           text=text+' , { "titulo": "'+i['titulo'].replace('\n', ' ').replace('\r', '') +'" , "url": "'+i['url'].replace('\n', ' ').replace('\r', '') +'"} '
    
    text = '{ "json":['+text+'] }'
    print text 
    jsondata = json.loads(text)
    return JsonResponse(jsondata)

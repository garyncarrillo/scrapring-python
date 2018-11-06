

from scrapy import Field, Spider, Item, Selector

import json

class Menu (Item):
    titulo = Field()
    link = Field()

class Planes(Item):
   titulo=Field()
   sub_titulo = Field()
   detalle = Field()

class Informacion(Item):
    titulo = Field()
    img = Field()
   
class MPrincipal(Item):
    titulo = Field()
    url = Field()



class Post(Item):
    menu = Field()
    informacion = Field()
    banner = Field()
    menu_principal = Field()
    planes_1 = Field()
    planes_2 = Field()
    planes_3 = Field()
    planes_4 = Field()

class index(Spider):
    name ="primero"
    start_urls = ['http://sindyk.com/planes/']

    def parse(self, response):
        sel = Selector(response)
        #print "********************************************************************************** primero"
        seleccion = sel.css(".mkd-mobile-header")


        #print seleccion
        #print "********************************************************************************** segundo"
    
        items = []
     
        #sel.css(".mkd-position-right-inner").xpath("//nav/ul/li/a/span/span/span/text()").extract()
        for elementos in seleccion.css(".mkd-position-right-inner"):

           post = Post()
           pmenu = Menu()
           menu_p = MPrincipal()
           pinformacion = Informacion()
          
           sub_elemento  = elementos.css(".mkd-position-right-inner").xpath("//nav/ul/li/a/span/span/span/text()").extract()
           print "Nombre de los menus"
           i =-1
           v_menu =[]
           while (i<=4):
             i=i+1
             v_menu.append(sub_elemento[i])
           

          

           #print sub_elemento[0]
           #print sub_elemento[1]
           #print sub_elemento[2]
           #print sub_elemento[3]
           #print sub_elemento[4]
           #print sub_elemento[5]
          
   
        
       
           #print "link"
           sub_link = elementos.css(".mkd-position-right-inner").xpath("//nav/ul/li/a/@href").extract()
           #print  sub_link [0]
           #print  sub_link [1]
           #print  sub_link [2]
           #print  sub_link [3]
           #print  sub_link [4]

          

     
           sub_img = sel.css(".mkd-mobile-logo-wrapper").xpath("//a/img/@src").extract()
           #.xpath("//a/img/@src/text()").extract()
           #print "imagen"
           #print sub_img[0] 
           #print sub_img[1] 
           #print sub_img[2] 
           #print sub_img[3] 

     
            
           #print "Texto"
           sub_text =sel.css(".mkd-custom-font-holder::text").extract() 
           #print sub_text[0]
           #print sub_text[1]



           sub_title = sel.css(".mkd-section-subtitle::text").extract()
           #print sub_title[0]


          

           print " ++++++++++++++++++++ tableus +++++++++++++++++++++++++++++"
           planes = sel.css(".mkd-pricing-tables-inner").xpath("//li/h4/text()").extract()
           #print planes
           costos = sel.css(".mkd-pricing-tables-inner").xpath("//li/h6/text()").extract()
           #print costos
           #print costos[1]



           #print "+++++++++tableus detall 2 ++++++++++++++++++++"
           precio_unitario =sel.css(".mkd-pricing-tables-inner").xpath("//li/div/span/text()").extract()
           #print "++++++++++++++++  "+precio_unitario

     

           #print "+++++++++tableus detall 3 ++++++++++++++++++++"
           feature=sel.css(".mkd-pricing-tables-inner").xpath("//li/ul/li/text()").extract()
           #print feature [0]
           #print feature [1]
           #post['menu'] = sub_elemento
           #post['link'] = sub_link[0]
           #post['imagen'] = sub_img
           #post['texto'] = 
           #post['otro_texto'] = sub_title
           #post['planes'] = planes
           #post['precios_total'] = costos
           #post['precios_total'] = precio_unitario
           #post['caracteristicas'] = feature

          #p =sel.css(".mkd-content-inner").extract() 
           #print "*****************************+++++++++++++++++++++++++++" 
           p =sel.css(".mkd-content-inner")
           p = p.css(".mkd-full-width")
           p = p.css(".mkd-full-width-inner")
           p = p.css(".mkd-grid-row")
           p = p.css(".mkd-page-content-holder")
           p = p.css(".vc_row").extract()

           #div_style = p.find('div')['style']
           #style = cssutils.parseStyle(div_style)
           #url = style['background-image']

           #p.value_of_css_property("background-image")
           texto = p[0]
           inicio =p[0].find('url(')
           fin = p[0].find('.png')
           pbanner= texto[inicio+4:fin+4]

           # vc_row wpb_row vc_row-fluid mkd-section vc_custom_1506448364898 mkd-content-aligment-center mkd-parallax-section-holder mkd-parallax-section-holder-touch-disabled
        
      
          
    

           #print sel.css(".mkd-pricing-tables-inner").extract()


           index =-1
           v_planes=[]
           v_costo=[]
           v_detalle=[]
           for p in sel.css(".mkd-pricing-tables-inner"):
        
             for j in p.css(".mkd-price-table"):
                index = index +1
                v_planes.append(planes[index])
                v_costo.append(costos[index])
                v_detalle.append(j.xpath("//ul/li/ul/li/text()").extract())  
           
       
                #pplanes['titulo'] = planes[index]
                #pplanes['sub_titulo'] = costos[index]
                #pplanes['detalle'] = j.xpath("//ul/li/ul/li/text()").extract()


           

      

           pplanes1 = Planes()
           pplanes1['titulo'] = v_planes[0]
           pplanes1['sub_titulo'] = v_costo[0]
           pplanes1['detalle'] = v_detalle[0]
           

    

           pplanes2 = Planes()
           pplanes2['titulo'] = v_planes[1]
           pplanes2['sub_titulo'] = v_costo[1]
           pplanes2['detalle'] = v_detalle[1]

     
            
           
           pplanes3 = Planes()
           pplanes3['titulo'] = v_planes[2]
           pplanes3['sub_titulo'] = v_costo[2]
           pplanes3['detalle'] = v_detalle[2]

      
           pplanes4 = Planes()
           pplanes4['titulo'] = v_planes[3]
           pplanes4['sub_titulo'] = v_costo[3]
           pplanes4['detalle'] = v_detalle[3]
          

           pmenu['titulo']= sub_elemento[0]
           pmenu['link']= sub_link[0]
           post['menu']= pmenu

           pinformacion['titulo'] = sub_text
           pinformacion['img'] = sub_img[0]

           post['planes_1'] = pplanes1
           post['planes_2'] = pplanes2
           post['planes_3'] = pplanes3
           post['planes_4'] = pplanes4
       
           menu_p['titulo'] = v_menu
           menu_p['url']=""
           post['menu_principal'] =menu_p
    
           post['informacion'] = pinformacion
           post['banner'] = pbanner 
           items.append(post)  
        return items
      

        


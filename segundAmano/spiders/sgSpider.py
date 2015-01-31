#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy, sys, locale, os, urllib, subprocess, re
from segundAmano.items import SegundamanoItem
from scrapy.http import Request
from scrapy import Selector

DOMAIN = 'www.segundamano.mx'
URL = 'http://www.segundamano.mx/mexico/venta_inmuebles?ca=11_s&cg=1020'

class SGSpider(scrapy.Spider):

    name = 'sgspider'
    allowed_domains = [DOMAIN]
    start_urls = [
        URL
    ]

    def extractText(self, eList, index):

        if len(eList) > index:
            return eList[index].strip()

        else:
            return ''

    def setParams(self, hxs, newItem):

		newItem['SG_Habitaciones_CLO'] = ''
		newItem['SG_Superficie_FLO'] = ''
		newItem['SG_Tipo_de_inmueble_CLO'] = ''

		for cIndex in range(1,10):

			pString = self.extractText( hxs.xpath("string(//div[@class=\'AdParams\'][2]/ul[1]/li["+str(cIndex)+"])").extract(), 0)

			if pString:

				if pString.startswith("Habitaciones: "):
					newItem['SG_Habitaciones_CLO'] = pString[14:]

				elif pString.startswith("Superficie: "):
					newItem['SG_Superficie_FLO'] = self.extractText( pString[12:].split(' '), 0) 

				elif pString.startswith("Tipo de inmueble: "):
					newItem['SG_Tipo_de_inmueble_CLO'] = pString[18:]

			else:
				break

    def setLocation(self, hxs, newItem):  
		
		newItem['SG_Estado_CLO'] = self.extractText( hxs.xpath("string(//div[@class=\'navigation_path\']/a[2])").extract(), 0)

		newItem['SG_Colonia_CLO'] = ''
		newItem['SG_Delegacion_CLO'] = ''

		for cIndex in range(1,10):

			pString = self.extractText( hxs.xpath("string(//div[@class=\'AdParams\'][2]/ul[2]/li["+str(cIndex)+"])").extract(), 0)

			if pString:

				if pString.startswith("Colonia: "):
					newItem['SG_Colonia_CLO'] = pString[9:]

				elif pString.startswith("Municipio: "):
					newItem['SG_Delegacion_CLO'] = pString[11:]

				elif pString.startswith(u"Delegaci\xf3n: "):
					newItem['SG_Delegacion_CLO'] = pString[12:]

			else:
				break										

    def parseItem(self, response):

		hxs = Selector(response)
        
		newItem = SegundamanoItem()

		newItem['SG_Listing_URL'] = response.url

		newItem['SG_Poster_CLO'] = self.extractText( hxs.xpath("//div[@class=\'AdHeaderBar\']/span/text()").extract(), 0)
		proAdStr='Este anuncio es de un profesional.'		

		if proAdStr==newItem['SG_Poster_CLO']:
			newItem['SG_Poster_CLO'] = u'Profesional'
		else:
			newItem['SG_Poster_CLO'] = u'Particular'

		newItem['SG_Titulo_TXT'] = self.extractText( hxs.xpath("//h1[@class=\'AdTitle\']/text()").extract(), 0)
		newItem['SG_Descripcion_del_anuncio_TXT'] = self.extractText( hxs.xpath("string(//span[@class=\'description\'])").extract(), 0)		

		priceStr = self.extractText( hxs.xpath("//li[@class=\'AdPrice\']/text()").extract(), 0).replace("Precio:","").strip()

		newItem['SG_Moneda_CLO'] = ''		
		newItem['SG_Precio_FLO'] = ''

		if priceStr:

			if priceStr.startswith("$"):
				newItem['SG_Moneda_CLO'] = 'MXN'
			elif priceStr.startswith("US"):			
				newItem['SG_Moneda_CLO'] = 'USD'

			newItem['SG_Precio_FLO'] = priceStr

		self.setParams(hxs, newItem)
		self.setLocation(hxs, newItem)

		newItem['SG_Nombre_TXT'] = self.extractText( response.xpath("//div[@class=\'contact_element adcontact_aligner\']/span/text()").extract(), 0)		

		imgUrl = self.extractText( hxs.xpath("//img[@class=\'AdPhonenum\']/@src").extract(), 0)
		newItem['SG_Telefono_TXT'] = ''

		if imgUrl:
			imgUrl = "http://www.segundamano.mx"+imgUrl

			f = urllib.urlopen(imgUrl)

			with open("PNImage.gif", "wb") as imgFile:
				imgFile.write(f.read())

			with open(os.devnull, "w") as fnull:				
				process = subprocess.Popen('tesseract PNImage.gif phoneNumber -psm 6', shell=True, stdout=fnull, stderr=fnull)
				process.wait()

			with open('phoneNumber.txt', 'r') as pData:
				newItem['SG_Telefono_TXT'] = unicode( re.sub("[^0123456789()-+]", "", pData.readline()), "UTF-8")

			os.remove('phoneNumber.txt')
			os.remove('PNImage.gif') 			

		newItem['SG_Photo_1_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb0\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_2_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb1\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_3_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb2\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_4_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb3\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_5_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb4\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_6_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb5\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_7_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb6\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_8_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb7\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_9_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb8\']/img/@src").extract(), 0).replace("thumbs","images")
		newItem['SG_Photo_10_URL'] = self.extractText( hxs.xpath("//li[@id=\'thumb9\']/img/@src").extract(), 0).replace("thumbs","images")

		return newItem

    def parse(self, response):

        hxs = Selector(response)

        nextURL = self.extractText( hxs.xpath("//div[@class=\'resultcontainer\']/span[last()]/a/@href").extract(), 0)

        for url in hxs.xpath('//div[@class=\'listing_list_container\']/div/a/@href').extract():
            yield Request(url, callback=self.parseItem)
                  
        if len(nextURL):                
            yield Request(nextURL, callback=self.parse)                                              
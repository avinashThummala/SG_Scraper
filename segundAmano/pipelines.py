# -*- coding: utf-8 -*-
 
import hashlib, sys, MySQLdb, re
from scrapy.exceptions import DropItem
from scrapy.http import Request

class SegundAmanoPipeline(object):

	def __init__(self):

		self.conn = MySQLdb.connect(user='root', passwd='baggio', db='pyScrapper', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def getFloat(self, floatStr):

		floatStr = re.sub("[^0123456789\.-]", '', floatStr)

		if floatStr:
			return float(floatStr)		
		else:
			return None			

	def process_item(self, newItem, spider):
				
		try:

			self.cursor.execute("""INSERT INTO segundAmano VALUES (

				%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
				        	
				)""", (

				newItem['SG_Listing_URL'].encode('utf-8'),

				newItem['SG_Poster_CLO'].encode('utf-8'),
				newItem['SG_Tipo_de_inmueble_CLO'].encode('utf-8'),

				self.getFloat(newItem['SG_Superficie_FLO']),
				newItem['SG_Habitaciones_CLO'].encode('utf-8'),

				newItem['SG_Titulo_TXT'].encode('utf-8'),
				newItem['SG_Descripcion_del_anuncio_TXT'].encode('utf-8'),

				self.getFloat(newItem['SG_Precio_FLO']),
				newItem['SG_Moneda_CLO'].encode('utf-8'),

				newItem['SG_Estado_CLO'].encode('utf-8'),
				newItem['SG_Delegacion_CLO'].encode('utf-8'),
				newItem['SG_Colonia_CLO'].encode('utf-8'),				

				newItem['SG_Nombre_TXT'].encode('utf-8'),
				newItem['SG_Telefono_TXT'].encode('utf-8'),

				newItem['SG_Photo_1_URL'].encode('utf-8'),
				newItem['SG_Photo_2_URL'].encode('utf-8'),
				newItem['SG_Photo_3_URL'].encode('utf-8'),
				newItem['SG_Photo_4_URL'].encode('utf-8'),
				newItem['SG_Photo_5_URL'].encode('utf-8'),
				newItem['SG_Photo_6_URL'].encode('utf-8'),
				newItem['SG_Photo_7_URL'].encode('utf-8'),
				newItem['SG_Photo_8_URL'].encode('utf-8'),
				newItem['SG_Photo_9_URL'].encode('utf-8'),
				newItem['SG_Photo_10_URL'].encode('utf-8')

			))

			self.conn.commit()

			return newItem

		except MySQLdb.Error, e:

			print "Error %d: %s" % (e.args[0], e.args[1])	       
			return newItem		
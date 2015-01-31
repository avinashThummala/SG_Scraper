# -*- coding: utf-8 -*-

import scrapy

class SegundamanoItem(scrapy.Item):

	SG_Poster_CLO = scrapy.Field()
	SG_Tipo_de_inmueble_CLO = scrapy.Field()

	SG_Superficie_FLO = scrapy.Field()
	SG_Habitaciones_CLO = scrapy.Field()

	SG_Titulo_TXT = scrapy.Field()
	SG_Descripcion_del_anuncio_TXT = scrapy.Field()

	SG_Precio_FLO = scrapy.Field()
	SG_Moneda_CLO = scrapy.Field()

	SG_Estado_CLO = scrapy.Field()
	SG_Delegacion_CLO = scrapy.Field()
	SG_Colonia_CLO = scrapy.Field()

	SG_Nombre_TXT = scrapy.Field()
	SG_Telefono_TXT = scrapy.Field()

	SG_Photo_1_URL = scrapy.Field()
	SG_Photo_2_URL = scrapy.Field()
	SG_Photo_3_URL = scrapy.Field()
	SG_Photo_4_URL = scrapy.Field()
	SG_Photo_5_URL = scrapy.Field()
	SG_Photo_6_URL = scrapy.Field()
	SG_Photo_7_URL = scrapy.Field()
	SG_Photo_8_URL = scrapy.Field()
	SG_Photo_9_URL = scrapy.Field()
	SG_Photo_10_URL = scrapy.Field()
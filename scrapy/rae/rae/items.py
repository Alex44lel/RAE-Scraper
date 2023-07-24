# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WordItem(scrapy.Item):
    # define the fields for your item here like:
    word = scrapy.Field()

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

class WordWithDefItem(scrapy.Item):
    word_name = scrapy.Field()
    definitions = scrapy.Field()
    number_of_definitions = scrapy.Field()


class AcepcionesItem(scrapy.Item):
    text = scrapy.Field()
    tipo = scrapy.Field()
    number = scrapy.Field()

class LocucionesItem(scrapy.Item):
    locucion_name = scrapy.Field()
    definitions = scrapy.Field()

class LocucionesDefinitionItem(scrapy.Item):
    text = scrapy.Field()
    tipo = scrapy.Field()
    number = scrapy.Field()

class DefinitionItem(scrapy.Item):
    acepciones = scrapy.Field(serializer=list)
    locuciones = scrapy.Field()
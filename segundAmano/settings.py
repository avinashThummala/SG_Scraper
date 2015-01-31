# -*- coding: utf-8 -*-

# Scrapy settings for segundAmano project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'segundAmano'

SPIDER_MODULES = ['segundAmano.spiders']
NEWSPIDER_MODULE = 'segundAmano.spiders'

ITEM_PIPELINES = {

    'segundAmano.pipelines.SegundAmanoPipeline': 300,
}


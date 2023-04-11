# -*- coding: utf-8 -*- #
"""
@created: 21/11/2019
@author: Julio Lafuente
@author: DxD
@version: 1.0
"""

import requests
from app  import configuration
import logging

log = logging.getLogger('root')


def get_browsers(view, date):

    log.info('Get_Browsers - View:' + view + ", Date: " + str(date.strftime('%Y-%m-%d')))

    url = (
        "http://estadisticasweb.aragon.local/services/v1/reportservice/data"
        "?login=opendata"
        "&password=" + configuration.URCHIN_KEY +
        "&ids=%s"
        "&start-date=%s"
        "&end-date=%s"
        "&dimensions=browser_base,platform_base"
        "&metrics=visits"
        "&table=7"
    ) % (str(view), str(date.strftime('%Y-%m-%d')), str(date.strftime('%Y-%m-%d')))

    response = requests.get(url, stream=True)

    return response.text


def get_countries(view, date):

    log.info('Get_Countries - View:' + view + ", Date: " + str(date.strftime('%Y-%m-%d')))

    url = (
        "http://estadisticasweb.aragon.local/services/v1/reportservice/data"
        "?login=opendata"
        "&password=" + configuration.URCHIN_KEY +
        "&ids=%s"
        "&start-date=%s"
        "&end-date=%s"
        "&dimensions=geo_country,geo_region,geo_city,geo_latitude,geo_longitude"
        "&metrics=visits"
        "&table=3"
    ) % (str(view), str(date.strftime('%Y-%m-%d')), str(date.strftime('%Y-%m-%d')))

    response = requests.get(url, stream=True)

    return response.text


def get_files(view, date):

    log.info('Get_Files - View:' + view + ", Date: " + str(date.strftime('%Y-%m-%d')))

    url = (
        "http://estadisticasweb.aragon.local/services/v1/reportservice/data"
        "?login=opendata"
        "&password=" + configuration.URCHIN_KEY +
        "&ids=%s"
        "&start-date=%s"
        "&end-date=%s"
        "&dimensions=request_origmime,request_origfilepath"
        "&metrics=validhits"
        "&table=29"
        "&filters=request_origmime%%3D~"
        "^wmv$|^mpg$|^mp4$|^mp3$|^svg$|^txt$|^avi$|^docm$|^pps$|^ppsx$|^ppsm$|"
        "^pdf$|^xml$|^json$|^csv$|^xls$|^xlsx$|^doc$|^docx$|^ppt$|^pptx$|^zip$|"
        "^rar$|^bz2$|^tgz$|^tar$|^gz$|^7z$|^msi$|^exe$|^odt$|^wma$|^flv$"
    ) % (str(view), str(date.strftime('%Y-%m-%d')), str(date.strftime('%Y-%m-%d')))

    response = requests.get(url, stream=True)

    return response.text


def get_pages(view, date):

    log.info('Get_Pages - View:' + view + ", Date: " + str(date.strftime('%Y-%m-%d')))

    url = (
        "http://estadisticasweb.aragon.local/services/v1/reportservice/data"
        "?login=opendata"
        "&password=" + configuration.URCHIN_KEY +
        "&ids=%s"
        "&start-date=%s"
        "&end-date=%s"
        "&dimensions=initial_path_page1"
        "&metrics=visits"
        "&table=15"
    ) % (str(view), str(date.strftime('%Y-%m-%d')), str(date.strftime('%Y-%m-%d')))

    response = requests.get(url, stream=True)

    return response.text

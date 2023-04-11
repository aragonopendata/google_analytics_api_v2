# -*- coding: utf-8 -*- #
"""
@created: 21/11/2019
@author: Julio Lafuente
@author: DxD
@version: 1.0
"""

from elasticsearch import Elasticsearch
from urllib.parse import unquote
from io import StringIO
import json
import csv
from app import configuration
import logging

es = Elasticsearch([configuration.ES_HOST])
log = logging.getLogger('root')


def get_browsers(days, extension, p):

    log.info("Exporting Browsers - Days: " + days +
             ", Extension: " + extension + ", Portal: " + str(p))

    data = []

    for portal in p:
        try:
            response = es.search(
                index="logstash-reports-browsers-" + portal,
                scroll='2m',
                size=1000,
                body={
                    "query": {
                        "bool": {
                            "filter": [
                                {"range": {"@timestamp": {"gte": unquote(str(days))}}}
                            ]
                        }
                    }
                }
            )

            sid = response['_scroll_id']
            scroll_size = len(response['hits']['hits'])
                
            while (scroll_size > 0):
                data.extend(browsers_response(response))
                response = es.scroll(scroll_id=sid, scroll='2m')
                sid = response['_scroll_id']
                scroll_size = len(response['hits']['hits'])

        except:
            log.info('No index found')

    res = dict(browsers=data)

    json_file = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=1)

    if extension == "json":
        return json_file
    if extension == "csv":
        x = json.loads(json_file)
        si = StringIO()
        cw = csv.writer(si, delimiter=';')
        cw.writerow(["portal", "timestamp", "browser_name",
                     "platform_name", "visits"])
        for y in x["browsers"]:
            cw.writerow([
                y["portal"],
                y["timestamp"],
                y["browser_name"],
                y["platform_name"],
                y["visits"]])

        return si.getvalue()

    return None


def get_pages(days, extension, p):

    log.info("Exporting Pages - Days: " + days +
             ", Extension: " + extension + ", Portal: " + str(p))

    data = []

    for portal in p:
        try:
            response = es.search(
                index="logstash-reports-pages-" + portal,
                scroll='2m',
                size=1000,
                body={
                    "query": {
                        "bool": {
                            "filter": [
                                {"range": {"@timestamp": {"gte": unquote(str(days))}}}
                            ]
                        }
                    }
                }
            )

            sid = response['_scroll_id']
            scroll_size = len(response['hits']['hits'])
                
            while (scroll_size > 0):
                data.extend(pages_response(response))
                response = es.scroll(scroll_id=sid, scroll='2m')
                sid = response['_scroll_id']
                scroll_size = len(response['hits']['hits'])

        except:
            log.info('No index found')

    res = dict(pages=data)

    json_file = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=1)

    if extension == "json":
        return json_file
    if extension == "csv":
        x = json.loads(json_file)
        si = StringIO()
        cw = csv.writer(si, delimiter=';')
        cw.writerow(["portal", "path", "timestamp", "visits"])
        for y in x["pages"]:
            cw.writerow([
                y["portal"],
                y["path"],
                y["timestamp"],
                y["visits"]])

        return si.getvalue()

    return None


def get_countries(days, extension, p):

    log.info("Exporting Countries - Days: " + days +
             ", Extension: " + extension + ", Portal: " + str(p))
        
    data = []

    for portal in p:
        try:
            response = es.search(
                index="logstash-reports-countries-" + portal,
                scroll='2m',
                size=1000,
                body={
                    "query": {
                        "bool": {
                            "filter": [
                                {"range": {"@timestamp": {"gte": unquote(str(days))}}}
                            ]
                        }
                    }
                }
            )

            sid = response['_scroll_id']
            scroll_size = len(response['hits']['hits'])
                
            while (scroll_size > 0):
                data.extend(countries_response(response))
                response = es.scroll(scroll_id=sid, scroll='2m')
                sid = response['_scroll_id']
                scroll_size = len(response['hits']['hits'])

        except:
            log.info('No index found')

    res = dict(countries=data)

    json_file = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=1)

    if extension == "json":
        return json_file
    if extension == "csv":
        x = json.loads(json_file)
        si = StringIO()
        cw = csv.writer(si, delimiter=';')
        cw.writerow(["portal", "timestamp", "city", "region",
                     "country", "latitude", "longitude", "visits"])
        for y in x["countries"]:
            cw.writerow([
                y["portal"],
                y["timestamp"],
                y["city"],
                y["region"],
                y["country"],
                y["latitude"],
                y["longitude"],
                y["visits"]])

        return si.getvalue()

    return None


def get_files(days, extension, p):

    log.info("Exporting Files - Days: " + days +
             ", Extension: " + extension + ", Portal: " + str(p))

    data = []

    for portal in p:

        try:
            response = es.search(
                index="logstash-reports-files-" + portal,
                scroll='2m',
                size=1000,
                body={
                    "query": {
                        "bool": {
                            "filter": [
                                {"range": {"@timestamp": {"gte": unquote(str(days))}}}
                            ]
                        }
                    }
                }
            )

            sid = response['_scroll_id']
            scroll_size = len(response['hits']['hits'])
                
            while (scroll_size > 0):
                data.extend(files_response(response))
                response = es.scroll(scroll_id=sid, scroll='2m')
                sid = response['_scroll_id']
                scroll_size = len(response['hits']['hits'])

        except:
            log.info('No index found')

    res = dict(files=data)

    json_file = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=1)

    if extension == "json":
        return json_file
    if extension == "csv":
        x = json.loads(json_file)
        si = StringIO()
        cw = csv.writer(si, delimiter=';')
        cw.writerow(["portal", "path", "timestamp", "extension", "downloads"])
        for y in x["files"]:
            cw.writerow([
                y["portal"],
                y["path"],
                y["timestamp"],
                y["extension"],
                y["downloads"]])

        return si.getvalue()

    return None


def files_response(response):

    res = []

    for hit in response['hits']['hits']:
        browser = {}
        if 'path' in hit["_source"]:
            browser['path'] = hit["_source"]['path']
        if 'extension' in hit["_source"]:
            browser['extension'] = hit["_source"]['extension']
        if 'portal' in hit["_source"]:
            browser['portal'] = hit["_source"]['portal']
        if 'downloads' in hit["_source"]:
            browser['downloads'] = hit["_source"]['downloads']
        if '@timestamp' in hit["_source"]:
            browser['timestamp'] = hit["_source"]['@timestamp']

        res.append(browser)

    return res


def pages_response(response):

    res = []

    for hit in response['hits']['hits']:
        browser = {}
        if 'Url' in hit["_source"]:
            browser['Url'] = hit["_source"]['Url']
        if 'path' in hit["_source"]:
            browser['path'] = hit["_source"]['path']
        if 'portal' in hit["_source"]:
            browser['portal'] = hit["_source"]['portal']
        if 'title' in hit["_source"]:
            browser['title'] = hit["_source"]['title']
        if 'visits' in hit["_source"]:
            browser['visits'] = hit["_source"]['visits']
        if '@timestamp' in hit["_source"]:
            browser['timestamp'] = hit["_source"]['@timestamp']

        res.append(browser)

    return res


def countries_response(response):

    res = []

    for hit in response['hits']['hits']:
        browser = {}
        if 'city' in hit["_source"]:
            browser['city'] = hit["_source"]['city']
        if 'country' in hit["_source"]:
            browser['country'] = hit["_source"]['country']
        if 'portal' in hit["_source"]:
            browser['portal'] = hit["_source"]['portal']
        if 'region' in hit["_source"]:
            browser['region'] = hit["_source"]['region']
        if 'geoip' in hit["_source"]:
            browser['latitude'] = hit["_source"]['geoip']['location']['lat']
            browser['longitude'] = hit["_source"]['geoip']['location']['lon']
        if 'visits' in hit["_source"]:
            browser['visits'] = hit["_source"]['visits']
        if '@timestamp' in hit["_source"]:
            browser['timestamp'] = hit["_source"]['@timestamp']

        res.append(browser)

    return res


def browsers_response(response):

    res = []

    for hit in response['hits']['hits']:
        browser = {}
        if 'platform_name' in hit["_source"]:
            browser['platform_name'] = hit["_source"]['platform_name']
        if 'browser_name' in hit["_source"]:
            browser['browser_name'] = hit["_source"]['browser_name']
        if 'device' in hit["_source"]:
            browser['device'] = hit["_source"]['device']
        if 'portal' in hit["_source"]:
            browser['portal'] = hit["_source"]['portal']
        if 'visits' in hit["_source"]:
            browser['visits'] = hit["_source"]['visits']
        if '@timestamp' in hit["_source"]:
            browser['timestamp'] = hit["_source"]['@timestamp']

        res.append(browser)

    return res
from elasticsearch import Elasticsearch
from urllib.parse import unquote
from io import StringIO
import json
import csv
from app import configuration
import logging
import requests

es = Elasticsearch([configuration.ES_HOST])
log = logging.getLogger('root')
_portals = []

def get_browsers(days, extension, p):
    #log.info("Exporting Browsers - Days: " + days +
    #         ", Extension: " + extension + ", Portal: " + str(p))

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
                     "platform_name", "visits", "device","portal_name"])
        for y in x["browsers"]:
            cw.writerow([
                y["portal"],
                y["timestamp"],
                y["browser_name"],
                y["platform_name"],
                y["visits"],
                y["device"],
                y["portal_name"]])

        return si.getvalue()

    return None


def get_pages(days, extension, p):

    # log.info("Exporting Pages - Days: " + days +
    #          ", Extension: " + extension + ", Portal: " + str(p))

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
        cw.writerow(["portal", "path", "timestamp", "visits", "portal_name"])
        for y in x["pages"]:
            cw.writerow([
                y["portal"],
                y["path"],
                y["timestamp"],
                y["visits"],
                y["portal_name"]])

        return si.getvalue()

    return None


def get_countries(days, extension, p):

    # log.info("Exporting Countries - Days: " + days +
    #          ", Extension: " + extension + ", Portal: " + str(p))
        
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
                     "country", "visits", "portal_name"])
        for y in x["countries"]:
            cw.writerow([
                y["portal"],
                y["timestamp"],
                y["city"],
                y["region"],
                y["country"],
                y["visits"],
                y["portal_name"]])

        return si.getvalue()

    return None


def get_files(days, extension, p):

    # log.info("Exporting Files - Days: " + days +
    #          ", Extension: " + extension + ", Portal: " + str(p))

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
        cw.writerow(["portal", "event_Count","event_Name" ,"timestamp", "portal_name"])
        for y in x["files"]:
            cw.writerow([
                y["portal"],
                y["timestamp"],
                y["event_Count"],
                y["event_Name"],
                y["portal_name"]])

        return si.getvalue()

    return None


def files_response(response):

    res = []

    for hit in response['hits']['hits']:
        browser = {}
        if 'portal' in hit["_source"]:
            browser['portal'] = hit["_source"]['portal']
        if 'event_Count' in hit["_source"]:
            browser['event_Count'] = hit["_source"]['event_Count']
        if '@timestamp' in hit["_source"]:
            browser['timestamp'] = hit["_source"]['@timestamp']
        if 'event_Name' in hit["_source"]:
            browser['event_Name'] = hit["_source"]['event_Name']
        if 'view' in hit["_source"]:
            browser['portal_name'] = get_portal_name(int(hit["_source"]["view"]))

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
        if 'view' in hit["_source"]:
            browser['portal_name'] = get_portal_name(int(hit["_source"]["view"]))

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
        if 'visits' in hit["_source"]:
            browser['visits'] = hit["_source"]['visits']
        if '@timestamp' in hit["_source"]:
            browser['timestamp'] = hit["_source"]['@timestamp']
        if 'view' in hit["_source"]:
            browser['portal_name'] = get_portal_name(int(hit["_source"]["view"]))
        print(browser)
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
        if 'view' in hit["_source"]:
            browser['portal_name'] = get_portal_name(int(hit["_source"]["view"]))

        res.append(browser)

    return res

def get_portals():
    data = requests.get("https://desopendata.aragon.es/aod/services/web/analytics/files")
    for portal in data.json()["message"]:
        _portals.append({"id":portal["view"], "name":portal["portal_name"]})

def get_portal_name(view):
    portal = list(filter(lambda _portal: _portal['id'] == str(view), _portals))
    if portal:
        return portal[0]["name"]
    else:
        get_portals()
        portal = list(filter(lambda portal: portal['id'] == str(view), _portals))
        if portal:
            return portal[0]["name"]
        else:
            return None
        

get_portals()

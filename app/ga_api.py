from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
from app import configuration
import logging
import json

log = logging.getLogger('root')

def process_response(response):
    res_list = list()
    for rowIdx, row in enumerate(response.rows):
        res_row = dict()
        for i, dimension_value in enumerate(row.dimension_values):
            dimension_name = response.dimension_headers[i].name
            res_row[dimension_name] = dimension_value.value
        for i, metric_value in enumerate(row.metric_values):
            metric_name = response.metric_headers[i].name
            res_row[metric_name] = metric_value.value
        res_list.append(res_row)

    res_list
    return res_list

def get_credentials():
    credentials = service_account.Credentials.from_service_account_file(
        configuration.GA_KEY)
    client = BetaAnalyticsDataClient(
        credentials=credentials
    )
    return client
    
def get_pages(property_id, date):
    log.info('Get_Pages - Property:' + property_id + ", Date: " +
             str(date.strftime('%Y-%m-%d')))
    res = []
    service = get_credentials()
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="hostname"),
            Dimension(name="pagePath"),
            Dimension(name="pageTitle"),
        ],
        metrics=[
            Metric(name="sessions")
        ],
        date_ranges=[
            DateRange(
                start_date  = str(date.strftime('%Y-%m-%d')), 
                end_date    = str(date.strftime('%Y-%m-%d'))
                )
        ],
    )
    response = service.run_report(request)
    result = process_response(response)
    res.append(dict(report=result))
    return json.dumps(dict(reports=res), ensure_ascii=False, sort_keys=True, indent=1)

def get_browsers(property_id, date):
    log.info('Get_Browsers - Property:' + property_id + ", Date: " +
             str(date.strftime('%Y-%m-%d')))
    res = []
    service = get_credentials()
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="browser"),
            Dimension(name="operatingSystem"),
            Dimension(name="deviceCategory")
        ],
        metrics=[
            Metric(name="sessions")
        ],
        date_ranges=[
            DateRange(
                start_date  = str(date.strftime('%Y-%m-%d')), 
                end_date    = str(date.strftime('%Y-%m-%d'))
                )
        ],
    )
    response = service.run_report(request)
    result = process_response(response)
    res.append(dict(report=result))
    return json.dumps(dict(reports=res), ensure_ascii=False, sort_keys=True, indent=1)

def get_countries(property_id, date):
    log.info('Get_Countries - Property:' + property_id + ", Date: " +
             str(date.strftime('%Y-%m-%d')))
    res = []
    service = get_credentials()
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="continent"),
            # Dimension(name="subcontinent"),
            Dimension(name="country"),
            Dimension(name="region"),
            Dimension(name="city"),
            # Dimension(name="latitude"),
            # Dimension(name="longitude")

        ],
        metrics=[
            Metric(name="sessions")
        ],
        date_ranges=[
            DateRange(
                start_date  = str(date.strftime('%Y-%m-%d')), 
                end_date    = str(date.strftime('%Y-%m-%d'))
                )
        ],
    )
    response = service.run_report(request)
    result = process_response(response)
    res.append(dict(report=result))
    return json.dumps(dict(reports=res), ensure_ascii=False, sort_keys=True, indent=1)

def get_files(property_id, date):
    log.info('Get_Pages - Property:' + property_id + ", Date: " +
             str(date.strftime('%Y-%m-%d')))
    res = []
    service = get_credentials()
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            # Dimension(name="eventCategory"),
            # Dimension(name="eventAction"),
            # Dimension(name="eventLabel")
            Dimension(name="eventName"), #nueva
        ],
        metrics=[
            # Metric(name="totalEvents")
            Metric(name="eventCount")

        ],
        date_ranges=[
            DateRange(
                start_date  = str(date.strftime('%Y-%m-%d')), 
                end_date    = str(date.strftime('%Y-%m-%d'))
                )
        ],
    )
    response = service.run_report(request)
    result = process_response(response)
    res.append(dict(report=result))
    return json.dumps(dict(reports=res), ensure_ascii=False, sort_keys=True, indent=1)


# -*- coding: utf-8 -*- #
"""
@created: 21/11/2019
@author: Julio Lafuente
@author: DxD
@version: 1.0
"""

import sys
from datetime import datetime, timedelta
from flask import make_response
from flask import Flask
from flask import request
from app import configuration
from app import export_api
from app import urchin_api
from app import ga_api
from app import logger

log = logger.setup_custom_logger('root')
APP = Flask(__name__)

if configuration.ENVIRONMENT == 'DEV':
    APP.env = 'development'
    APP.debug = 1


def common_headers(res):
    res.headers['Access-Control-Allow-Headers'] = "*"
    res.headers['Access-Control-Allow-Origin'] = "*"
    res.headers['Access-Control-Allow-Methods'] = "GET"

    return res


@APP.route('/browsers_ga')
def run_browsers_ga():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        ga_api.get_browsers(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/countries_ga')
def run_countries_ga():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        ga_api.get_countries(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/files_ga')
def run_files_ga():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        ga_api.get_files(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/pages_ga')
def run_pages_ga():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        ga_api.get_pages(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/browsers_urchin')
def run_browsers_urchin():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        urchin_api.get_browsers(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/countries_urchin')
def run_countries_urchin():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        urchin_api.get_countries(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/files_urchin')
def run_files_urchin():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        urchin_api.get_files(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/pages_urchin')
def run_pages_urchin():

    view = request.args.get("view")
    delay = request.args.get("delay")
    date = request.args.get("date")

    if delay is not None:
        date = datetime.today() - timedelta(days=int(delay))
    else:
        if date is not None:
            date = datetime.fromtimestamp(int(date))
        else:
            log.warn("No se ha informado de la fecha")
            return "No se ha informado de la fecha"

    if view is None:
        log.warn("No se ha informado la ID de la vista")
        return "No se ha informado la ID de la vista"

    res = make_response(
        urchin_api.get_pages(view, date)
    )

    res.headers['Custom-Date'] = str(date.strftime('%Y-%m-%d'))
    res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    res = common_headers(res)

    return res


@APP.route('/export_browsers')
def run_export_browsers():

    days = request.args.get("days")
    extension = request.args.get("extension")
    portal = request.args.getlist("portal")

    if days is None:
        log.warn("No se ha informado del número de días")
        return "No se ha informado del número de días"

    if not portal:
        log.info("No se ha informado del campo portal, se usa portal=* por defecto")
        portal = '*'

    res = make_response(
        export_api.get_browsers(days, extension, portal)
    )

    fileName = "Navegadores"
    res.headers['Content-Disposition'] = "attachment; filename=\"" + \
        fileName + "." + extension + "\""
    if extension == "json":
        res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    if extension == "csv":
        res.headers['Content-Type'] = 'text/csv; charset=UTF-8'

    res = common_headers(res)

    return res


@APP.route('/export_files')
def run_export_files():

    days = request.args.get("days")
    extension = request.args.get("extension")
    portal = request.args.getlist("portal")

    if days is None:
        log.warn("No se ha informado del número de días")
        return "No se ha informado del número de días"

    if not portal:
        log.info("No se ha informado del campo portal, se usa portal=* por defecto")
        portal = '*'

    res = make_response(
        export_api.get_files(days, extension, portal)
    )

    fileName = "Archivos"
    res.headers['Content-Disposition'] = "attachment; filename=\"" + \
        fileName + "." + extension + "\""
    if extension == "json":
        res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    if extension == "csv":
        res.headers['Content-Type'] = 'text/csv; charset=UTF-8'

    res = common_headers(res)

    return res


@APP.route('/export_pages')
def run_export_pages():

    days = request.args.get("days")
    extension = request.args.get("extension")
    portal = request.args.getlist("portal")
    if days is None:
        log.warn("No se ha informado del número de días")
        return "No se ha informado del número de días"

    if not portal:
        log.info("No se ha informado del campo portal, se usa portal=* por defecto")
        portal = '*'

    res = make_response(
        export_api.get_pages(days, extension, portal)
    )

    fileName = "Paginas"
    res.headers['Content-Disposition'] = "attachment; filename=\"" + \
        fileName + "." + extension + "\""
    if extension == "json":
        res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    if extension == "csv":
        res.headers['Content-Type'] = 'text/csv; charset=UTF-8'

    res = common_headers(res)

    return res


@APP.route('/export_countries')
def run_export_countries():

    days = request.args.get("days")
    extension = request.args.get("extension")
    portal = request.args.getlist("portal")

    if days is None:
        log.warn("No se ha informado del número de días")
        return "No se ha informado del número de días"

    if not portal:
        log.info("No se ha informado del campo portal, se usa portal=* por defecto")
        portal = '*'

    res = make_response(
        export_api.get_countries(days, extension, portal)
    )

    fileName = "Localizaciones"
    res.headers['Content-Disposition'] = "attachment; filename=\"" + \
        fileName + "." + extension + "\""
    if extension == "json":
        res.headers['Content-Type'] = 'application/json; charset=UTF-8'
    if extension == "csv":
        res.headers['Content-Type'] = 'text/csv; charset=UTF-8'

    res = common_headers(res)

    return res


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=50053)

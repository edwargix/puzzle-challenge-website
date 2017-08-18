# -*- coding: utf-8 -*-
"""Template Helpers used in puzzlesweb."""
import logging
from markupsafe import Markup
from datetime import datetime
import tg
import markdown as md

log = logging.getLogger(__name__)

def current_year():
    now = datetime.now()
    return now.strftime('%Y')

def markdown(*args, strip_par=False, **kwargs):
    res = md.markdown(*args, **kwargs)
    if strip_par:
        res = res.replace('<p>', '').replace('</p>', '')
    return Markup(res)

def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)

def ftime(datetime_obj, show_day=False):
    day_fmt = '{0:%A}, ' if show_day else ''
    date_fmt = '{0.day} {0:%B %Y}'
    time_fmt = '{0:%-I}:{0:%M} {0:%p}'
    if isinstance(datetime_obj, datetime):
        return (day_fmt + date_fmt + ' at ' + time_fmt).format(datetime_obj)
    if isinstance(datetime_obj, date):
        return (day_fmt + date_fmt).format(datetime_obj)
    if isinstance(datetime_obj, time):
        return (time_fmt).format(datetime_obj)

# Import commonly used helpers from WebHelpers2 and TG
from tg.util.html import script_json_encode

try:
    from webhelpers2 import date, html, number, misc, text
except SyntaxError:
    log.error("WebHelpers2 helpers not available with this Python Version")

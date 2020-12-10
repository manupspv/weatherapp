from django import template
from datetime import datetime, tzinfo
import pytz
from pytz import timezone

register = template.Library()

@register.filter
def get_date(datentime,tzone):

    timestamp = datentime
    # tzone = "Asia/Kolkata"
    dt = datetime.fromtimestamp(timestamp).astimezone(pytz.timezone(tzone))
    
    return dt.strftime("%b-%d-%Y %I:%M %p")


@register.filter
def get_day(datentime,tzone):

    timestamp = datentime
    dt = datetime.fromtimestamp(timestamp).astimezone(pytz.timezone(tzone))
    
    return dt.strftime("%d-%b")


@register.filter
def get_time(datentime,tzone):

    timestamp = datentime
    dt = datetime.fromtimestamp(timestamp).astimezone(pytz.timezone(tzone))
    
    return dt.strftime("%I:%M %p")


@register.filter
def celsius(temp):

    temperature = temp - 273.15
    
    return  temperature




# dt = datetime.fromtimestamp(1604915352).astimezone(pytz.timezone('Asia/Kolkata'))
# tz = pytz.timezone("Asia/Kolkata")

# dtobject = datetime.strptime(dt,"%Y-%b-%d %H:%M:%S")

# print(dtobject)


# print(dt.strftime("%I  %p"))
# print(dt.tzinfo)

# print(dt)













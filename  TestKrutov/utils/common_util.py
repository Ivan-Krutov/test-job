import dateparser
import re


DUE_DATE = [
    {
        'неделя': '0_0_ЕХТRА_0'
    },
    {
        'недели': '0_0_ЕХТRА_0'
    },
    {
        'недель': '0_0_ЕХТRА_0'
    },
    {
        'день': '0_0_0_ЕХТRА'
    },
    {
        'дня': '0_0_0_ЕХТRА'
    },
    {
        'дней': '0_0_0_ЕХТRА'
    },
    {
        'год': 'ЕХТRА_0_0_0'
    },
    {
        'года': 'ЕХТRА_0_0_0'
    },
    {
        'лет': 'ЕХТRА_0_0_0'
    },
    {
        'месяц': '0_ЕХТRА_0_0'
    },
    {
        'месяца': '0_ЕХТRА_0_0'
    },
    {
        'месяцев': '0_ЕХТRА_0_0'
    }
]


def normalize_date(date):
    result = dateparser.parse(date).strftime("%d.%m.%Y")
    return result


def normalize_due_date(string):
    for count, i in enumerate(DUE_DATE):
        key = list(i.keys())[0]
        if string.find(key) > 0:
            return DUE_DATE[count][key].replace('ЕХТRА', re.findall(r'\b\d+\b', string[0])[0])
    return string

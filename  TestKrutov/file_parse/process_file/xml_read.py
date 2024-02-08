import pandas as pd
from typing import Dict
from utils.common_util import normalize_date, normalize_due_date


async def read_xml_file(file_path) -> Dict:
    data = pd.read_xml(file_path).to_dict('list')
    if data.get('ДатаДокумента'):
        for count, i in enumerate(data['ДатаДокумента']):
            data['ДатаДокумента'][count] = normalize_date(data['ДатаДокумента'][count])
    if data.get('Оплата'):
        for count, v in enumerate(data['Оплата']):
            data['Оплата'][count] = normalize_due_date(data['Оплата'][count])

    response_data = {
        "file": file_path,
        "content": data
    }
    return response_data

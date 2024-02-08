import json

from typing import Dict
from utils.common_util import normalize_date, normalize_due_date


async def read_json_file(file_path) -> Dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if data.get('ДатаДокумента'):
            data['ДатаДокумента'] = normalize_date(data['ДатаДокумента'])

        if data.get('Оплата'):
            data['Оплата'] = normalize_due_date(data['Оплата'])

        response_data = {
            "file": file_path,
            "content": data
        }
    return response_data
import json
from typing import Dict


def nullify(dic: Dict) -> Dict:
    return {k: v for k, v in dic.items() if v is not None}


def to_nullified_json(dic: Dict) -> str:
    return json.dumps(nullify(dic))

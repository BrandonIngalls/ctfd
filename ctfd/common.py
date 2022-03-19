from typing import Any, Dict, Optional


def build_param_dict(**kwargs: Any) -> Optional[Dict[str, str]]:
    result: Dict[str, str] = {}
    for key, value in kwargs.items():
        if value is None:
            continue
        result[key] = value
    return result if result else None

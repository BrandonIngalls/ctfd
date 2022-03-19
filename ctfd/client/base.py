from typing import Dict, Optional

from . import utils
from .api_result import APIResult


class CTFd:
    def get(self, uri: str, /, *, params: Optional[Dict[str, str]] = None) -> APIResult:
        url = f"{self._host}/api/v1{uri}"

        response = self._session.get(url, params=params)
        data = response.json()

        return APIResult.parse_obj(data)

    def __init__(self, host: str, token: str, /, *, verify_tls: bool = True) -> None:
        self._host = host
        self._session = utils.create_session(verify_tls=verify_tls, token=token)

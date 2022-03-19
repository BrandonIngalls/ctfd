from typing import Dict, Optional, Protocol

from .api_result import APIResult


class IClient(Protocol):
    def get(self, uri: str, /, *, params: Optional[Dict[str, str]] = None) -> APIResult:
        ...

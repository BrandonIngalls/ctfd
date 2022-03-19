from typing import Protocol

import requests


class IClient(Protocol):
    _session: requests.Session

from . import utils


class CTFd:
    def __init__(self, host: str, token: str, /, *, verify_tls: bool = True) -> None:
        self._host = host
        self._session = utils.create_session(verify_tls=verify_tls, token=token)

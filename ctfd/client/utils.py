import requests

from ctfd.version import VERSION


def create_session(
    *, verify_tls: bool, token: str, version: str = VERSION
) -> requests.Session:
    session = requests.Session()

    session.verify = verify_tls

    session.headers.update({"Content-Type": "application/json"})
    session.headers.update({"Authorization": f"token {token}"})
    session.headers.update({"User-Agent": f"Python CTFd Library v{version}"})

    return session

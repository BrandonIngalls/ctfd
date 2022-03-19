from ctfd.client.protos import IClient


class SubmissionsClient:
    def __init__(self, client: IClient, /) -> None:
        self._client = client

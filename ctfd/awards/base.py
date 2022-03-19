from ctfd.client.protos import IClient


class AwardsClient:
    def __init__(self, client: IClient, /) -> None:
        self._client = client

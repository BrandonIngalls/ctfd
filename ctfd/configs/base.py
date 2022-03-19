from typing import List, Optional

from ctfd import common
from ctfd.client.protos import IClient

from .models import ConfigItem


class ConfigsClient:
    def get(
        self,
        *,
        key: Optional[str] = None,
        value: Optional[str] = None,
        q: Optional[str] = None,
        field: Optional[str] = None,
    ) -> List[ConfigItem]:
        params = common.build_param_dict(key=key, value=value, q=q, field=field)

        result = self._client.get("/configs", params=params)
        config_item_list = result.data

        return [ConfigItem.parse_obj(item) for item in config_item_list]

    def by_key(self, key_name: str, /) -> Optional[ConfigItem]:
        items = self.get(key=key_name)
        if not items:
            return None

        if len(items) > 1:
            raise RuntimeError(f"more than one config items with key=={key_name}")

        return items[0]

    def __init__(self, client: IClient, /) -> None:
        self._client = client

from typing import Optional

from pydantic import BaseModel


class ConfigItem(BaseModel):
    id: int
    key: str
    value: Optional[str]

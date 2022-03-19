from typing import Any, Dict, List, Union

from pydantic import BaseModel

ResultDict = Dict[str, Any]


class APIResult(BaseModel):
    success: bool
    data: Union[ResultDict, List[ResultDict]]

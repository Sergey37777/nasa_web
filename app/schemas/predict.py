from typing import Any, List, Optional

from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    preds: Optional[List[int]]
    probs: Optional[List[float]]



from typing import List, Optional

from pydantic import BaseModel


class MetarText(BaseModel):
    metar_text: str
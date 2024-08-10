

from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class SchoolType(Enum):
    PRIVATE = "private"
    PUBLIC = "public"


class School(BaseModel):
    name: str
    img: str
    address: str 
    category: SchoolType
    description: Optional[str] = None
    city: str
    
class SchoolList(BaseModel):
    schools: List[School]
from typing import Optional
import uuid;
from pydantic import BaseModel, Field

#This model maintains the list of list items
class ListModel(BaseModel):
    id:str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str
    description: str

#This model updates the list items
class ListUpdateModel(BaseModel):
    title: Optional[str]
    description: Optional[str]

    
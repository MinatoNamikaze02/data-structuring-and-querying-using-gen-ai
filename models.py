from pydantic import BaseModel, constr, validator
from datetime import datetime
from typing import List, Optional

class FilmRecord(BaseModel):
    date: datetime
    box_office_collection: int
    notes: Optional[constr(strip_whitespace=True)] = None

    @validator('date', pre=True)
    def parse_date(cls, value):
        #format January 8, 2023
        return datetime.strptime(value, '%B %d, %Y')
    
class Film(BaseModel):
    title: constr(strip_whitespace=True)
    records: List[FilmRecord]

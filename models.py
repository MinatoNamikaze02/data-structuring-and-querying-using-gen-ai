from pydantic import BaseModel, constr, validator
from datetime import datetime
from typing import List, Optional

    
class Film(BaseModel):
    title: constr(strip_whitespace=True)
    dates: List[datetime]
    box_office_collections: List[constr(strip_whitespace=True)]

    @validator('dates', pre=True)
    def parse_dates(cls, value):
        # 2023-01-08
        return [datetime.strptime(date, '%Y-%m-%d') for date in value]
    
    @validator('box_office_collections', pre=True)
    def parse_box_office_collections(cls, value):
        return [str(collection) for collection in value]

    @classmethod
    def to_dict(self):
        return {
            "title": self.title,
            "dates": self.dates,
            "box_office_collections": self.box_office_collections
        }
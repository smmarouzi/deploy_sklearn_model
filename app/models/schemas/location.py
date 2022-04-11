from pydantic import BaseModel, conlist
from typing import List, Any

class Location(BaseModel):
    x_coord: float 
    y_coord: float
    
    @staticmethod
    def from_dict(obj):
        return Location(x_coord=obj['x_coord'], y_coord=obj['y_coord'])

    @staticmethod
    def default():
        return Location(x_coord=0.5, y_coord=0.5) 
    
    def to_dict(self):
        return self.dict()
    
class LocationList(BaseModel):
    data: List[conlist(float, min_items=2, max_items=2)]
    
class LocationPredictionResponse(BaseModel):
    prediction: List[int]
    probability: List[Any]
    log_probability: List[Any]
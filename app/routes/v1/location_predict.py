from fastapi import APIRouter
from app.models.schemas.location import Location, LocationList, LocationPredictionResponse
import app.models.ml.classifier as clf

app_location_predict_v1 = APIRouter()
@app_location_predict_v1.post('/location/predict',
                             tags=["predictions"],
                             response_model = LocationPredictionResponse,
                             description = "Get a location classification from x and y coordinations")

async def getpredictions(loc: LocationList):
    data = dict(loc)['data']
    prediction = clf.model.predict(data).tolist()
    probability = clf.model.predict_proba(data).tolist()
    log_probability = clf.model.predict_log_proba(data).tolist()
    return {"prediction": prediction,
            "probability": probability,
            "log_probability": log_probability}
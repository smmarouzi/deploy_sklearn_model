import app.models.ml.classifier as clf
from fastapi import FastAPI
from joblib import load
from app.routes.v1.location_predict import app_location_predict_v1
from app.routes.home import app_home


app = FastAPI(title="Location ML API", description="API for location prediction from x and y coordinations", version="1.0")


@app.on_event('startup')
async def load_model():
    clf.model = load('app/models/ml/logistic_regression_v1.pkl')
    print(clf.model)


app.include_router(app_home)
app.include_router(app_location_predict_v1, prefix='/v1')

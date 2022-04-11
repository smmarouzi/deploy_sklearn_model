import json
import requests

def prediction_request(input_list):
    """
    receives array of input values and returns list of predicted values
    Args:
        input_list (list(list)): list of input variables list [[x_coord1, y_coord1], ..., [x_coordn, y_coordn]]
    returns:
        predictions (list): list of predicted values for each input
    """
    f = requests.Session()

    endpoint = 'https://sonova-api-4ivksk4oza-pd.a.run.app/v1/location/predict'
    body = {"data": input_list}
    headers = {'content-type': 'application/json'}

    get_data = f.post(endpoint, json=body, timeout=30, headers=headers, verify=False)
    predictions = get_data.json()["prediction"]
    return predictions
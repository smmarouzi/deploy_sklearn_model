from locust import HttpUser, TaskSet, task, between, tag

"""
Run locus with:
locust -f ./tests/load_test.py
"""


class LocationPredict(TaskSet):
    @tag('Predictions')
    @task
    def predict(self):
        request_body = {"data": [[0.54, 0.32]]}
        self.client.post('/v1/location/predict', json=request_body)

    @tag('Baseline')
    @task
    def health_check(self):
        self.client.get('/')


class LocationLoadTest(HttpUser):
    tasks = [LocationPredict]
    host = 'http://0.0.0.0'
    stop_timeout = 200
    wait_time = between(1, 5)
from locust import HttpUser, task, between

class APILoadTester(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def high_volume_request(self):
        self.client.get("/item")

    @task
    def low_volume_request(self):
        self.client.get("/item/xpto")

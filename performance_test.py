from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def search_product(self):
        self.client.get("/search", params={"query": "Titan watch"})

    @task
    def add_to_cart(self):
        self.client.post("/add-to-cart", json={"productId": 1})

    @task
    def buy_now(self):
        self.client.post("/buy-now")

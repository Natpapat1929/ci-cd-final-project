from unittest import TestCase
from service import app


class TestCounterRoutes(TestCase):
    """Tests for the counter service routes"""

    def setUp(self):
        self.client = app.test_client()

    def test_health(self):
        """It should return a healthy status"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["status"], "OK")

    def test_index(self):
        """It should return the index page"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_counter_lifecycle(self):
        """It should create, read, update and delete a counter"""
        name = "foo"
        resp = self.client.post(f"/counters/{name}")
        self.assertEqual(resp.status_code, 201)
        resp = self.client.post(f"/counters/{name}")
        self.assertEqual(resp.status_code, 409)
        resp = self.client.put(f"/counters/{name}")
        self.assertEqual(resp.get_json()[name], 1)
        resp = self.client.get(f"/counters/{name}")
        self.assertEqual(resp.status_code, 200)
        resp = self.client.delete(f"/counters/{name}")
        self.assertEqual(resp.status_code, 204)
        resp = self.client.get(f"/counters/{name}")
        self.assertEqual(resp.status_code, 404)
        resp = self.client.put(f"/counters/{name}")
        self.assertEqual(resp.status_code, 404)

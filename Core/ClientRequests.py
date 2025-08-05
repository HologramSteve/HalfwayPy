import requests

# Some base data
apiVersion = "10"
baseUrl = "https://discord.com/api/v" + apiVersion 

class ClientRequests:
    def __init__(self, token):
        self.token = token

    def _make_url(self, endpoint):
        return f"{baseUrl}/{endpoint.lstrip('/')}"

    def _make_headers(self, headers=None):
        req_headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }
        if headers:
            req_headers.update(headers)
        return req_headers

    def get(self, endpoint, params=None, headers=None):
        url = self._make_url(endpoint)
        req_headers = self._make_headers(headers)
        response = requests.get(url, headers=req_headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None, headers=None):
        url = self._make_url(endpoint)
        req_headers = self._make_headers(headers)
        response = requests.post(url, headers=req_headers, json=data)
        response.raise_for_status()
        return response.json()

    def patch(self, endpoint, data=None, headers=None):
        url = self._make_url(endpoint)
        req_headers = self._make_headers(headers)
        response = requests.patch(url, headers=req_headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint, headers=None):
        url = self._make_url(endpoint)
        req_headers = self._make_headers(headers)
        response = requests.delete(url, headers=req_headers)
        response.raise_for_status()
        return True
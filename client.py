from pydantic import BaseModel


class LazopClient(BaseModel):
    url: str = "https://auth.lazada.com/rest"
    appkey: str = "118458"
    appSecret: str = "aWAppvLaHEqBYFlacDcY7TFnlk68rYpX"


class LazopClientRequest(BaseModel):
    url: str
    method: str = "GET"
    api_params: dict = {}

    def add_api_param(self, key, value):
        """Adds an API parameter."""
        self.api_params[key] = value
import json
from flask import make_response

class ApiResponse():
  def __init__(self, data: list, error: str) -> None:
      self.data = data
      self.error = error

  def to_json(self):
    return json.dumps(self, default=lambda obj: obj.__dict__)

  @staticmethod
  def success(data: list):
    result = ApiResponse(data=data, error=None).to_json()
    return make_response(result, 200, { "Content-Type": "application/json" })

  @staticmethod
  def failure(error: str):
    result = ApiResponse(data=None, error=error).to_json()
    return make_response(result, 200, { "Content-Type": "application/json" })

  @staticmethod
  def unauthorized():
    result = ApiResponse(data=None, error="Unauthorized").to_json()
    return make_response(result, 401, { "Content-Type": "application/json" })
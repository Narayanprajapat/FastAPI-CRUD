from enum import Enum


class ResponseMessages(Enum):
    Success = "Success"
    InternalServerError = "Internal Server Error"
    BadRequest = "Bad Request"

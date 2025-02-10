from request_generator.base_request import BaseRequest
from request_generator.request_type import RequestType


class RollDiceRequest(BaseRequest):
    def __init__(self):
        self.protocolNumber = RequestType.ROLL_DICE.value

    def toDictionary(self):
        return {"protocolNumber": self.protocolNumber}

    def __str__(self):
        return f"RollDiceRequest(protocolNumber={self.protocolNumber})"
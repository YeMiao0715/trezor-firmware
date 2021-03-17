# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class VerifyMessage(p.MessageType):
    MESSAGE_WIRE_TYPE = 39

    def __init__(
        self,
        *,
        address: str,
        signature: bytes,
        message: bytes,
        coin_name: str = "Bitcoin",
    ) -> None:
        self.address = address
        self.signature = signature
        self.message = message
        self.coin_name = coin_name

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address', p.UnicodeType, p.FLAG_REQUIRED),
            2: ('signature', p.BytesType, p.FLAG_REQUIRED),
            3: ('message', p.BytesType, p.FLAG_REQUIRED),
            4: ('coin_name', p.UnicodeType, "Bitcoin"),  # default=Bitcoin
        }

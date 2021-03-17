# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TxAckPrevInputWrapper import TxAckPrevInputWrapper

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckPrevInput(p.MessageType):
    MESSAGE_WIRE_TYPE = 22

    def __init__(
        self,
        *,
        tx: TxAckPrevInputWrapper,
    ) -> None:
        self.tx = tx

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('tx', TxAckPrevInputWrapper, p.FLAG_REQUIRED),
        }

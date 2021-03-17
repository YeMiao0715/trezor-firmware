# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroLiveRefreshStepAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 555

    def __init__(
        self,
        *,
        salt: Optional[bytes] = None,
        key_image: Optional[bytes] = None,
    ) -> None:
        self.salt = salt
        self.key_image = key_image

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('salt', p.BytesType, None),
            2: ('key_image', p.BytesType, None),
        }

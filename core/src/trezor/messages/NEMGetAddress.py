# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMGetAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 67

    def __init__(
        self,
        *,
        address_n: Optional[List[int]] = None,
        network: Optional[int] = None,
        show_display: Optional[bool] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.network = network
        self.show_display = show_display

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('network', p.UVarintType, None),
            3: ('show_display', p.BoolType, None),
        }

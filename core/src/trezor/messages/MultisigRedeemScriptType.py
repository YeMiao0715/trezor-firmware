# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .HDNodePathType import HDNodePathType
from .HDNodeType import HDNodeType

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MultisigRedeemScriptType(p.MessageType):

    def __init__(
        self,
        *,
        m: int,
        pubkeys: Optional[List[HDNodePathType]] = None,
        signatures: Optional[List[bytes]] = None,
        nodes: Optional[List[HDNodeType]] = None,
        address_n: Optional[List[int]] = None,
    ) -> None:
        self.pubkeys = pubkeys if pubkeys is not None else []
        self.signatures = signatures if signatures is not None else []
        self.nodes = nodes if nodes is not None else []
        self.address_n = address_n if address_n is not None else []
        self.m = m

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('pubkeys', HDNodePathType, p.FLAG_REPEATED),
            2: ('signatures', p.BytesType, p.FLAG_REPEATED),
            3: ('m', p.UVarintType, p.FLAG_REQUIRED),
            4: ('nodes', HDNodeType, p.FLAG_REPEATED),
            5: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        }

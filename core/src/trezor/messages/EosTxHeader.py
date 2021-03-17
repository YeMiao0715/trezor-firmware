# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosTxHeader(p.MessageType):

    def __init__(
        self,
        *,
        expiration: int,
        ref_block_num: int,
        ref_block_prefix: int,
        max_net_usage_words: int,
        max_cpu_usage_ms: int,
        delay_sec: int,
    ) -> None:
        self.expiration = expiration
        self.ref_block_num = ref_block_num
        self.ref_block_prefix = ref_block_prefix
        self.max_net_usage_words = max_net_usage_words
        self.max_cpu_usage_ms = max_cpu_usage_ms
        self.delay_sec = delay_sec

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('expiration', p.UVarintType, p.FLAG_REQUIRED),
            2: ('ref_block_num', p.UVarintType, p.FLAG_REQUIRED),
            3: ('ref_block_prefix', p.UVarintType, p.FLAG_REQUIRED),
            4: ('max_net_usage_words', p.UVarintType, p.FLAG_REQUIRED),
            5: ('max_cpu_usage_ms', p.UVarintType, p.FLAG_REQUIRED),
            6: ('delay_sec', p.UVarintType, p.FLAG_REQUIRED),
        }

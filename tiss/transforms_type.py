from dataclasses import dataclass, field
from typing import List

from tiss.transform import Transform

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class TransformsType:
    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )

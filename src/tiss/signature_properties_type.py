from dataclasses import dataclass, field
from typing import List, Optional

from tiss.signature_property import SignatureProperty

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignaturePropertiesType:
    signature_property: List[SignatureProperty] = field(
        default_factory=list,
        metadata={
            "name": "SignatureProperty",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )

from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class ObjectType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Attribute",
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )

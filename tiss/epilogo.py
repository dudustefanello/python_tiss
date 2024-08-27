from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class Epilogo:
    class Meta:
        name = "epilogo"

    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

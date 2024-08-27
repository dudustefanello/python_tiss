from dataclasses import dataclass, field
from typing import Optional

from tiss.st_tiss_fault import StTissFault

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class TissFaultWs:
    class Meta:
        name = "tissFaultWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    tiss_fault: Optional[StTissFault] = field(
        default=None,
        metadata={
            "name": "tissFault",
            "type": "Element",
            "required": True,
        },
    )

from dataclasses import dataclass, field
from typing import Optional

from tiss.cancela_guia_ws import CancelaGuiaWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissCancelaGuiaPortTypeTissCancelaGuiaOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissCancelaGuiaPortTypeTissCancelaGuiaOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        cancela_guia_ws: Optional[CancelaGuiaWs] = field(
            default=None,
            metadata={
                "name": "cancelaGuiaWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
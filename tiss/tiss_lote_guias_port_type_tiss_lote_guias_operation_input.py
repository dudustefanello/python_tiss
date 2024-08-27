from dataclasses import dataclass, field
from typing import Optional

from tiss.lote_guias_ws import LoteGuiasWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissLoteGuiasPortTypeTissLoteGuiasOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["TissLoteGuiasPortTypeTissLoteGuiasOperationInput.Body"] = (
        field(
            default=None,
            metadata={
                "name": "Body",
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        lote_guias_ws: Optional[LoteGuiasWs] = field(
            default=None,
            metadata={
                "name": "loteGuiasWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

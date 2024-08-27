from dataclasses import dataclass, field
from typing import Optional

from tiss.lote_anexo_ws import LoteAnexoWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissLoteAnexoPortTypeTissLoteAnexoOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["TissLoteAnexoPortTypeTissLoteAnexoOperationInput.Body"] = (
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
        lote_anexo_ws: Optional[LoteAnexoWs] = field(
            default=None,
            metadata={
                "name": "loteAnexoWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

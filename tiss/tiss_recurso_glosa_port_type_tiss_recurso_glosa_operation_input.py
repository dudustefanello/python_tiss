from dataclasses import dataclass, field
from typing import Optional

from tiss.lote_recurso_glosa_ws import LoteRecursoGlosaWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissRecursoGlosaPortTypeTissRecursoGlosaOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissRecursoGlosaPortTypeTissRecursoGlosaOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        lote_recurso_glosa_ws: Optional[LoteRecursoGlosaWs] = field(
            default=None,
            metadata={
                "name": "loteRecursoGlosaWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

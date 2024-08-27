from dataclasses import dataclass, field
from typing import Optional

from tiss.solicitacao_status_recurso_glosa_ws import (
    SolicitacaoStatusRecursoGlosaWs,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        solicitacao_status_recurso_glosa_ws: Optional[
            SolicitacaoStatusRecursoGlosaWs
        ] = field(
            default=None,
            metadata={
                "name": "solicitacaoStatusRecursoGlosaWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

from dataclasses import dataclass, field
from typing import Optional

from tiss.solicitacao_status_autorizacao_ws import (
    SolicitacaoStatusAutorizacaoWs,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        solicitacao_status_autorizacao_ws: Optional[
            SolicitacaoStatusAutorizacaoWs
        ] = field(
            default=None,
            metadata={
                "name": "solicitacaoStatusAutorizacaoWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

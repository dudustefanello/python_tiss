from dataclasses import dataclass, field
from typing import Optional

from tiss.solicitacao_status_protocolo_ws import SolicitacaoStatusProtocoloWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        solicitacao_status_protocolo_ws: Optional[
            SolicitacaoStatusProtocoloWs
        ] = field(
            default=None,
            metadata={
                "name": "solicitacaoStatusProtocoloWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

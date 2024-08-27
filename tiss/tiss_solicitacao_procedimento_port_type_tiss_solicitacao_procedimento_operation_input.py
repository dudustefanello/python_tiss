from dataclasses import dataclass, field
from typing import Optional

from tiss.solicitacao_procedimento_ws import SolicitacaoProcedimentoWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        solicitacao_procedimento_ws: Optional[SolicitacaoProcedimentoWs] = (
            field(
                default=None,
                metadata={
                    "name": "solicitacaoProcedimentoWS",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
        )

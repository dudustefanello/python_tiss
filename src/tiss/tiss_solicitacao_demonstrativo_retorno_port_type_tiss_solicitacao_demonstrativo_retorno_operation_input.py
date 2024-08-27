from dataclasses import dataclass, field
from typing import Optional

from tiss.solicitacao_demonstrativo_retorno_ws import (
    SolicitacaoDemonstrativoRetornoWs,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        solicitacao_demonstrativo_retorno_ws: Optional[
            SolicitacaoDemonstrativoRetornoWs
        ] = field(
            default=None,
            metadata={
                "name": "solicitacaoDemonstrativoRetornoWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

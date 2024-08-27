from dataclasses import dataclass, field
from typing import Optional

from tiss.pedido_elegibilidade_ws import PedidoElegibilidadeWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        pedido_elegibilidade_ws: Optional[PedidoElegibilidadeWs] = field(
            default=None,
            metadata={
                "name": "pedidoElegibilidadeWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

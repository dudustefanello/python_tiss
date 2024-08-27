from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_elegibilidade_verifica import CtElegibilidadeVerifica
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class PedidoElegibilidadeWs:
    """
    Prestador solicita elegibilidade do paciente.
    """

    class Meta:
        name = "pedidoElegibilidadeWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    pedido_elegibilidade: Optional[CtElegibilidadeVerifica] = field(
        default=None,
        metadata={
            "name": "pedidoElegibilidade",
            "type": "Element",
            "required": True,
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature1] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
        },
    )

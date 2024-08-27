from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_demonstrativo_retorno import CtDemonstrativoRetorno
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class DemonstrativoRetornoWs:
    """
    Operadora envia demonstrativos de pagamento (até 30)
    """

    class Meta:
        name = "demonstrativoRetornoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    demonstrativo_retorno: Optional[CtDemonstrativoRetorno] = field(
        default=None,
        metadata={
            "name": "demonstrativoRetorno",
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

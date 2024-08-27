from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_demonstrativo_solicitacao import CtDemonstrativoSolicitacao
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class SolicitacaoDemonstrativoRetornoWs:
    """
    Prestador solicita demonstrativo de retorno de pagamentos.
    """

    class Meta:
        name = "solicitacaoDemonstrativoRetornoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    solicitacao_demonstrativo_retorno: Optional[CtDemonstrativoSolicitacao] = (
        field(
            default=None,
            metadata={
                "name": "solicitacaoDemonstrativoRetorno",
                "type": "Element",
                "required": True,
            },
        )
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

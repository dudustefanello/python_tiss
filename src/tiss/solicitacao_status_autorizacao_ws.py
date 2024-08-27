from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_autorizacao_solicita_status import CtAutorizacaoSolicitaStatus
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class SolicitacaoStatusAutorizacaoWs:
    """
    Prestador solicita status de pedido de autorização.
    """

    class Meta:
        name = "solicitacaoStatusAutorizacaoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    solicitacao_status_autorizacao: Optional[CtAutorizacaoSolicitaStatus] = (
        field(
            default=None,
            metadata={
                "name": "solicitacaoStatusAutorizacao",
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

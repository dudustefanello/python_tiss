from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_protocolo_solicitacao_status import CtProtocoloSolicitacaoStatus
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class SolicitacaoStatusProtocoloWs:
    """
    Prestador solicita status de protocolo(s)
    """

    class Meta:
        name = "solicitacaoStatusProtocoloWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    solicitacao_status_protocolo: Optional[CtProtocoloSolicitacaoStatus] = (
        field(
            default=None,
            metadata={
                "name": "solicitacaoStatusProtocolo",
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

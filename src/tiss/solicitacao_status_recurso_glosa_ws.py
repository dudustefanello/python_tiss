from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_protocolo_solicitacao_status import CtProtocoloSolicitacaoStatus
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class SolicitacaoStatusRecursoGlosaWs:
    """
    Prestador solicita status de protocolo de recurso de glosa.
    """

    class Meta:
        name = "solicitacaoStatusRecursoGlosaWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    solicitacao_status_protocolo_recurso: Optional[
        CtProtocoloSolicitacaoStatus
    ] = field(
        default=None,
        metadata={
            "name": "solicitacaoStatusProtocoloRecurso",
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

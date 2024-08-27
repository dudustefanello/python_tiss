from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_situacao_autorizacao import CtSituacaoAutorizacao
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class SituacaoAutorizacaoWs:
    """
    Operadora responde status de autorização.
    """

    class Meta:
        name = "situacaoAutorizacaoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    situacao_autorizacao: Optional[CtSituacaoAutorizacao] = field(
        default=None,
        metadata={
            "name": "situacaoAutorizacao",
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

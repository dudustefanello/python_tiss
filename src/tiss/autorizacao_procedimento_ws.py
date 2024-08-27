from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_situacao_autorizacao import CtSituacaoAutorizacao
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class AutorizacaoProcedimentoWs:
    """
    Operadora responde a autorização de procedimento(SpSadt, internação ou
    prorrogação)
    """

    class Meta:
        name = "autorizacaoProcedimentoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    autorizacao_procedimento: Optional[CtSituacaoAutorizacao] = field(
        default=None,
        metadata={
            "name": "autorizacaoProcedimento",
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
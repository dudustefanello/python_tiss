from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_solicitacao_procedimento import CtSolicitacaoProcedimento
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class SolicitacaoProcedimentoWs:
    """
    Prestador solicita autorização de procedimento (SpSADT, Internação ou
    prorrogação de internação)
    """

    class Meta:
        name = "solicitacaoProcedimentoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    solicitacao_procedimento: Optional[CtSolicitacaoProcedimento] = field(
        default=None,
        metadata={
            "name": "solicitacaoProcedimento",
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

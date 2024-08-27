from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_resposta_elegibilidade import CtRespostaElegibilidade
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class RespostaElegibilidadeWs:
    """
    Operadora responde sobre a elegibilidade do paciente.
    """

    class Meta:
        name = "respostaElegibilidadeWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    resposta_elegibilidade: Optional[CtRespostaElegibilidade] = field(
        default=None,
        metadata={
            "name": "respostaElegibilidade",
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
    signatures: Optional[Signature1] = field(
        default=None,
        metadata={
            "name": "Signatures",
            "type": "Element",
        },
    )

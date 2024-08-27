from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_recibo_comunicacao import CtReciboComunicacao
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class ReciboComunicacaoWs:
    """
    Operadora responde a informação de internação/alta de beneficiário.
    """

    class Meta:
        name = "reciboComunicacaoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    recibo_comunicacao: Optional[CtReciboComunicacao] = field(
        default=None,
        metadata={
            "name": "reciboComunicacao",
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

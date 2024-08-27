from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_recibo_cancela_guia import CtReciboCancelaGuia
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class ReciboCancelaGuiaWs:
    """
    Operadora responde a solicitação de cancelamento de guia.
    """

    class Meta:
        name = "reciboCancelaGuiaWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    recibo_cancela_guia: Optional[CtReciboCancelaGuia] = field(
        default=None,
        metadata={
            "name": "reciboCancelaGuia",
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

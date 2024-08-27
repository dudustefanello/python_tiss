from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_anexo_lote import CtAnexoLote
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class LoteAnexoWs:
    """
    Prestador envia solicitação de quimio, radio e opme.
    """

    class Meta:
        name = "loteAnexoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lote_anexo: Optional[CtAnexoLote] = field(
        default=None,
        metadata={
            "name": "loteAnexo",
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

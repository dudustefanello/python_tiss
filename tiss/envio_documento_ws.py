from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_envio_documentos import CtEnvioDocumentos
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class EnvioDocumentoWs:
    class Meta:
        name = "envioDocumentoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    envio_documento: Optional[CtEnvioDocumentos] = field(
        default=None,
        metadata={
            "name": "envioDOcumento",
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

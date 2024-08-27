from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_recibo_documentos import CtReciboDocumentos
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class ReciboDocumentosWs:
    class Meta:
        name = "reciboDocumentosWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    recebimento_documento: Optional[
        "ReciboDocumentosWs.RecebimentoDocumento"
    ] = field(
        default=None,
        metadata={
            "name": "recebimentoDocumento",
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

    @dataclass
    class RecebimentoDocumento:
        mensagem_erro: Optional[CtMotivoGlosa] = field(
            default=None,
            metadata={
                "name": "mensagemErro",
                "type": "Element",
            },
        )
        recibo_documentos: Optional[CtReciboDocumentos] = field(
            default=None,
            metadata={
                "name": "reciboDocumentos",
                "type": "Element",
            },
        )

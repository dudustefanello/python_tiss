from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_anexo_recebimento import CtAnexoRecebimento
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class ProtocoloRecebimentoAnexoWs:
    """
    Operadora envia protocolo de recebimento dos anexos de quimio, radio e opme.
    """

    class Meta:
        name = "protocoloRecebimentoAnexoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    lote_anexo: Optional["ProtocoloRecebimentoAnexoWs.LoteAnexo"] = field(
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
    signatures: Optional[Signature1] = field(
        default=None,
        metadata={
            "name": "Signatures",
            "type": "Element",
        },
    )

    @dataclass
    class LoteAnexo:
        mensagem_erro: Optional[CtMotivoGlosa] = field(
            default=None,
            metadata={
                "name": "mensagemErro",
                "type": "Element",
            },
        )
        protocolo_recebimento_anexo: Optional[CtAnexoRecebimento] = field(
            default=None,
            metadata={
                "name": "protocoloRecebimentoAnexo",
                "type": "Element",
            },
        )

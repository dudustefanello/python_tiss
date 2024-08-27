from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_resposta_glosa import CtRespostaGlosa
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class SituacaoProtocoloRecursoWs:
    """
    Operadora responde situação do protocolo de recurso de glosa.
    """

    class Meta:
        name = "situacaoProtocoloRecursoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    situacao_protocolo_recurso: Optional[CtRespostaGlosa] = field(
        default=None,
        metadata={
            "name": "situacaoProtocoloRecurso",
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

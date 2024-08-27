from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ct_recebimento_recurso import CtRecebimentoRecurso
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class ProtocoloRecebimentoRecursoWs:
    """
    Operadora envia protocolo de recebimento de recurso de glosa.
    """

    class Meta:
        name = "protocoloRecebimentoRecursoWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    recebimento_recurso: Optional[CtRecebimentoRecurso] = field(
        default=None,
        metadata={
            "name": "recebimentoRecurso",
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

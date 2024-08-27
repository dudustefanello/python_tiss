from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_protocolo_recebimento import CtProtocoloRecebimento

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRecebimentoLote:
    class Meta:
        name = "ct_recebimentoLote"

    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    protocolo_recebimento: Optional[CtProtocoloRecebimento] = field(
        default=None,
        metadata={
            "name": "protocoloRecebimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

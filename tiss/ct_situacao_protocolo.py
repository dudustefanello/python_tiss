from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_protocolo_anexo_status import CtProtocoloAnexoStatus
from tiss.ct_protocolo_status import CtProtocoloStatus

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtSituacaoProtocolo:
    class Meta:
        name = "ct_situacaoProtocolo"

    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    situacao_do_protocolo: Optional[CtProtocoloStatus] = field(
        default=None,
        metadata={
            "name": "situacaoDoProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    situacao_protocolo_anexo: Optional[CtProtocoloAnexoStatus] = field(
        default=None,
        metadata={
            "name": "situacaoProtocoloAnexo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

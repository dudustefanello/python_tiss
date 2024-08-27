from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_recurso_glosa_recebimento import CtRecursoGlosaRecebimento

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRecebimentoRecurso:
    class Meta:
        name = "ct_recebimentoRecurso"

    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    protocolo_recebimento: Optional[CtRecursoGlosaRecebimento] = field(
        default=None,
        metadata={
            "name": "protocoloRecebimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

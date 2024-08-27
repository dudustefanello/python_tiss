from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_elegibilidade_recibo import CtElegibilidadeRecibo
from tiss.ct_motivo_glosa import CtMotivoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRespostaElegibilidade:
    class Meta:
        name = "ct_respostaElegibilidade"

    codigo_glosa: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "codigoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recibo_elegibilidade: Optional[CtElegibilidadeRecibo] = field(
        default=None,
        metadata={
            "name": "reciboElegibilidade",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

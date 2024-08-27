from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_unidade_tempo_ciclo import DmUnidadeTempoCiclo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtIntervaloCiclos:
    class Meta:
        name = "ct_intervaloCiclos"

    tempo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 2,
        },
    )
    unidade: Optional[DmUnidadeTempoCiclo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

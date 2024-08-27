from dataclasses import dataclass, field
from typing import List, Optional

from tiss.dm_indicador_acidente import DmIndicadorAcidente
from tiss.dm_motivo_saida import DmMotivoSaida

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmInternacaoDadosSaida:
    class Meta:
        name = "ctm_internacaoDadosSaida"

    diagnostico: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "max_occurs": 4,
            "min_length": 1,
            "max_length": 4,
        },
    )
    indicador_acidente: Optional[DmIndicadorAcidente] = field(
        default=None,
        metadata={
            "name": "indicadorAcidente",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    motivo_encerramento: Optional[DmMotivoSaida] = field(
        default=None,
        metadata={
            "name": "motivoEncerramento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_diagnostico import CtDiagnostico
from tiss.dm_indicador_acidente import DmIndicadorAcidente

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtHipoteseDiagnostica:
    class Meta:
        name = "ct_hipoteseDiagnostica"

    diagnostico: Optional[CtDiagnostico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    indicacao_acidente: Optional[DmIndicadorAcidente] = field(
        default=None,
        metadata={
            "name": "indicacaoAcidente",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

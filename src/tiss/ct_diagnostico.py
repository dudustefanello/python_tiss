from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_tabelas_diagnostico import DmTabelasDiagnostico

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDiagnostico:
    class Meta:
        name = "ct_diagnostico"

    tabela_diagnostico: Optional[DmTabelasDiagnostico] = field(
        default=None,
        metadata={
            "name": "tabelaDiagnostico",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    codigo_diagnostico: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoDiagnostico",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    descricao_diagnostico: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoDiagnostico",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )

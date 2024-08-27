from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_tabela import DmTabela

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoDados:
    class Meta:
        name = "ct_procedimentoDados"

    codigo_tabela: Optional[DmTabela] = field(
        default=None,
        metadata={
            "name": "codigoTabela",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    codigo_procedimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoProcedimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )
    descricao_procedimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoProcedimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 150,
        },
    )

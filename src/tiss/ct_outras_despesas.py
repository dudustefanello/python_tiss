from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_procedimento_executado_outras import CtProcedimentoExecutadoOutras
from tiss.dm_outras_despesas import DmOutrasDespesas

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtOutrasDespesas:
    class Meta:
        name = "ct_outrasDespesas"

    despesa: List["CtOutrasDespesas.Despesa"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Despesa:
        sequencial_item: Optional[int] = field(
            default=None,
            metadata={
                "name": "sequencialItem",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 4,
            },
        )
        codigo_despesa: Optional[DmOutrasDespesas] = field(
            default=None,
            metadata={
                "name": "codigoDespesa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        servicos_executados: Optional[CtProcedimentoExecutadoOutras] = field(
            default=None,
            metadata={
                "name": "servicosExecutados",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        item_vinculado: Optional[int] = field(
            default=None,
            metadata={
                "name": "itemVinculado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "total_digits": 4,
            },
        )

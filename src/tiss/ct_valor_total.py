from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtValorTotal:
    class Meta:
        name = "ct_valorTotal"

    valor_processado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorProcessado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_glosa: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_liberado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorLiberado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )

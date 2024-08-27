from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtCreditoOdonto:
    class Meta:
        name = "ct_creditoOdonto"

    valor_credito: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorCredito",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    descricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )

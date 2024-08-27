from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from tiss.dm_tipo_lancamento import DmTipoLancamento

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtValorCreditoDesconto:
    class Meta:
        name = "ct_valorCreditoDesconto"

    tipo_lancamento: Optional[DmTipoLancamento] = field(
        default=None,
        metadata={
            "name": "tipoLancamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    descricao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 100,
        },
    )
    valor: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from tiss.dm_debito_credito_indicador import DmDebitoCreditoIndicador
from tiss.dm_debito_credito_tipo import DmDebitoCreditoTipo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDescontos:
    class Meta:
        name = "ct_descontos"

    indicador: Optional[DmDebitoCreditoIndicador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    tipo_debito_credito: Optional[DmDebitoCreditoTipo] = field(
        default=None,
        metadata={
            "name": "tipoDebitoCredito",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    descricao_db_cr: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoDbCr",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    valor_db_cr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorDbCr",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )

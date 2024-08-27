from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from tiss.dm_sexo import DmSexo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDadosComplementaresBeneficiario:
    class Meta:
        name = "ct_dadosComplementaresBeneficiario"

    peso: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    altura: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    superficie_corporal: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "superficieCorporal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 4,
            "fraction_digits": 2,
        },
    )
    idade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    sexo: Optional[DmSexo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

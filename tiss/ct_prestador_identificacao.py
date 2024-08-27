from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtPrestadorIdentificacao:
    class Meta:
        name = "ct_prestadorIdentificacao"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "pattern": r"[0-9]{14}",
        },
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "pattern": r"[0-9]{11}",
        },
    )
    codigo_prestador_na_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoPrestadorNaOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 14,
        },
    )

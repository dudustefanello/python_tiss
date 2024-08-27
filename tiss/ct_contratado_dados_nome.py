from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtContratadoDadosNome:
    class Meta:
        name = "ct_contratadoDadosNome"

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
    cpf_contratado: Optional[str] = field(
        default=None,
        metadata={
            "name": "cpfContratado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "pattern": r"[0-9]{11}",
        },
    )
    cnpj_contratado: Optional[str] = field(
        default=None,
        metadata={
            "name": "cnpjContratado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "pattern": r"[0-9]{14}",
        },
    )
    nome_contratado: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeContratado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )

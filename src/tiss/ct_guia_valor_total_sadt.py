from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGuiaValorTotalSadt:
    class Meta:
        name = "ct_guiaValorTotalSADT"

    valor_procedimentos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorProcedimentos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_taxas_alugueis: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTaxasAlugueis",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_materiais: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorMateriais",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_medicamentos: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorMedicamentos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_opme: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorOPME",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_gases_medicinais: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorGasesMedicinais",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_total_geral: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalGeral",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )

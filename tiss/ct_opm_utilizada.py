from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_procedimento_dados import CtProcedimentoDados

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtOpmUtilizada:
    class Meta:
        name = "ct_opmUtilizada"

    opm: Optional["CtOpmUtilizada.Opm"] = field(
        default=None,
        metadata={
            "name": "OPM",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    valor_total_opm: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalOPM",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )

    @dataclass
    class Opm:
        identificacao_opm: List["CtOpmUtilizada.Opm.IdentificacaoOpm"] = field(
            default_factory=list,
            metadata={
                "name": "identificacaoOPM",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

        @dataclass
        class IdentificacaoOpm:
            identificacao_opme: Optional[CtProcedimentoDados] = field(
                default=None,
                metadata={
                    "name": "identificacaoOPME",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            quantidade: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 2,
                },
            )
            codigo_barra: Optional[str] = field(
                default=None,
                metadata={
                    "name": "codigoBarra",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 20,
                },
            )
            valor_unitario: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorUnitario",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "total_digits": 8,
                    "fraction_digits": 2,
                },
            )
            valor_total: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorTotal",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "total_digits": 8,
                    "fraction_digits": 2,
                },
            )

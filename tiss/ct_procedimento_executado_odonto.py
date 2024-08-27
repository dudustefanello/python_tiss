from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_dente import DmDente
from tiss.dm_regiao import DmRegiao
from tiss.dm_sim_nao import DmSimNao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoExecutadoOdonto:
    class Meta:
        name = "ct_procedimentoExecutadoOdonto"

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
    procedimento: Optional[CtProcedimentoDados] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dente_regiao: Optional["CtProcedimentoExecutadoOdonto.DenteRegiao"] = (
        field(
            default=None,
            metadata={
                "name": "denteRegiao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )
    dente_face: Optional[str] = field(
        default=None,
        metadata={
            "name": "denteFace",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "pattern": r"[OLMVDIP]{1,5}",
        },
    )
    qtd_proc: Optional[int] = field(
        default=None,
        metadata={
            "name": "qtdProc",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 2,
        },
    )
    qtd_us: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "qtdUS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    valor_proc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorProc",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    valor_franquia: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorFranquia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    autorizado: Optional[DmSimNao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    data_realizacao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataRealizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class DenteRegiao:
        cod_dente: Optional[DmDente] = field(
            default=None,
            metadata={
                "name": "codDente",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        cod_regiao: Optional[DmRegiao] = field(
            default=None,
            metadata={
                "name": "codRegiao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

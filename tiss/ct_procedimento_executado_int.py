from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlTime

from tiss.ct_ident_equipe import CtIdentEquipe
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_tecnica_utilizada import DmTecnicaUtilizada
from tiss.dm_via_de_acesso import DmViaDeAcesso

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoExecutadoInt:
    class Meta:
        name = "ct_procedimentoExecutadoInt"

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
    data_execucao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataExecucao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    hora_inicial: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaInicial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    hora_final: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaFinal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
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
    quantidade_executada: Optional[int] = field(
        default=None,
        metadata={
            "name": "quantidadeExecutada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    via_acesso: Optional[DmViaDeAcesso] = field(
        default=None,
        metadata={
            "name": "viaAcesso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    tecnica_utilizada: Optional[DmTecnicaUtilizada] = field(
        default=None,
        metadata={
            "name": "tecnicaUtilizada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    reducao_acrescimo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "reducaoAcrescimo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 2,
        },
    )
    valor_unitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorUnitario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    ident_equipe: List["CtProcedimentoExecutadoInt.IdentEquipe"] = field(
        default_factory=list,
        metadata={
            "name": "identEquipe",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class IdentEquipe:
        identificacao_equipe: Optional[CtIdentEquipe] = field(
            default=None,
            metadata={
                "name": "identificacaoEquipe",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

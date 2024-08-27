from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlTime

from tiss.ct_ident_equipe_sadt import CtIdentEquipeSadt
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_tecnica_utilizada import DmTecnicaUtilizada
from tiss.dm_via_de_acesso import DmViaDeAcesso

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoExecutadoSadt:
    class Meta:
        name = "ct_procedimentoExecutadoSadt"

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
    equipe_sadt: List[CtIdentEquipeSadt] = field(
        default_factory=list,
        metadata={
            "name": "equipeSadt",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

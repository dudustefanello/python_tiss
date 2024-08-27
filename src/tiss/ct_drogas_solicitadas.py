from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_unidade_medida import DmUnidadeMedida
from tiss.dm_via_administracao import DmViaAdministracao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDrogasSolicitadas:
    class Meta:
        name = "ct_drogasSolicitadas"

    data_provavel: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataProvavel",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    identificacao: Optional[CtProcedimentoDados] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    qt_doses: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "qtDoses",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 7,
            "fraction_digits": 2,
        },
    )
    unidade_medida: Optional[DmUnidadeMedida] = field(
        default=None,
        metadata={
            "name": "unidadeMedida",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    via_administracao: Optional[DmViaAdministracao] = field(
        default=None,
        metadata={
            "name": "viaAdministracao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    frequencia: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 2,
        },
    )

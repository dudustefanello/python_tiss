from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_procedimento_dados import CtProcedimentoDados

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentosComplementares:
    class Meta:
        name = "ct_procedimentosComplementares"

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
    quantidade: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )

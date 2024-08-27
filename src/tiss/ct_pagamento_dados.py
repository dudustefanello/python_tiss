from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.dm_forma_pagamento import DmFormaPagamento

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtPagamentoDados:
    class Meta:
        name = "ct_pagamentoDados"

    data_pagamento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataPagamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    forma_pagamento: Optional[DmFormaPagamento] = field(
        default=None,
        metadata={
            "name": "formaPagamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    banco: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 4,
        },
    )
    agencia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 7,
        },
    )
    nr_conta_cheque: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrContaCheque",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )

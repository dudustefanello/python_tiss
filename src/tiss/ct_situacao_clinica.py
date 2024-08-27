from dataclasses import dataclass, field
from typing import List, Optional

from tiss.dm_condicao_clinica import DmCondicaoClinica
from tiss.dm_dente import DmDente

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtSituacaoClinica:
    class Meta:
        name = "ct_situacaoClinica"

    dentes: List["CtSituacaoClinica.Dentes"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Dentes:
        elemento_dentario: Optional[DmDente] = field(
            default=None,
            metadata={
                "name": "elementoDentario",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        condicao_clinica: Optional[DmCondicaoClinica] = field(
            default=None,
            metadata={
                "name": "condicaoClinica",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

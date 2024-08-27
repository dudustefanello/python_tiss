from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_unidade_medida import DmUnidadeMedida

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoSolicitado:
    class Meta:
        name = "ct_procedimentoSolicitado"

    procedimento: Optional[CtProcedimentoDados] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    quantidade_solicitada: Optional[int] = field(
        default=None,
        metadata={
            "name": "quantidadeSolicitada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )

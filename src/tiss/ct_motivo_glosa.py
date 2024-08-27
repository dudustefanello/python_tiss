from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtMotivoGlosa:
    class Meta:
        name = "ct_motivoGlosa"

    codigo_glosa: Optional[DmTipoGlosa] = field(
        default=None,
        metadata={
            "name": "codigoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    descricao_glosa: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 500,
        },
    )

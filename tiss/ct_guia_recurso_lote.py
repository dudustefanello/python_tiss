from dataclasses import dataclass, field
from typing import Optional

from tiss.ctm_recurso_glosa import CtmRecursoGlosa
from tiss.cto_recurso_glosa_odonto import CtoRecursoGlosaOdonto

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGuiaRecursoLote:
    """
    Lote de recurso de glosa.
    """

    class Meta:
        name = "ct_guiaRecursoLote"

    guia_recurso_glosa_odonto: Optional[CtoRecursoGlosaOdonto] = field(
        default=None,
        metadata={
            "name": "guiaRecursoGlosaOdonto",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    guia_recurso_glosa: Optional[CtmRecursoGlosa] = field(
        default=None,
        metadata={
            "name": "guiaRecursoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

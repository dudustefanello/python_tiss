from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_guia_recurso import CtGuiaRecurso
from tiss.ct_motivo_glosa import CtMotivoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProtocoloRecurso:
    """
    Estrutura da resposta da operadora a um lote de guias de recurso de glosa de
    medicina e de odonto.
    """

    class Meta:
        name = "ct_protocoloRecurso"

    numero_protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    glosa_protocolo: List[CtMotivoGlosa] = field(
        default_factory=list,
        metadata={
            "name": "glosaProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    dados_guias: List[CtGuiaRecurso] = field(
        default_factory=list,
        metadata={
            "name": "dadosGuias",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

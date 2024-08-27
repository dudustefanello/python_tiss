from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGuiaRecurso:
    """
    Estrutura utilizada no retorno do recurso de glosa.
    """

    class Meta:
        name = "ct_guiaRecurso"

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
    num_demo_analise_pagto: Optional[str] = field(
        default=None,
        metadata={
            "name": "numDemoAnalisePagto",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 12,
        },
    )
    numero_guia_recurso: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    numero_guia_origem: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaOrigem",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    motivos_glosa: List[CtMotivoGlosa] = field(
        default_factory=list,
        metadata={
            "name": "motivosGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

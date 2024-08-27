from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_guia_dados_anexo import CtGuiaDadosAnexo
from tiss.ct_motivo_glosa import CtMotivoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProtocoloDetalheAnexo:
    class Meta:
        name = "ct_protocoloDetalheAnexo"

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
    valor_total_protocolo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    glosas_protocolo: List[CtMotivoGlosa] = field(
        default_factory=list,
        metadata={
            "name": "glosasProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    vl_glosa_protocolo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "vlGlosaProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    dados_guias: List[CtGuiaDadosAnexo] = field(
        default_factory=list,
        metadata={
            "name": "dadosGuias",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
        },
    )

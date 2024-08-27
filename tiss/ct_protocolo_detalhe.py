from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_guia_dados import CtGuiaDados
from tiss.ct_guia_dados_odonto import CtGuiaDadosOdonto
from tiss.ct_motivo_glosa import CtMotivoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProtocoloDetalhe:
    class Meta:
        name = "ct_protocoloDetalhe"

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
    glosa_protocolo: Optional["CtProtocoloDetalhe.GlosaProtocolo"] = field(
        default=None,
        metadata={
            "name": "glosaProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    dados_guias_protocolo: Optional[
        "CtProtocoloDetalhe.DadosGuiasProtocolo"
    ] = field(
        default=None,
        metadata={
            "name": "dadosGuiasProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class GlosaProtocolo:
        motivos_glosa: Optional[
            "CtProtocoloDetalhe.GlosaProtocolo.MotivosGlosa"
        ] = field(
            default=None,
            metadata={
                "name": "motivosGlosa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        vl_glosa_protocolo: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "vlGlosaProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )

        @dataclass
        class MotivosGlosa:
            motivo_glosa: List[CtMotivoGlosa] = field(
                default_factory=list,
                metadata={
                    "name": "motivoGlosa",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_occurs": 1,
                },
            )

    @dataclass
    class DadosGuiasProtocolo:
        dados_guias: List[CtGuiaDados] = field(
            default_factory=list,
            metadata={
                "name": "dadosGuias",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        dados_guias_odonto: List[CtGuiaDadosOdonto] = field(
            default_factory=list,
            metadata={
                "name": "dadosGuiasOdonto",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

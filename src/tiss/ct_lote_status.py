from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_guia_dados import CtGuiaDados
from tiss.ct_guia_dados_odonto import CtGuiaDadosOdonto
from tiss.ct_valor_total import CtValorTotal
from tiss.dm_status_protocolo import DmStatusProtocolo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtLoteStatus:
    """
    Resposta a uma solicitação de situação de protocolo.
    """

    class Meta:
        name = "ct_loteStatus"

    status_protocolo: Optional[DmStatusProtocolo] = field(
        default=None,
        metadata={
            "name": "statusProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
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
    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    data_envio_lote: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEnvioLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    valor_total_lote: Optional[CtValorTotal] = field(
        default=None,
        metadata={
            "name": "valorTotalLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    guias_tiss: Optional["CtLoteStatus.GuiasTiss"] = field(
        default=None,
        metadata={
            "name": "guiasTISS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class GuiasTiss:
        guias_medicas: List["CtLoteStatus.GuiasTiss.GuiasMedicas"] = field(
            default_factory=list,
            metadata={
                "name": "guiasMedicas",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        guias_odonto: List["CtLoteStatus.GuiasTiss.GuiasOdonto"] = field(
            default_factory=list,
            metadata={
                "name": "guiasOdonto",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

        @dataclass
        class GuiasMedicas:
            guias: Optional[CtGuiaDados] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )

        @dataclass
        class GuiasOdonto:
            guias: Optional[CtGuiaDadosOdonto] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )

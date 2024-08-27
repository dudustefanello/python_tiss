from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.dm_tipo_pagamento import DmTipoPagamento

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDadosResumoDemonstrativo:
    class Meta:
        name = "ct_dadosResumoDemonstrativo"

    data_protocolo: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataProtocolo",
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
    valor_informado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorInformado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_processado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorProcessado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_liberado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorLiberado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_glosa: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    guias_do_lote: List["CtDadosResumoDemonstrativo.GuiasDoLote"] = field(
        default_factory=list,
        metadata={
            "name": "guiasDoLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )

    @dataclass
    class GuiasDoLote:
        numero_guia_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "numeroGuiaPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 20,
            },
        )
        numero_guia_operadora: Optional[str] = field(
            default=None,
            metadata={
                "name": "numeroGuiaOperadora",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 20,
            },
        )
        senha: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 20,
            },
        )
        tipo_pagamento: Optional[DmTipoPagamento] = field(
            default=None,
            metadata={
                "name": "tipoPagamento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        valor_processado_guia: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorProcessadoGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )
        valor_liberado_guia: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorLiberadoGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )
        valor_glosa_guia: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorGlosaGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )

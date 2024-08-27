from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.dm_tipo_guia import DmTipoGuia

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGuiaCancelamento:
    class Meta:
        name = "ct_guiaCancelamento"

    dados_prestador: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    tipo_cancelamento: Optional["CtGuiaCancelamento.TipoCancelamento"] = field(
        default=None,
        metadata={
            "name": "tipoCancelamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class TipoCancelamento:
        tipo_cancelamento_lote: Optional[
            "CtGuiaCancelamento.TipoCancelamento.TipoCancelamentoLote"
        ] = field(
            default=None,
            metadata={
                "name": "tipoCancelamentoLote",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        tipo_cancelamento_guia: List[
            "CtGuiaCancelamento.TipoCancelamento.TipoCancelamentoGuia"
        ] = field(
            default_factory=list,
            metadata={
                "name": "tipoCancelamentoGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

        @dataclass
        class TipoCancelamentoLote:
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
            numero_protocolo: Optional[str] = field(
                default=None,
                metadata={
                    "name": "numeroProtocolo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 12,
                },
            )

        @dataclass
        class TipoCancelamentoGuia:
            tipo_guia: Optional[DmTipoGuia] = field(
                default=None,
                metadata={
                    "name": "tipoGuia",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
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
            numero_protocolo: Optional[str] = field(
                default=None,
                metadata={
                    "name": "numeroProtocolo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 12,
                },
            )

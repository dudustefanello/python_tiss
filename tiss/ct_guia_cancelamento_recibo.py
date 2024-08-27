from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.dm_status_cancelamento import DmStatusCancelamento
from tiss.dm_tipo_guia import DmTipoGuia

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGuiaCancelamentoRecibo:
    class Meta:
        name = "ct_guiaCancelamentoRecibo"

    registro_ans: Optional[str] = field(
        default=None,
        metadata={
            "name": "registroANS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "max_length": 6,
            "pattern": r"[0-9]{6}",
        },
    )
    dados_prestador: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    retorno_status: Optional["CtGuiaCancelamentoRecibo.RetornoStatus"] = field(
        default=None,
        metadata={
            "name": "retornoStatus",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class RetornoStatus:
        lote_cancelado: Optional[
            "CtGuiaCancelamentoRecibo.RetornoStatus.LoteCancelado"
        ] = field(
            default=None,
            metadata={
                "name": "loteCancelado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        guias_canceladas: Optional[
            "CtGuiaCancelamentoRecibo.RetornoStatus.GuiasCanceladas"
        ] = field(
            default=None,
            metadata={
                "name": "guiasCanceladas",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

        @dataclass
        class LoteCancelado:
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
            numeroprotocolo: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 12,
                },
            )
            status_cancelamento: Optional[DmStatusCancelamento] = field(
                default=None,
                metadata={
                    "name": "statusCancelamento",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )

        @dataclass
        class GuiasCanceladas:
            dados_guia: List[
                "CtGuiaCancelamentoRecibo.RetornoStatus.GuiasCanceladas.DadosGuia"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "dadosGuia",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class DadosGuia:
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
                status_cancelamento: Optional[DmStatusCancelamento] = field(
                    default=None,
                    metadata={
                        "name": "statusCancelamento",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                    },
                )

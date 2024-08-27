from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlTime

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_grau_part import DmGrauPart
from tiss.dm_status_protocolo import DmStatusProtocolo
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtContaMedicaResumo:
    """
    Utilizado no demonstrativo de análise de conta.
    """

    class Meta:
        name = "ct_contaMedicaResumo"

    numero_lote_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroLotePrestador",
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
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    data_protocolo: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    glosa_protocolo: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "GlosaProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    situacao_protocolo: Optional[DmStatusProtocolo] = field(
        default=None,
        metadata={
            "name": "situacaoProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    relacao_guias: List["CtContaMedicaResumo.RelacaoGuias"] = field(
        default_factory=list,
        metadata={
            "name": "relacaoGuias",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    valor_informado_protocolo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorInformadoProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_processado_protocolo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorProcessadoProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_liberado_protocolo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorLiberadoProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_glosa_protocolo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorGlosaProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )

    @dataclass
    class RelacaoGuias:
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
        numero_carteira: Optional[str] = field(
            default=None,
            metadata={
                "name": "numeroCarteira",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 20,
            },
        )
        data_inicio_fat: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataInicioFat",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        hora_inicio_fat: Optional[XmlTime] = field(
            default=None,
            metadata={
                "name": "horaInicioFat",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        data_fim_fat: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataFimFat",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        hora_fim_fat: Optional[XmlTime] = field(
            default=None,
            metadata={
                "name": "horaFimFat",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        motivo_glosa_guia: List[CtMotivoGlosa] = field(
            default_factory=list,
            metadata={
                "name": "motivoGlosaGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        situacao_guia: Optional[DmStatusProtocolo] = field(
            default=None,
            metadata={
                "name": "situacaoGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        detalhes_guia: List[
            "CtContaMedicaResumo.RelacaoGuias.DetalhesGuia"
        ] = field(
            default_factory=list,
            metadata={
                "name": "detalhesGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        valor_informado_guia: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorInformadoGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
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

        @dataclass
        class DetalhesGuia:
            sequencial_item: Optional[int] = field(
                default=None,
                metadata={
                    "name": "sequencialItem",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 4,
                },
            )
            data_realizacao: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "dataRealizacao",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            procedimento: Optional[CtProcedimentoDados] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            grau_participacao: Optional[DmGrauPart] = field(
                default=None,
                metadata={
                    "name": "grauParticipacao",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            valor_informado: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorInformado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 8,
                    "fraction_digits": 2,
                },
            )
            qtd_executada: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "qtdExecutada",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 9,
                    "fraction_digits": 4,
                },
            )
            valor_processado: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorProcessado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 8,
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
                    "total_digits": 8,
                    "fraction_digits": 2,
                },
            )
            relacao_glosa: List[
                "CtContaMedicaResumo.RelacaoGuias.DetalhesGuia.RelacaoGlosa"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "relacaoGlosa",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )

            @dataclass
            class RelacaoGlosa:
                valor_glosa: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorGlosa",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 8,
                        "fraction_digits": 2,
                    },
                )
                tipo_glosa: Optional[DmTipoGlosa] = field(
                    default=None,
                    metadata={
                        "name": "tipoGlosa",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                    },
                )

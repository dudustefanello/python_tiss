from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_dente import DmDente
from tiss.dm_regiao import DmRegiao
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRecursoGlosaRecebimento:
    class Meta:
        name = "ct_recursoGlosaRecebimento"

    nr_protocolo_recurso_glosa: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrProtocoloRecursoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    data_envio_recurso: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEnvioRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_recebimento_recurso: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataRecebimentoRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    nr_protocolo_recursado: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrProtocoloRecursado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    recurso_protocolo: Optional[
        "CtRecursoGlosaRecebimento.RecursoProtocolo"
    ] = field(
        default=None,
        metadata={
            "name": "recursoProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    qt_guias_recurso: Optional[int] = field(
        default=None,
        metadata={
            "name": "qtGuiasRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 3,
        },
    )
    guias_recurso: List["CtRecursoGlosaRecebimento.GuiasRecurso"] = field(
        default_factory=list,
        metadata={
            "name": "guiasRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "max_occurs": 100,
        },
    )
    observacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 500,
        },
    )
    valor_total_recursado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalRecursado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )

    @dataclass
    class RecursoProtocolo:
        codigo_glosa_protocolo: Optional[DmTipoGlosa] = field(
            default=None,
            metadata={
                "name": "codigoGlosaProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        justificativa_protocolo: Optional[str] = field(
            default=None,
            metadata={
                "name": "justificativaProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 500,
            },
        )

    @dataclass
    class GuiasRecurso:
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
        opcao_recurso_guia: Optional[
            "CtRecursoGlosaRecebimento.GuiasRecurso.OpcaoRecursoGuia"
        ] = field(
            default=None,
            metadata={
                "name": "opcaoRecursoGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class OpcaoRecursoGuia:
            recurso_guia: List[
                "CtRecursoGlosaRecebimento.GuiasRecurso.OpcaoRecursoGuia.RecursoGuia"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "recursoGuia",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            itens_guia: List[
                "CtRecursoGlosaRecebimento.GuiasRecurso.OpcaoRecursoGuia.ItensGuia"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "itensGuia",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )

            @dataclass
            class RecursoGuia:
                cod_glosa_guia: Optional[DmTipoGlosa] = field(
                    default=None,
                    metadata={
                        "name": "codGlosaGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                    },
                )
                justificativa_guia: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "justificativaGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "min_length": 1,
                        "max_length": 150,
                    },
                )

            @dataclass
            class ItensGuia:
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
                data_inicio: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "name": "dataInicio",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                    },
                )
                data_fim: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "name": "dataFim",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    },
                )
                proc_recurso: Optional[CtProcedimentoDados] = field(
                    default=None,
                    metadata={
                        "name": "procRecurso",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                    },
                )
                dente_regiao: Optional[
                    "CtRecursoGlosaRecebimento.GuiasRecurso.OpcaoRecursoGuia.ItensGuia.DenteRegiao"
                ] = field(
                    default=None,
                    metadata={
                        "name": "denteRegiao",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    },
                )
                dente_face: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "denteFace",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "pattern": r"[OLMVDIP]{1,5}",
                    },
                )
                cod_glosa_item: Optional[DmTipoGlosa] = field(
                    default=None,
                    metadata={
                        "name": "codGlosaItem",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                    },
                )
                valor_recursado: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorRecursado",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 8,
                        "fraction_digits": 2,
                    },
                )
                justificativa_item: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "justificativaItem",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "min_length": 1,
                        "max_length": 500,
                    },
                )

                @dataclass
                class DenteRegiao:
                    cod_dente: Optional[DmDente] = field(
                        default=None,
                        metadata={
                            "name": "codDente",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        },
                    )
                    cod_regiao: Optional[DmRegiao] = field(
                        default=None,
                        metadata={
                            "name": "codRegiao",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        },
                    )

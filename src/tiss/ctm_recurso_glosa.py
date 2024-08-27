from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_grau_part import DmGrauPart
from tiss.dm_objeto_recurso import DmObjetoRecurso
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmRecursoGlosa:
    class Meta:
        name = "ctm_recursoGlosa"

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
    numero_guia_rec_glosa_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaRecGlosaPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    nome_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    objeto_recurso: Optional[DmObjetoRecurso] = field(
        default=None,
        metadata={
            "name": "objetoRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_guia_rec_glosa_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaRecGlosaOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )
    dados_contratado: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosContratado",
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
    numero_protocolo: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 12,
        },
    )
    opcao_recurso: Optional["CtmRecursoGlosa.OpcaoRecurso"] = field(
        default=None,
        metadata={
            "name": "opcaoRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    data_recurso: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class OpcaoRecurso:
        recurso_protocolo: Optional[
            "CtmRecursoGlosa.OpcaoRecurso.RecursoProtocolo"
        ] = field(
            default=None,
            metadata={
                "name": "recursoProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        recurso_guia: List["CtmRecursoGlosa.OpcaoRecurso.RecursoGuia"] = field(
            default_factory=list,
            metadata={
                "name": "recursoGuia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
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
        class RecursoGuia:
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
                "CtmRecursoGlosa.OpcaoRecurso.RecursoGuia.OpcaoRecursoGuia"
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
                recurso_guia_completa: List[
                    "CtmRecursoGlosa.OpcaoRecurso.RecursoGuia.OpcaoRecursoGuia.RecursoGuiaCompleta"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "recursoGuiaCompleta",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    },
                )
                itens_guia: List[
                    "CtmRecursoGlosa.OpcaoRecurso.RecursoGuia.OpcaoRecursoGuia.ItensGuia"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "itensGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    },
                )

                @dataclass
                class RecursoGuiaCompleta:
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
                            "max_length": 500,
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
                    grau_participacao: Optional[DmGrauPart] = field(
                        default=None,
                        metadata={
                            "name": "grauParticipacao",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
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

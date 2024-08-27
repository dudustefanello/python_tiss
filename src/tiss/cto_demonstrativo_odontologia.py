from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_descontos import CtDescontos
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_dente import DmDente
from tiss.dm_regiao import DmRegiao
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtoDemonstrativoOdontologia:
    class Meta:
        name = "cto_demonstrativoOdontologia"

    cabecalho_demonstrativo_odonto: Optional[
        "CtoDemonstrativoOdontologia.CabecalhoDemonstrativoOdonto"
    ] = field(
        default=None,
        metadata={
            "name": "cabecalhoDemonstrativoOdonto",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_prestador: Optional["CtoDemonstrativoOdontologia.DadosPrestador"] = (
        field(
            default=None,
            metadata={
                "name": "dadosPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    dados_pagamento_por_data: List[
        "CtoDemonstrativoOdontologia.DadosPagamentoPorData"
    ] = field(
        default_factory=list,
        metadata={
            "name": "dadosPagamentoPorData",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
        },
    )
    totais_bruto_demonstrativo: Optional[
        "CtoDemonstrativoOdontologia.TotaisBrutoDemonstrativo"
    ] = field(
        default=None,
        metadata={
            "name": "totaisBrutoDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    deb_cred_demonstrativo: Optional[
        "CtoDemonstrativoOdontologia.DebCredDemonstrativo"
    ] = field(
        default=None,
        metadata={
            "name": "debCredDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    total_debitos_demonstativo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalDebitosDemonstativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    total_creditos_demonstrativo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalCreditosDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_recebido_demonstrativo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorRecebidoDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
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

    @dataclass
    class CabecalhoDemonstrativoOdonto:
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
        numero_demonstrativo: Optional[str] = field(
            default=None,
            metadata={
                "name": "numeroDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 12,
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
        cnpj_oper: Optional[str] = field(
            default=None,
            metadata={
                "name": "cnpjOper",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "pattern": r"[0-9]{14}",
            },
        )
        periodo_proc: Optional[
            "CtoDemonstrativoOdontologia.CabecalhoDemonstrativoOdonto.PeriodoProc"
        ] = field(
            default=None,
            metadata={
                "name": "periodoProc",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class PeriodoProc:
            datainicio: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            datafim: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )

    @dataclass
    class DadosPrestador:
        codigo_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "codigoPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 14,
            },
        )
        cpf_cnpjcontratado: Optional[
            "CtoDemonstrativoOdontologia.DadosPrestador.CpfCnpjcontratado"
        ] = field(
            default=None,
            metadata={
                "name": "cpfCNPJContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class CpfCnpjcontratado:
            cnpj_prestador: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cnpjPrestador",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "pattern": r"[0-9]{14}",
                },
            )
            cpf_contratado: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cpfContratado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "pattern": r"[0-9]{11}",
                },
            )

    @dataclass
    class DadosPagamentoPorData:
        dados_pagamento: Optional[
            "CtoDemonstrativoOdontologia.DadosPagamentoPorData.DadosPagamento"
        ] = field(
            default=None,
            metadata={
                "name": "dadosPagamento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        protocolos: List[
            "CtoDemonstrativoOdontologia.DadosPagamentoPorData.Protocolos"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )
        totais_por_data: Optional[
            "CtoDemonstrativoOdontologia.DadosPagamentoPorData.TotaisPorData"
        ] = field(
            default=None,
            metadata={
                "name": "totaisPorData",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        deb_cred_por_data_pagamento: Optional[
            "CtoDemonstrativoOdontologia.DadosPagamentoPorData.DebCredPorDataPagamento"
        ] = field(
            default=None,
            metadata={
                "name": "debCredPorDataPagamento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        total_liquido_por_data: Optional[
            "CtoDemonstrativoOdontologia.DadosPagamentoPorData.TotalLiquidoPorData"
        ] = field(
            default=None,
            metadata={
                "name": "totalLiquidoPorData",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class DadosPagamento:
            data_pagamento: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "dataPagamento",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            banco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 4,
                },
            )
            agencia: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 7,
                },
            )
            conta: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 20,
                },
            )

        @dataclass
        class Protocolos:
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
                    "required": True,
                    "min_length": 1,
                    "max_length": 12,
                },
            )
            dados_pagamento_guia: List[
                "CtoDemonstrativoOdontologia.DadosPagamentoPorData.Protocolos.DadosPagamentoGuia"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "dadosPagamentoGuia",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_occurs": 1,
                },
            )
            totais_por_protocolo: Optional[
                "CtoDemonstrativoOdontologia.DadosPagamentoPorData.Protocolos.TotaisPorProtocolo"
            ] = field(
                default=None,
                metadata={
                    "name": "totaisPorProtocolo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )

            @dataclass
            class DadosPagamentoGuia:
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
                recurso: Optional[DmSimNao] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                    },
                )
                nome_executante: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nomeExecutante",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "min_length": 1,
                        "max_length": 70,
                    },
                )
                carteira_beneficiario: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "carteiraBeneficiario",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                    },
                )
                dados_pagamento: List[
                    "CtoDemonstrativoOdontologia.DadosPagamentoPorData.Protocolos.DadosPagamentoGuia.DadosPagamento"
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "dadosPagamento",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "min_occurs": 1,
                    },
                )
                observacao_guia: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "observacaoGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "min_length": 1,
                        "max_length": 500,
                    },
                )
                valor_total_informado_guia: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalInformadoGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 8,
                        "fraction_digits": 2,
                    },
                )
                valor_total_processado_guia: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalProcessadoGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 8,
                        "fraction_digits": 2,
                    },
                )
                valor_total_glosa_guia: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalGlosaGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 8,
                        "fraction_digits": 2,
                    },
                )
                valor_total_franquia_guia: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalFranquiaGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 8,
                        "fraction_digits": 2,
                    },
                )
                valor_total_liberado_guia: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalLiberadoGuia",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 8,
                        "fraction_digits": 2,
                    },
                )

                @dataclass
                class DadosPagamento:
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
                    procedimento: Optional[CtProcedimentoDados] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                            "required": True,
                        },
                    )
                    dente_regiao: Optional[
                        "CtoDemonstrativoOdontologia.DadosPagamentoPorData.Protocolos.DadosPagamentoGuia.DadosPagamento.DenteRegiao"
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
                            "min_length": 1,
                            "max_length": 5,
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
                    qtd_proc: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "qtdProc",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                            "required": True,
                            "total_digits": 2,
                        },
                    )
                    valor_informado: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "valorInformado",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                            "required": True,
                            "total_digits": 7,
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
                            "total_digits": 7,
                            "fraction_digits": 2,
                        },
                    )
                    valor_glosa_estorno: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "valorGlosaEstorno",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                            "required": True,
                            "total_digits": 7,
                            "fraction_digits": 2,
                        },
                    )
                    valor_franquia: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "valorFranquia",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                            "required": True,
                            "total_digits": 7,
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
                            "total_digits": 7,
                            "fraction_digits": 2,
                        },
                    )
                    codigos_glosa: List[DmTipoGlosa] = field(
                        default_factory=list,
                        metadata={
                            "name": "codigosGlosa",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
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

            @dataclass
            class TotaisPorProtocolo:
                valor_total_informado_por_protocolo: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalInformadoPorProtocolo",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                valor_total_processado_por_protocolo: Optional[Decimal] = (
                    field(
                        default=None,
                        metadata={
                            "name": "valorTotalProcessadoPorProtocolo",
                            "type": "Element",
                            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                            "required": True,
                            "total_digits": 10,
                            "fraction_digits": 2,
                        },
                    )
                )
                valor_total_glosa_por_protocolo: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalGlosaPorProtocolo",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                valor_total_franquia_por_protocolo: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalFranquiaPorProtocolo",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                valor_total_liberado_por_protocolo: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorTotalLiberadoPorProtocolo",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )

        @dataclass
        class TotaisPorData:
            valor_brutonformado_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorBrutonformadoPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_bruto_processado_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorBrutoProcessadoPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_bruto_glosa_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorBrutoGlosaPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_bruto_franquia_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorBrutoFranquiaPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_bruto_liberado_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorBrutoLiberadoPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )

        @dataclass
        class DebCredPorDataPagamento:
            descontos: List[CtDescontos] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_occurs": 1,
                },
            )

        @dataclass
        class TotalLiquidoPorData:
            valor_total_debitos_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorTotalDebitosPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_total_creditos_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorTotalCreditosPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_final_areceber_por_data: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorFinalAReceberPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )

    @dataclass
    class TotaisBrutoDemonstrativo:
        valor_informado_por_demonstrativo_data: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorInformadoPorDemonstrativoData",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )
        valorl_processado_por_demonstrativo: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorlProcessadoPorDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )
        valorl_glosa_por_demonstrativo: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorlGlosaPorDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )
        valo_franquia_por_demonstrativo: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valoFranquiaPorDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )
        valor_liberado_por_demonstrativo: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorLiberadoPorDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )

    @dataclass
    class DebCredDemonstrativo:
        descontos: List[CtDescontos] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

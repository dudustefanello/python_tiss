from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_dados_resumo_demonstrativo import CtDadosResumoDemonstrativo
from tiss.ct_demonstrativo_cabecalho import CtDemonstrativoCabecalho
from tiss.ct_descontos import CtDescontos
from tiss.ct_pagamento_dados import CtPagamentoDados

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmDemonstrativoPagamento:
    class Meta:
        name = "ctm_demonstrativoPagamento"

    cabecalho_demonstrativo: Optional[CtDemonstrativoCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_contratado: Optional["CtmDemonstrativoPagamento.DadosContratado"] = (
        field(
            default=None,
            metadata={
                "name": "dadosContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    pagamentos: Optional["CtmDemonstrativoPagamento.Pagamentos"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    totais_demonstrativo: Optional[
        "CtmDemonstrativoPagamento.TotaisDemonstrativo"
    ] = field(
        default=None,
        metadata={
            "name": "totaisDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    class DadosContratado:
        dados_prestador: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "dadosPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        cnes: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNES",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 7,
            },
        )

    @dataclass
    class Pagamentos:
        pagamentos_por_data: List[
            "CtmDemonstrativoPagamento.Pagamentos.PagamentosPorData"
        ] = field(
            default_factory=list,
            metadata={
                "name": "pagamentosPorData",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

        @dataclass
        class PagamentosPorData:
            dados_pagamento: Optional[CtPagamentoDados] = field(
                default=None,
                metadata={
                    "name": "dadosPagamento",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            dados_resumo: Optional[
                "CtmDemonstrativoPagamento.Pagamentos.PagamentosPorData.DadosResumo"
            ] = field(
                default=None,
                metadata={
                    "name": "dadosResumo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            totais_brutos_por_data: Optional[
                "CtmDemonstrativoPagamento.Pagamentos.PagamentosPorData.TotaisBrutosPorData"
            ] = field(
                default=None,
                metadata={
                    "name": "totaisBrutosPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            debitos_creditos_por_data: Optional[
                "CtmDemonstrativoPagamento.Pagamentos.PagamentosPorData.DebitosCreditosPorData"
            ] = field(
                default=None,
                metadata={
                    "name": "debitosCreditosPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            totais_liquidos_por_data: Optional[
                "CtmDemonstrativoPagamento.Pagamentos.PagamentosPorData.TotaisLiquidosPorData"
            ] = field(
                default=None,
                metadata={
                    "name": "totaisLiquidosPorData",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )

            @dataclass
            class DadosResumo:
                relacao_protocolos: List[CtDadosResumoDemonstrativo] = field(
                    default_factory=list,
                    metadata={
                        "name": "relacaoProtocolos",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "min_occurs": 1,
                    },
                )

            @dataclass
            class TotaisBrutosPorData:
                total_informado_por_data: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "totalInformadoPorData",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                total_processado_por_data: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "totalProcessadoPorData",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                tota_liberado_por_data: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "totaLiberadoPorData",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                total_glosa_por_data: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "totalGlosaPorData",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )

            @dataclass
            class DebitosCreditosPorData:
                debitos_creditos: List[CtDescontos] = field(
                    default_factory=list,
                    metadata={
                        "name": "debitosCreditos",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "min_occurs": 1,
                    },
                )

            @dataclass
            class TotaisLiquidosPorData:
                total_debitos_por_data: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "totalDebitosPorData",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                total_creditos_por_data: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "totalCreditosPorData",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )
                liquido_por_data: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "liquidoPorData",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )

    @dataclass
    class TotaisDemonstrativo:
        totais_brutos_demonstrativo: Optional[
            "CtmDemonstrativoPagamento.TotaisDemonstrativo.TotaisBrutosDemonstrativo"
        ] = field(
            default=None,
            metadata={
                "name": "totaisBrutosDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        debitos_creditos_demonstrativo: List[CtDescontos] = field(
            default_factory=list,
            metadata={
                "name": "debitosCreditosDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        totais_liquidos_demonstrativo: Optional[
            "CtmDemonstrativoPagamento.TotaisDemonstrativo.TotaisLiquidosDemonstrativo"
        ] = field(
            default=None,
            metadata={
                "name": "totaisLiquidosDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class TotaisBrutosDemonstrativo:
            valor_informado_bruto: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorInformadoBruto",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_processado_bruto: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorProcessadoBruto",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_liberado_bruto: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorLiberadoBruto",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_glosa_bruto: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorGlosaBruto",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )

        @dataclass
        class TotaisLiquidosDemonstrativo:
            total_debitos_demonstrativo: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "totalDebitosDemonstrativo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            total_creditosdemonstrativo: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "totalCreditosdemonstrativo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )
            valor_liberado_demonstrativo: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorLiberadoDemonstrativo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 10,
                    "fraction_digits": 2,
                },
            )

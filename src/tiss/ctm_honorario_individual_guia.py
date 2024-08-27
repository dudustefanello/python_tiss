from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_guia_cabecalho import CtGuiaCabecalho
from tiss.ct_procedimento_executado_honor_indiv import (
    CtProcedimentoExecutadoHonorIndiv,
)
from tiss.dm_sim_nao import DmSimNao
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmHonorarioIndividualGuia:
    class Meta:
        name = "ctm_honorarioIndividualGuia"

    cabecalho_guia: Optional[CtGuiaCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    guia_solic_internacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "guiaSolicInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    beneficiario: Optional["CtmHonorarioIndividualGuia.Beneficiario"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    local_contratado: Optional[
        "CtmHonorarioIndividualGuia.LocalContratado"
    ] = field(
        default=None,
        metadata={
            "name": "localContratado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_contratado_executante: Optional[
        "CtmHonorarioIndividualGuia.DadosContratadoExecutante"
    ] = field(
        default=None,
        metadata={
            "name": "dadosContratadoExecutante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_internacao: Optional[
        "CtmHonorarioIndividualGuia.DadosInternacao"
    ] = field(
        default=None,
        metadata={
            "name": "dadosInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    procedimentos_realizados: Optional[
        "CtmHonorarioIndividualGuia.ProcedimentosRealizados"
    ] = field(
        default=None,
        metadata={
            "name": "procedimentosRealizados",
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
    valor_total_honorarios: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalHonorarios",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    data_emissao_guia: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEmissaoGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    assinatura_digital_guia: Optional[Signature1] = field(
        default=None,
        metadata={
            "name": "assinaturaDigitalGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class Beneficiario:
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
        atendimento_rn: Optional[DmSimNao] = field(
            default=None,
            metadata={
                "name": "atendimentoRN",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

    @dataclass
    class LocalContratado:
        codigo_contratado: Optional[
            "CtmHonorarioIndividualGuia.LocalContratado.CodigoContratado"
        ] = field(
            default=None,
            metadata={
                "name": "codigoContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        nome_contratado: Optional[str] = field(
            default=None,
            metadata={
                "name": "nomeContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 70,
            },
        )
        cnes: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 7,
            },
        )

        @dataclass
        class CodigoContratado:
            codigo_na_operadora: Optional[str] = field(
                default=None,
                metadata={
                    "name": "codigoNaOperadora",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 14,
                },
            )
            cnpj_local_executante: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cnpjLocalExecutante",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "pattern": r"[0-9]{14}",
                },
            )

    @dataclass
    class DadosContratadoExecutante:
        codigona_operadora: Optional[str] = field(
            default=None,
            metadata={
                "name": "codigonaOperadora",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 14,
            },
        )
        cnes_contratado_executante: Optional[str] = field(
            default=None,
            metadata={
                "name": "cnesContratadoExecutante",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 7,
            },
        )

    @dataclass
    class DadosInternacao:
        data_inicio_faturamento: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataInicioFaturamento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        data_fim_faturamento: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataFimFaturamento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

    @dataclass
    class ProcedimentosRealizados:
        procedimento_realizado: List[CtProcedimentoExecutadoHonorIndiv] = (
            field(
                default_factory=list,
                metadata={
                    "name": "procedimentoRealizado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_occurs": 1,
                },
            )
        )

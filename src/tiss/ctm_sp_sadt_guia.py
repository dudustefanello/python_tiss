from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_autorizacao_sadt import CtAutorizacaoSadt
from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_contratado_profissional_dados import CtContratadoProfissionalDados
from tiss.ct_guia_cabecalho import CtGuiaCabecalho
from tiss.ct_guia_valor_total import CtGuiaValorTotal
from tiss.ct_outras_despesas import CtOutrasDespesas
from tiss.ct_procedimento_executado_sadt import CtProcedimentoExecutadoSadt
from tiss.ctm_sp_sadt_atendimento import CtmSpSadtAtendimento
from tiss.dm_carater_atendimento import DmCaraterAtendimento
from tiss.dm_cob_esp import DmCobEsp
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmSpSadtGuia:
    class Meta:
        name = "ctm_sp-sadtGuia"

    cabecalho_guia: Optional["CtmSpSadtGuia.CabecalhoGuia"] = field(
        default=None,
        metadata={
            "name": "cabecalhoGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_autorizacao: Optional[CtAutorizacaoSadt] = field(
        default=None,
        metadata={
            "name": "dadosAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    dados_beneficiario: Optional[CtBeneficiarioDados] = field(
        default=None,
        metadata={
            "name": "dadosBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_solicitante: Optional["CtmSpSadtGuia.DadosSolicitante"] = field(
        default=None,
        metadata={
            "name": "dadosSolicitante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_solicitacao: Optional["CtmSpSadtGuia.DadosSolicitacao"] = field(
        default=None,
        metadata={
            "name": "dadosSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_executante: Optional["CtmSpSadtGuia.DadosExecutante"] = field(
        default=None,
        metadata={
            "name": "dadosExecutante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_atendimento: Optional[CtmSpSadtAtendimento] = field(
        default=None,
        metadata={
            "name": "dadosAtendimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    procedimentos_executados: Optional[
        "CtmSpSadtGuia.ProcedimentosExecutados"
    ] = field(
        default=None,
        metadata={
            "name": "procedimentosExecutados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    outras_despesas: Optional[CtOutrasDespesas] = field(
        default=None,
        metadata={
            "name": "outrasDespesas",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
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
    valor_total: Optional[CtGuiaValorTotal] = field(
        default=None,
        metadata={
            "name": "valorTotal",
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
    class CabecalhoGuia(CtGuiaCabecalho):
        guia_principal: Optional[str] = field(
            default=None,
            metadata={
                "name": "guiaPrincipal",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 20,
            },
        )

    @dataclass
    class DadosSolicitante:
        contratado_solicitante: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "contratadoSolicitante",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        nome_contratado_solicitante: Optional[str] = field(
            default=None,
            metadata={
                "name": "nomeContratadoSolicitante",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 70,
            },
        )
        profissional_solicitante: Optional[CtContratadoProfissionalDados] = (
            field(
                default=None,
                metadata={
                    "name": "profissionalSolicitante",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
        )

    @dataclass
    class DadosSolicitacao:
        data_solicitacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataSolicitacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        carater_atendimento: Optional[DmCaraterAtendimento] = field(
            default=None,
            metadata={
                "name": "caraterAtendimento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        indicacao_clinica: Optional[str] = field(
            default=None,
            metadata={
                "name": "indicacaoClinica",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 500,
            },
        )
        ind_cob_especial: Optional[DmCobEsp] = field(
            default=None,
            metadata={
                "name": "indCobEspecial",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

    @dataclass
    class DadosExecutante:
        contratado_executante: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "contratadoExecutante",
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
    class ProcedimentosExecutados:
        procedimento_executado: List[CtProcedimentoExecutadoSadt] = field(
            default_factory=list,
            metadata={
                "name": "procedimentoExecutado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_autorizacao_internacao import CtAutorizacaoInternacao
from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_guia_cabecalho import CtGuiaCabecalho
from tiss.ct_guia_valor_total import CtGuiaValorTotal
from tiss.ct_outras_despesas import CtOutrasDespesas
from tiss.ct_procedimento_executado_int import CtProcedimentoExecutadoInt
from tiss.ctm_internacao_dados import CtmInternacaoDados
from tiss.ctm_internacao_dados_saida import CtmInternacaoDadosSaida
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmInternacaoResumoGuia:
    class Meta:
        name = "ctm_internacaoResumoGuia"

    cabecalho_guia: Optional[CtGuiaCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_guia_solicitacao_internacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaSolicitacaoInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    dados_autorizacao: Optional[CtAutorizacaoInternacao] = field(
        default=None,
        metadata={
            "name": "dadosAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    dados_executante: Optional["CtmInternacaoResumoGuia.DadosExecutante"] = (
        field(
            default=None,
            metadata={
                "name": "dadosExecutante",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    dados_internacao: Optional[CtmInternacaoDados] = field(
        default=None,
        metadata={
            "name": "dadosInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_saida_internacao: Optional[CtmInternacaoDadosSaida] = field(
        default=None,
        metadata={
            "name": "dadosSaidaInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    procedimentos_executados: Optional[
        "CtmInternacaoResumoGuia.ProcedimentosExecutados"
    ] = field(
        default=None,
        metadata={
            "name": "procedimentosExecutados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
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
    assinatura_digital_guia: Optional[Signature1] = field(
        default=None,
        metadata={
            "name": "assinaturaDigitalGuia",
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
        procedimento_executado: List[CtProcedimentoExecutadoInt] = field(
            default_factory=list,
            metadata={
                "name": "procedimentoExecutado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

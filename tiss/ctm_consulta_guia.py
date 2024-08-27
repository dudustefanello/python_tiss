from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_contratado_profissional_dados import CtContratadoProfissionalDados
from tiss.ct_guia_cabecalho import CtGuiaCabecalho
from tiss.ctm_consulta_atendimento import CtmConsultaAtendimento
from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao
from tiss.dm_indicador_acidente import DmIndicadorAcidente
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmConsultaGuia:
    class Meta:
        name = "ctm_consultaGuia"

    cabecalho_consulta: Optional[CtGuiaCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoConsulta",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    ausencia_cod_validacao: Optional[DmAusenciaCodValidacao] = field(
        default=None,
        metadata={
            "name": "ausenciaCodValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    cod_validacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "codValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 10,
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
    contratado_executante: Optional["CtmConsultaGuia.ContratadoExecutante"] = (
        field(
            default=None,
            metadata={
                "name": "contratadoExecutante",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    profissional_executante: Optional[CtContratadoProfissionalDados] = field(
        default=None,
        metadata={
            "name": "profissionalExecutante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    indicacao_acidente: Optional[DmIndicadorAcidente] = field(
        default=None,
        metadata={
            "name": "indicacaoAcidente",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_atendimento: Optional[CtmConsultaAtendimento] = field(
        default=None,
        metadata={
            "name": "dadosAtendimento",
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
    assinatura_digital_guia: Optional[Signature1] = field(
        default=None,
        metadata={
            "name": "assinaturaDigitalGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class ContratadoExecutante(CtContratadoDados):
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

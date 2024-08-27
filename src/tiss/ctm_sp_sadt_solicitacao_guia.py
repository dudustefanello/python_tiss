from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_contratado_profissional_dados import CtContratadoProfissionalDados
from tiss.ct_guia_cabecalho import CtGuiaCabecalho
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.ctm_anexo_solicitacao_opme import CtmAnexoSolicitacaoOpme
from tiss.ctm_anexo_solicitacao_quimio import CtmAnexoSolicitacaoQuimio
from tiss.ctm_anexo_solicitacao_radio import CtmAnexoSolicitacaoRadio
from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao
from tiss.dm_carater_atendimento import DmCaraterAtendimento
from tiss.dm_cob_esp import DmCobEsp
from tiss.dm_etapas_autorizacao import DmEtapasAutorizacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmSpSadtSolicitacaoGuia:
    class Meta:
        name = "ctm_sp-sadtSolicitacaoGuia"

    cabecalho_solicitacao: Optional[CtGuiaCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_guia_principal: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaPrincipal",
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
    tipo_etapa_autorizacao: Optional[DmEtapasAutorizacao] = field(
        default=None,
        metadata={
            "name": "tipoEtapaAutorizacao",
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
    dados_solicitante: Optional[
        "CtmSpSadtSolicitacaoGuia.DadosSolicitante"
    ] = field(
        default=None,
        metadata={
            "name": "dadosSolicitante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    data_solicitacao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataSolicitacao",
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
    cobertura_especial: Optional[DmCobEsp] = field(
        default=None,
        metadata={
            "name": "coberturaEspecial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    procedimentos_solicitados: List[
        "CtmSpSadtSolicitacaoGuia.ProcedimentosSolicitados"
    ] = field(
        default_factory=list,
        metadata={
            "name": "procedimentosSolicitados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
        },
    )
    dados_executante: Optional["CtmSpSadtSolicitacaoGuia.DadosExecutante"] = (
        field(
            default=None,
            metadata={
                "name": "dadosExecutante",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )
    anexo_clinico: Optional["CtmSpSadtSolicitacaoGuia.AnexoClinico"] = field(
        default=None,
        metadata={
            "name": "anexoClinico",
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
    class ProcedimentosSolicitados:
        procedimento: Optional[CtProcedimentoDados] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        quantidade_solicitada: Optional[int] = field(
            default=None,
            metadata={
                "name": "quantidadeSolicitada",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 3,
            },
        )

    @dataclass
    class DadosExecutante:
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
    class AnexoClinico:
        solicitacao_quimioterapia: Optional[CtmAnexoSolicitacaoQuimio] = field(
            default=None,
            metadata={
                "name": "solicitacaoQuimioterapia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        solicitacao_radioterapia: Optional[CtmAnexoSolicitacaoRadio] = field(
            default=None,
            metadata={
                "name": "solicitacaoRadioterapia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        solicitacao_opme: Optional[CtmAnexoSolicitacaoOpme] = field(
            default=None,
            metadata={
                "name": "solicitacaoOPME",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

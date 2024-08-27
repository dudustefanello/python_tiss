from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_contratado_profissional_dados import CtContratadoProfissionalDados
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.ctm_anexo_solicitacao_opme import CtmAnexoSolicitacaoOpme
from tiss.ctm_anexo_solicitacao_quimio import CtmAnexoSolicitacaoQuimio
from tiss.ctm_anexo_solicitacao_radio import CtmAnexoSolicitacaoRadio
from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao
from tiss.dm_carater_atendimento import DmCaraterAtendimento
from tiss.dm_etapas_autorizacao import DmEtapasAutorizacao
from tiss.dm_indicador_acidente import DmIndicadorAcidente
from tiss.dm_regime_internacao import DmRegimeInternacao
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_internacao import DmTipoInternacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmInternacaoSolicitacaoGuia:
    class Meta:
        name = "ctm_internacaoSolicitacaoGuia"

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
    identificacao_solicitante: Optional[
        "CtmInternacaoSolicitacaoGuia.IdentificacaoSolicitante"
    ] = field(
        default=None,
        metadata={
            "name": "identificacaoSolicitante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_hospital_solicitado: Optional[
        "CtmInternacaoSolicitacaoGuia.DadosHospitalSolicitado"
    ] = field(
        default=None,
        metadata={
            "name": "dadosHospitalSolicitado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_internacao: Optional[
        "CtmInternacaoSolicitacaoGuia.DadosInternacao"
    ] = field(
        default=None,
        metadata={
            "name": "dadosInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    hipoteses_diagnosticas: Optional[
        "CtmInternacaoSolicitacaoGuia.HipotesesDiagnosticas"
    ] = field(
        default=None,
        metadata={
            "name": "hipotesesDiagnosticas",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    procedimentos_solicitados: List[
        "CtmInternacaoSolicitacaoGuia.ProcedimentosSolicitados"
    ] = field(
        default_factory=list,
        metadata={
            "name": "procedimentosSolicitados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
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
    observacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    anexo_clinico: Optional["CtmInternacaoSolicitacaoGuia.AnexoClinico"] = (
        field(
            default=None,
            metadata={
                "name": "anexoClinico",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )

    @dataclass
    class IdentificacaoSolicitante:
        dados_do_contratado: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "dadosDoContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        dados_profissional_contratado: Optional[
            CtContratadoProfissionalDados
        ] = field(
            default=None,
            metadata={
                "name": "dadosProfissionalContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

    @dataclass
    class DadosHospitalSolicitado:
        codigo_indicadona_operadora: Optional[str] = field(
            default=None,
            metadata={
                "name": "codigoIndicadonaOperadora",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 14,
            },
        )
        nome_contratado_indicado: Optional[str] = field(
            default=None,
            metadata={
                "name": "nomeContratadoIndicado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 70,
            },
        )
        data_sugerida_internacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataSugeridaInternacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

    @dataclass
    class DadosInternacao:
        carater_atendimento: Optional[DmCaraterAtendimento] = field(
            default=None,
            metadata={
                "name": "caraterAtendimento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        tipo_internacao: Optional[DmTipoInternacao] = field(
            default=None,
            metadata={
                "name": "tipoInternacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        regime_internacao: Optional[DmRegimeInternacao] = field(
            default=None,
            metadata={
                "name": "regimeInternacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        qt_diarias_solicitadas: Optional[int] = field(
            default=None,
            metadata={
                "name": "qtDiariasSolicitadas",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 2,
            },
        )
        indicador_opme: Optional[DmSimNao] = field(
            default=None,
            metadata={
                "name": "indicadorOPME",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        indicador_quimio: Optional[DmSimNao] = field(
            default=None,
            metadata={
                "name": "indicadorQuimio",
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
                "required": True,
                "min_length": 1,
                "max_length": 500,
            },
        )

    @dataclass
    class HipotesesDiagnosticas:
        diagnostico_cid: List[str] = field(
            default_factory=list,
            metadata={
                "name": "diagnosticoCID",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 4,
                "min_length": 1,
                "max_length": 4,
            },
        )
        indicador_acidente: Optional[DmIndicadorAcidente] = field(
            default=None,
            metadata={
                "name": "indicadorAcidente",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
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

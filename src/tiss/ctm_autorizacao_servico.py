from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_autorizacao_dados import CtAutorizacaoDados
from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_procedimento_autorizado import CtProcedimentoAutorizado
from tiss.ctm_autorizacao_quimio import CtmAutorizacaoQuimio
from tiss.ctm_autorizacao_radio import CtmAutorizacaoRadio
from tiss.dm_etapas_autorizacao import DmEtapasAutorizacao
from tiss.dm_status_solicitacao import DmStatusSolicitacao
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAutorizacaoServico:
    class Meta:
        name = "ctm_autorizacaoServico"

    dados_autorizacao: Optional[CtAutorizacaoDados] = field(
        default=None,
        metadata={
            "name": "dadosAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    nome_beneficiario: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    nome_social_beneficiario: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeSocialBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prestador_autorizado: Optional[
        "CtmAutorizacaoServico.PrestadorAutorizado"
    ] = field(
        default=None,
        metadata={
            "name": "prestadorAutorizado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    status_solicitacao: Optional[DmStatusSolicitacao] = field(
        default=None,
        metadata={
            "name": "statusSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    motivos_negativa: Optional["CtmAutorizacaoServico.MotivosNegativa"] = (
        field(
            default=None,
            metadata={
                "name": "motivosNegativa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )
    servicos_autorizados: Optional[
        "CtmAutorizacaoServico.ServicosAutorizados"
    ] = field(
        default=None,
        metadata={
            "name": "servicosAutorizados",
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
            "max_length": 1000,
        },
    )
    autorizacao_quimio: Optional[CtmAutorizacaoQuimio] = field(
        default=None,
        metadata={
            "name": "autorizacaoQuimio",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    autorizacao_radio: Optional[CtmAutorizacaoRadio] = field(
        default=None,
        metadata={
            "name": "autorizacaoRadio",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class PrestadorAutorizado:
        dados_contratado: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "dadosContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        cnes_contratado: Optional[str] = field(
            default=None,
            metadata={
                "name": "cnesContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 7,
            },
        )

    @dataclass
    class MotivosNegativa:
        codigo_glosa: List[DmTipoGlosa] = field(
            default_factory=list,
            metadata={
                "name": "codigoGlosa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

    @dataclass
    class ServicosAutorizados:
        servico_autorizado: List[CtProcedimentoAutorizado] = field(
            default_factory=list,
            metadata={
                "name": "servicoAutorizado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

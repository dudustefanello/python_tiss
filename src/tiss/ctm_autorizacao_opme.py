from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ct_autorizacao_dados import CtAutorizacaoDados
from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_procedimento_autorizado import CtProcedimentoAutorizado
from tiss.dm_status_solicitacao import DmStatusSolicitacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAutorizacaoOpme:
    class Meta:
        name = "ctm_autorizacaoOPME"

    dados_autorizacao: Optional[CtAutorizacaoDados] = field(
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
    nomebeneficiario: Optional[str] = field(
        default=None,
        metadata={
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
    status_solicitacao: Optional[DmStatusSolicitacao] = field(
        default=None,
        metadata={
            "name": "statusSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    motivos_negativa: Optional["CtmAutorizacaoOpme.MotivosNegativa"] = field(
        default=None,
        metadata={
            "name": "motivosNegativa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    prestador_autorizado: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "prestadorAutorizado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    servicos_autorizados_opme: List[CtProcedimentoAutorizado] = field(
        default_factory=list,
        metadata={
            "name": "servicosAutorizadosOPME",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class MotivosNegativa:
        motivo_negativa: List[CtMotivoGlosa] = field(
            default_factory=list,
            metadata={
                "name": "motivoNegativa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

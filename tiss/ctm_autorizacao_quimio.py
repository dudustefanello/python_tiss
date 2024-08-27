from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_autorizacao_dados import CtAutorizacaoDados
from tiss.ct_dados_complementares_beneficiario import (
    CtDadosComplementaresBeneficiario,
)
from tiss.ct_diagnostico_oncologico import CtDiagnosticoOncologico
from tiss.ct_drogas_solicitadas import CtDrogasSolicitadas
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ctm_anexo_solicitante import CtmAnexoSolicitante
from tiss.dm_metastase import DmMetastase
from tiss.dm_nodulo import DmNodulo
from tiss.dm_status_solicitacao import DmStatusSolicitacao
from tiss.dm_tipo_quimioterapia import DmTipoQuimioterapia
from tiss.dm_tumor import DmTumor

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAutorizacaoQuimio:
    class Meta:
        name = "ctm_autorizacaoQuimio"

    dados_autorizacao: Optional[CtAutorizacaoDados] = field(
        default=None,
        metadata={
            "name": "dadosAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
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
    status_solicitacao: Optional[DmStatusSolicitacao] = field(
        default=None,
        metadata={
            "name": "statusSolicitacao",
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
    dados_complementares_beneficiario: Optional[
        CtDadosComplementaresBeneficiario
    ] = field(
        default=None,
        metadata={
            "name": "dadosComplementaresBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    medico_solicitante: Optional[CtmAnexoSolicitante] = field(
        default=None,
        metadata={
            "name": "medicoSolicitante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    diagnostico_oncologico_quimioterapia: Optional[
        "CtmAutorizacaoQuimio.DiagnosticoOncologicoQuimioterapia"
    ] = field(
        default=None,
        metadata={
            "name": "diagnosticoOncologicoQuimioterapia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    drogas_solicitadas: Optional["CtmAutorizacaoQuimio.DrogasSolicitadas"] = (
        field(
            default=None,
            metadata={
                "name": "drogasSolicitadas",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    tratamentos_anteriores: Optional[
        "CtmAutorizacaoQuimio.TratamentosAnteriores"
    ] = field(
        default=None,
        metadata={
            "name": "tratamentosAnteriores",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    numero_ciclos: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroCiclos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 2,
        },
    )
    ciclo_atual: Optional[int] = field(
        default=None,
        metadata={
            "name": "cicloAtual",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 2,
        },
    )
    dias_ciclo_atual: Optional[int] = field(
        default=None,
        metadata={
            "name": "diasCicloAtual",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    intervalo_ciclos: Optional[int] = field(
        default=None,
        metadata={
            "name": "intervaloCiclos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    motivos_negativa: Optional["CtmAutorizacaoQuimio.MotivosNegativa"] = field(
        default=None,
        metadata={
            "name": "motivosNegativa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class DiagnosticoOncologicoQuimioterapia:
        diag_quimio: Optional[CtDiagnosticoOncologico] = field(
            default=None,
            metadata={
                "name": "diagQuimio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        tumor: Optional[DmTumor] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        nodulo: Optional[DmNodulo] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        metastase: Optional[DmMetastase] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        tipo_quimioterapia: Optional[DmTipoQuimioterapia] = field(
            default=None,
            metadata={
                "name": "tipoQuimioterapia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        plano_terapeutico: Optional[str] = field(
            default=None,
            metadata={
                "name": "planoTerapeutico",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 1000,
            },
        )

    @dataclass
    class DrogasSolicitadas:
        droga_solicitada: List[CtDrogasSolicitadas] = field(
            default_factory=list,
            metadata={
                "name": "drogaSolicitada",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

    @dataclass
    class TratamentosAnteriores:
        cirurgia: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 40,
            },
        )
        datacirurgia: Optional[XmlDate] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        area_irradiada: Optional[str] = field(
            default=None,
            metadata={
                "name": "areaIrradiada",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 40,
            },
        )
        data_irradiacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataIrradiacao",
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

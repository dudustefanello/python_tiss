from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_autorizacao_dados import CtAutorizacaoDados
from tiss.ct_dados_complementares_beneficiario_radio import (
    CtDadosComplementaresBeneficiarioRadio,
)
from tiss.ct_diagnostico_oncologico import CtDiagnosticoOncologico
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ctm_anexo_solicitante import CtmAnexoSolicitante
from tiss.dm_diagnostico_imagem import DmDiagnosticoImagem
from tiss.dm_status_solicitacao import DmStatusSolicitacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAutorizacaoRadio:
    class Meta:
        name = "ctm_autorizacaoRadio"

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
    status_solicitacao: Optional[DmStatusSolicitacao] = field(
        default=None,
        metadata={
            "name": "statusSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_complementares_beneficiario: Optional[
        CtDadosComplementaresBeneficiarioRadio
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
    diagnostico_oncologico_radio: Optional[
        "CtmAutorizacaoRadio.DiagnosticoOncologicoRadio"
    ] = field(
        default=None,
        metadata={
            "name": "diagnosticoOncologicoRadio",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    tratamentos_anteriores: Optional[
        "CtmAutorizacaoRadio.TratamentosAnteriores"
    ] = field(
        default=None,
        metadata={
            "name": "tratamentosAnteriores",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    numero_campos: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroCampos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    dose_campo: Optional[int] = field(
        default=None,
        metadata={
            "name": "doseCampo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 4,
        },
    )
    dose_total: Optional[int] = field(
        default=None,
        metadata={
            "name": "doseTotal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 4,
        },
    )
    nr_dias: Optional[int] = field(
        default=None,
        metadata={
            "name": "nrDias",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    dt_prevista_inicio: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dtPrevistaInicio",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    motivos_negativa: Optional["CtmAutorizacaoRadio.MotivosNegativa"] = field(
        default=None,
        metadata={
            "name": "motivosNegativa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class DiagnosticoOncologicoRadio:
        diag_radio: Optional[CtDiagnosticoOncologico] = field(
            default=None,
            metadata={
                "name": "diagRadio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        diagnostico_imagem: Optional[DmDiagnosticoImagem] = field(
            default=None,
            metadata={
                "name": "diagnosticoImagem",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
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
        quimioterapia: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 40,
            },
        )
        data_quimioterapia: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataQuimioterapia",
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

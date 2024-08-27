from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_anexo_cabecalho import CtAnexoCabecalho
from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_dados_complementares_beneficiario_radio import (
    CtDadosComplementaresBeneficiarioRadio,
)
from tiss.ct_diagnostico_oncologico import CtDiagnosticoOncologico
from tiss.ctm_anexo_solicitante import CtmAnexoSolicitante
from tiss.dm_diagnostico_imagem import DmDiagnosticoImagem

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAnexoSolicitacaoRadio:
    class Meta:
        name = "ctm_anexoSolicitacaoRadio"

    cabecalho_anexo: Optional[CtAnexoCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoAnexo",
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
        "CtmAnexoSolicitacaoRadio.DiagnosticoOncologicoRadio"
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
        "CtmAnexoSolicitacaoRadio.TratamentosAnteriores"
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

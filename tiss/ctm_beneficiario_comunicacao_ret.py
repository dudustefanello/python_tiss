from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.dm_motivo_saida import DmMotivoSaida
from tiss.dm_tipo_evento import DmTipoEvento
from tiss.dm_tipo_internacao import DmTipoInternacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmBeneficiarioComunicacaoRet:
    class Meta:
        name = "ctm_beneficiarioComunicacaoRet"

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
    tipo_evento: Optional[DmTipoEvento] = field(
        default=None,
        metadata={
            "name": "tipoEvento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_internacao: Optional[
        "CtmBeneficiarioComunicacaoRet.DadosInternacao"
    ] = field(
        default=None,
        metadata={
            "name": "dadosInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class DadosInternacao:
        motivo_encerramento: Optional[DmMotivoSaida] = field(
            default=None,
            metadata={
                "name": "motivoEncerramento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        tipo_internacao: Optional[DmTipoInternacao] = field(
            default=None,
            metadata={
                "name": "tipoInternacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

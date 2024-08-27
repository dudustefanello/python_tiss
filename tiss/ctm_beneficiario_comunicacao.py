from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.dm_motivo_saida import DmMotivoSaida
from tiss.dm_tipo_evento import DmTipoEvento
from tiss.dm_tipo_internacao import DmTipoInternacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmBeneficiarioComunicacao:
    class Meta:
        name = "ctm_beneficiarioComunicacao"

    dados_beneficiario: Optional[CtBeneficiarioDados] = field(
        default=None,
        metadata={
            "name": "dadosBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_evento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEvento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
        "CtmBeneficiarioComunicacao.DadosInternacao"
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

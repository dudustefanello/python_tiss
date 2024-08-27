from dataclasses import dataclass, field
from typing import Optional

from tiss.ctm_beneficiario_comunicacao_ret import CtmBeneficiarioComunicacaoRet
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmBeneficiarioComunicacaoRecibo:
    class Meta:
        name = "ctm_beneficiarioComunicacaoRecibo"

    status_comunicacao: Optional[DmSimNao] = field(
        default=None,
        metadata={
            "name": "statusComunicacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    beneficiario_comunicacao_ret: Optional[CtmBeneficiarioComunicacaoRet] = (
        field(
            default=None,
            metadata={
                "name": "beneficiarioComunicacaoRet",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    codigo_glosa: Optional[DmTipoGlosa] = field(
        default=None,
        metadata={
            "name": "codigoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

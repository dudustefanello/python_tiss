from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ctm_beneficiario_comunicacao_recibo import (
    CtmBeneficiarioComunicacaoRecibo,
)

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtReciboComunicacao:
    class Meta:
        name = "ct_reciboComunicacao"

    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recibo_comunicacao: Optional[CtmBeneficiarioComunicacaoRecibo] = field(
        default=None,
        metadata={
            "name": "reciboComunicacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

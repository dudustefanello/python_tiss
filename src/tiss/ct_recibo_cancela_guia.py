from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_guia_cancelamento_recibo import CtGuiaCancelamentoRecibo
from tiss.ct_motivo_glosa import CtMotivoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtReciboCancelaGuia:
    class Meta:
        name = "ct_reciboCancelaGuia"

    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recibo_cancela_guia: Optional[CtGuiaCancelamentoRecibo] = field(
        default=None,
        metadata={
            "name": "reciboCancelaGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_contratado_dados import CtContratadoDados

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProtocoloSolicitacaoStatus:
    class Meta:
        name = "ct_protocoloSolicitacaoStatus"

    dados_prestador: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )

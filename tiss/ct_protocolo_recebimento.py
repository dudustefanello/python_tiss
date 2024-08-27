from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_protocolo_detalhe import CtProtocoloDetalhe

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProtocoloRecebimento:
    class Meta:
        name = "ct_protocoloRecebimento"

    registro_ans: Optional[str] = field(
        default=None,
        metadata={
            "name": "registroANS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "max_length": 6,
            "pattern": r"[0-9]{6}",
        },
    )
    dados_prestador: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    data_envio_lote: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEnvioLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    detalhe_protocolo: Optional[CtProtocoloDetalhe] = field(
        default=None,
        metadata={
            "name": "detalheProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

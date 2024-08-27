from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_fonte_pagadora import CtFontePagadora
from tiss.ct_protocolo_detalhe_anexo import CtProtocoloDetalheAnexo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProtocoloRecebimentoAnexo:
    class Meta:
        name = "ct_protocoloRecebimentoAnexo"

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
    identificacao_operadora: Optional[CtFontePagadora] = field(
        default=None,
        metadata={
            "name": "identificacaoOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    data_envio_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataEnvioLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    detalhe_protocolo: Optional[CtProtocoloDetalheAnexo] = field(
        default=None,
        metadata={
            "name": "detalheProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

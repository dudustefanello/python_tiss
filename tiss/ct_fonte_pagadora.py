from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtFontePagadora:
    class Meta:
        name = "ct_fontePagadora"

    registro_ans: Optional[str] = field(
        default=None,
        metadata={
            "name": "registroANS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "max_length": 6,
            "pattern": r"[0-9]{6}",
        },
    )
    identificacao_unidade_pagadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "identificacaoUnidadePagadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "pattern": r"[0-9]{14}",
        },
    )

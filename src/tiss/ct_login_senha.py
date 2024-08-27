from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtLoginSenha:
    class Meta:
        name = "ct_loginSenha"

    login_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "loginPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    senha_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "senhaPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        },
    )

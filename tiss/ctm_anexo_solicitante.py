from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAnexoSolicitante:
    class Meta:
        name = "ctm_anexoSolicitante"

    nome_profissional: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeProfissional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    telefone_profissional: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefoneProfissional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 11,
        },
    )
    email_profissional: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailProfissional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 60,
        },
    )

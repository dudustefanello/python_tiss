from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_sexo import DmSexo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDadosComplementaresBeneficiarioRadio:
    class Meta:
        name = "ct_dadosComplementaresBeneficiarioRadio"

    idade: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    sexo: Optional[DmSexo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

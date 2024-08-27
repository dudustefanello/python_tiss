from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_cbos import DmCbos
from tiss.dm_conselho_profissional import DmConselhoProfissional
from tiss.dm_uf import DmUf

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtContratadoProfissionalDados:
    class Meta:
        name = "ct_contratadoProfissionalDados"

    nome_profissional: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeProfissional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 70,
        },
    )
    conselho_profissional: Optional[DmConselhoProfissional] = field(
        default=None,
        metadata={
            "name": "conselhoProfissional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_conselho_profissional: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroConselhoProfissional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 15,
        },
    )
    uf: Optional[DmUf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    cbos: Optional[DmCbos] = field(
        default=None,
        metadata={
            "name": "CBOS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

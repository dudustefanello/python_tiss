from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_cbos import DmCbos
from tiss.dm_conselho_profissional import DmConselhoProfissional
from tiss.dm_grau_part import DmGrauPart
from tiss.dm_uf import DmUf

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtIdentEquipe:
    class Meta:
        name = "ct_identEquipe"

    grau_part: Optional[DmGrauPart] = field(
        default=None,
        metadata={
            "name": "grauPart",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    cod_profissional: Optional["CtIdentEquipe.CodProfissional"] = field(
        default=None,
        metadata={
            "name": "codProfissional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    nome_prof: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeProf",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    conselho: Optional[DmConselhoProfissional] = field(
        default=None,
        metadata={
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

    @dataclass
    class CodProfissional:
        codigo_prestador_na_operadora: Optional[str] = field(
            default=None,
            metadata={
                "name": "codigoPrestadorNaOperadora",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 14,
            },
        )
        cpf_contratado: Optional[str] = field(
            default=None,
            metadata={
                "name": "cpfContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "pattern": r"[0-9]{11}",
            },
        )

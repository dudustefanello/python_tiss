from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_procedimento_dados import CtProcedimentoDados

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtOpmeDados:
    class Meta:
        name = "ct_opmeDados"

    identificacao_opme: Optional[CtProcedimentoDados] = field(
        default=None,
        metadata={
            "name": "identificacaoOPME",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    nome_fabricante: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeFabricante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )

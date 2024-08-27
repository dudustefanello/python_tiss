from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDemonstrativoCabecalho:
    class Meta:
        name = "ct_demonstrativoCabecalho"

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
    numero_demonstrativo: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    nome_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    numero_cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroCNPJ",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "pattern": r"[0-9]{14}",
        },
    )
    data_emissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEmissao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

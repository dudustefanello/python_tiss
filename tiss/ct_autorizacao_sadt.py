from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtAutorizacaoSadt:
    class Meta:
        name = "ct_autorizacaoSADT"

    numero_guia_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )
    data_autorizacao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    senha: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )
    data_validade_senha: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataValidadeSenha",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    ausencia_cod_validacao: Optional[DmAusenciaCodValidacao] = field(
        default=None,
        metadata={
            "name": "ausenciaCodValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    cod_validacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "codValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 10,
        },
    )

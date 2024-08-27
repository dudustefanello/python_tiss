from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.epilogo import Epilogo
from tiss.operadora_prestador import OperadoraPrestador
from tiss.prestador_operadora import PrestadorOperadora
from tiss.signature import Signature

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class MensagemTiss:
    class Meta:
        name = "mensagemTISS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    operadora_para_prestador: Optional[OperadoraPrestador] = field(
        default=None,
        metadata={
            "name": "operadoraParaPrestador",
            "type": "Element",
        },
    )
    prestador_para_operadora: Optional[PrestadorOperadora] = field(
        default=None,
        metadata={
            "name": "prestadorParaOperadora",
            "type": "Element",
        },
    )
    epilogo: Optional[Epilogo] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )

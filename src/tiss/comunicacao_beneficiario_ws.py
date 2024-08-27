from dataclasses import dataclass, field
from typing import Optional

from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.ctm_beneficiario_comunicacao import CtmBeneficiarioComunicacao
from tiss.signature_1 import Signature1

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class ComunicacaoBeneficiarioWs:
    """
    Prestador envia informação sobre internação/alta de beneficiário.
    """

    class Meta:
        name = "comunicacaoBeneficiarioWS"
        namespace = "http://www.ans.gov.br/padroes/tiss/schemas"

    cabecalho: Optional[CabecalhoTransacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    comunicacao_beneficiario: Optional[CtmBeneficiarioComunicacao] = field(
        default=None,
        metadata={
            "name": "comunicacaoBeneficiario",
            "type": "Element",
            "required": True,
        },
    )
    hash: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature1] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
        },
    )

from dataclasses import dataclass, field
from typing import Optional

from tiss.comunicacao_beneficiario_ws import ComunicacaoBeneficiarioWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        comunicacao_beneficiario_ws: Optional[ComunicacaoBeneficiarioWs] = (
            field(
                default=None,
                metadata={
                    "name": "comunicacaoBeneficiarioWS",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
        )

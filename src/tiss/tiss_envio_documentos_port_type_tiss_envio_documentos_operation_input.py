from dataclasses import dataclass, field
from typing import Optional

from tiss.envio_documento_ws import EnvioDocumentoWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationInput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        envio_documento_ws: Optional[EnvioDocumentoWs] = field(
            default=None,
            metadata={
                "name": "envioDocumentoWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

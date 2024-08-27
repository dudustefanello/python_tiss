from dataclasses import dataclass, field
from typing import Optional

from tiss.protocolo_recebimento_ws import ProtocoloRecebimentoWs
from tiss.tiss_fault_ws import TissFaultWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissLoteGuiasPortTypeTissLoteGuiasOperationOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissLoteGuiasPortTypeTissLoteGuiasOperationOutput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        protocolo_recebimento_ws: Optional[ProtocoloRecebimentoWs] = field(
            default=None,
            metadata={
                "name": "protocoloRecebimentoWS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        fault: Optional[
            "TissLoteGuiasPortTypeTissLoteGuiasOperationOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[
                "TissLoteGuiasPortTypeTissLoteGuiasOperationOutput.Body.Fault.Detail"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class Detail:
                tiss_fault_ws: Optional[TissFaultWs] = field(
                    default=None,
                    metadata={
                        "name": "tissFaultWS",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    },
                )

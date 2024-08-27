from dataclasses import dataclass, field
from typing import Optional

from tiss.situacao_protocolo_recurso_ws import SituacaoProtocoloRecursoWs
from tiss.tiss_fault_ws import TissFaultWs

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


@dataclass
class TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional[
        "TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationOutput.Body"
    ] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        situacao_protocolo_recurso_ws: Optional[SituacaoProtocoloRecursoWs] = (
            field(
                default=None,
                metadata={
                    "name": "situacaoProtocoloRecursoWS",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
        )
        fault: Optional[
            "TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationOutput.Body.Fault"
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
                "TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationOutput.Body.Fault.Detail"
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

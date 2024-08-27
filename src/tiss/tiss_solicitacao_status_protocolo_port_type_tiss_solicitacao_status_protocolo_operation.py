from tiss.tiss_solicitacao_status_protocolo_port_type_tiss_solicitacao_status_protocolo_operation_input import (
    TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationInput,
)
from tiss.tiss_solicitacao_status_protocolo_port_type_tiss_solicitacao_status_protocolo_operation_output import (
    TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationInput
    output = TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationOutput

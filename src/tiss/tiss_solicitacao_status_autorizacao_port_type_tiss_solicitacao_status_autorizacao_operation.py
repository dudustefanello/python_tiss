from tiss.tiss_solicitacao_status_autorizacao_port_type_tiss_solicitacao_status_autorizacao_operation_input import (
    TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationInput,
)
from tiss.tiss_solicitacao_status_autorizacao_port_type_tiss_solicitacao_status_autorizacao_operation_output import (
    TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationInput
    output = TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationOutput

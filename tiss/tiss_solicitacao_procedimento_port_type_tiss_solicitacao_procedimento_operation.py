from tiss.tiss_solicitacao_procedimento_port_type_tiss_solicitacao_procedimento_operation_input import (
    TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationInput,
)
from tiss.tiss_solicitacao_procedimento_port_type_tiss_solicitacao_procedimento_operation_output import (
    TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationInput
    output = TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationOutput

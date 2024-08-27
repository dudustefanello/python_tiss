from tiss.tiss_solicitacao_demonstrativo_retorno_port_type_tiss_solicitacao_demonstrativo_retorno_operation_input import (
    TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationInput,
)
from tiss.tiss_solicitacao_demonstrativo_retorno_port_type_tiss_solicitacao_demonstrativo_retorno_operation_output import (
    TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationInput
    output = TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationOutput

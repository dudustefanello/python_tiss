from tiss.tiss_cancela_guia_port_type_tiss_cancela_guia_operation_input import (
    TissCancelaGuiaPortTypeTissCancelaGuiaOperationInput,
)
from tiss.tiss_cancela_guia_port_type_tiss_cancela_guia_operation_output import (
    TissCancelaGuiaPortTypeTissCancelaGuiaOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissCancelaGuiaPortTypeTissCancelaGuiaOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissCancelaGuiaPortTypeTissCancelaGuiaOperationInput
    output = TissCancelaGuiaPortTypeTissCancelaGuiaOperationOutput

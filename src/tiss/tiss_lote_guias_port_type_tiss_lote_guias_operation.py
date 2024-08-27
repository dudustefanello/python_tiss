from tiss.tiss_lote_guias_port_type_tiss_lote_guias_operation_input import (
    TissLoteGuiasPortTypeTissLoteGuiasOperationInput,
)
from tiss.tiss_lote_guias_port_type_tiss_lote_guias_operation_output import (
    TissLoteGuiasPortTypeTissLoteGuiasOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissLoteGuiasPortTypeTissLoteGuiasOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissLoteGuiasPortTypeTissLoteGuiasOperationInput
    output = TissLoteGuiasPortTypeTissLoteGuiasOperationOutput

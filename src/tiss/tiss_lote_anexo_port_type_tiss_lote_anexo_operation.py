from tiss.tiss_lote_anexo_port_type_tiss_lote_anexo_operation_input import (
    TissLoteAnexoPortTypeTissLoteAnexoOperationInput,
)
from tiss.tiss_lote_anexo_port_type_tiss_lote_anexo_operation_output import (
    TissLoteAnexoPortTypeTissLoteAnexoOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissLoteAnexoPortTypeTissLoteAnexoOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissLoteAnexoPortTypeTissLoteAnexoOperationInput
    output = TissLoteAnexoPortTypeTissLoteAnexoOperationOutput

from tiss.tiss_recurso_glosa_port_type_tiss_recurso_glosa_operation_input import (
    TissRecursoGlosaPortTypeTissRecursoGlosaOperationInput,
)
from tiss.tiss_recurso_glosa_port_type_tiss_recurso_glosa_operation_output import (
    TissRecursoGlosaPortTypeTissRecursoGlosaOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissRecursoGlosaPortTypeTissRecursoGlosaOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissRecursoGlosaPortTypeTissRecursoGlosaOperationInput
    output = TissRecursoGlosaPortTypeTissRecursoGlosaOperationOutput

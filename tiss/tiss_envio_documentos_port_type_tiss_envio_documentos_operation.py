from tiss.tiss_envio_documentos_port_type_tiss_envio_documentos_operation_input import (
    TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationInput,
)
from tiss.tiss_envio_documentos_port_type_tiss_envio_documentos_operation_output import (
    TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissEnvioDocumentosPortTypeTissEnvioDocumentosOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationInput
    output = TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationOutput

from tiss.tiss_verifica_elegibilidade_port_type_tiss_verifica_elegibilidade_operation_input import (
    TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationInput,
)
from tiss.tiss_verifica_elegibilidade_port_type_tiss_verifica_elegibilidade_operation_output import (
    TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationInput
    output = TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationOutput

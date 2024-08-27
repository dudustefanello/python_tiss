from tiss.tiss_comunicacao_beneficiario_port_type_tiss_comunicacao_beneficiario_operation_input import (
    TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationInput,
)
from tiss.tiss_comunicacao_beneficiario_port_type_tiss_comunicacao_beneficiario_operation_output import (
    TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationOutput,
)

__NAMESPACE__ = "http://www.ans.gov.br/tiss/ws/tipos/tisscancelaguia/v40100"


class TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperation:
    style = "document"
    transport = "http://schemas.xmlsoap.org/soap/http"
    input = TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationInput
    output = TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationOutput

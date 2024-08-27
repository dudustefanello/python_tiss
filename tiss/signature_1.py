from dataclasses import dataclass

from tiss.signature_type import SignatureType

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class Signature1(SignatureType):
    class Meta:
        name = "Signature"

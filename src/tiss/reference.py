from dataclasses import dataclass

from tiss.reference_type import ReferenceType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Reference(ReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

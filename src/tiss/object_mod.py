from dataclasses import dataclass

from tiss.object_type import ObjectType

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Object(ObjectType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"

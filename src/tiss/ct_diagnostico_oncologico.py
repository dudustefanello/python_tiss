from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.dm_ecog import DmEcog
from tiss.dm_estadiamento import DmEstadiamento
from tiss.dm_finalidade_tratamento import DmFinalidadeTratamento

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDiagnosticoOncologico:
    class Meta:
        name = "ct_diagnosticoOncologico"

    data_diagnostico: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataDiagnostico",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    diagnostico_cid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "diagnosticoCID",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "max_occurs": 4,
            "min_length": 1,
            "max_length": 4,
            "pattern": r"[a-zA-Z0-9]+",
        },
    )
    estadiamento: Optional[DmEstadiamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    finalidade: Optional[DmFinalidadeTratamento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    ecog: Optional[DmEcog] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    diagnostico_hispatologico: Optional[str] = field(
        default=None,
        metadata={
            "name": "diagnosticoHispatologico",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    info_relevantes: Optional[str] = field(
        default=None,
        metadata={
            "name": "infoRelevantes",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 1000,
        },
    )

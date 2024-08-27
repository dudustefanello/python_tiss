from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ctm_autorizacao_opme import CtmAutorizacaoOpme
from tiss.ctm_autorizacao_quimio import CtmAutorizacaoQuimio
from tiss.ctm_autorizacao_radio import CtmAutorizacaoRadio
from tiss.dm_status_protocolo import DmStatusProtocolo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtLoteAnexoStatus:
    """
    Resposta a uma solicitação de situação de protocolo.
    """

    class Meta:
        name = "ct_loteAnexoStatus"

    status_protocolo: Optional[DmStatusProtocolo] = field(
        default=None,
        metadata={
            "name": "statusProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_protocolo: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    data_envio_lote: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEnvioLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    anexos_clinicos: Optional["CtLoteAnexoStatus.AnexosClinicos"] = field(
        default=None,
        metadata={
            "name": "anexosClinicos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class AnexosClinicos:
        anexo_opme: Optional[CtmAutorizacaoOpme] = field(
            default=None,
            metadata={
                "name": "anexoOPME",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        anexo_quimio: Optional[CtmAutorizacaoQuimio] = field(
            default=None,
            metadata={
                "name": "anexoQuimio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        anexo_radio: Optional[CtmAutorizacaoRadio] = field(
            default=None,
            metadata={
                "name": "anexoRadio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ctm_autorizacao_servico import CtmAutorizacaoServico
from tiss.dm_tipo_acomodacao import DmTipoAcomodacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAutorizacaoInternacao:
    class Meta:
        name = "ctm_autorizacaoInternacao"

    autorizacao_dos_servicos: Optional[CtmAutorizacaoServico] = field(
        default=None,
        metadata={
            "name": "autorizacaoDosServicos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_provavel_admissao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataProvavelAdmissao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    qtd_diarias_autorizadas: Optional[int] = field(
        default=None,
        metadata={
            "name": "qtdDiariasAutorizadas",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 3,
        },
    )
    tipo_acomodacao_autorizada: Optional[DmTipoAcomodacao] = field(
        default=None,
        metadata={
            "name": "tipoAcomodacaoAutorizada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

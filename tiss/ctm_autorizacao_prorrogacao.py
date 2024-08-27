from dataclasses import dataclass, field
from typing import Optional

from tiss.ctm_autorizacao_servico import CtmAutorizacaoServico
from tiss.dm_tipo_acomodacao import DmTipoAcomodacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAutorizacaoProrrogacao:
    class Meta:
        name = "ctm_autorizacaoProrrogacao"

    autorizacao_dos_servicos: Optional[CtmAutorizacaoServico] = field(
        default=None,
        metadata={
            "name": "autorizacaoDosServicos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    nome_contratado: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeContratado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 70,
        },
    )
    diarias_autorizadas: Optional[int] = field(
        default=None,
        metadata={
            "name": "diariasAutorizadas",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 3,
        },
    )
    acomodacao_autorizada: Optional[DmTipoAcomodacao] = field(
        default=None,
        metadata={
            "name": "acomodacaoAutorizada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    justificativa_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "justificativaOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 500,
        },
    )

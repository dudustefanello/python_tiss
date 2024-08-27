from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ctm_autorizacao_internacao import CtmAutorizacaoInternacao
from tiss.ctm_autorizacao_prorrogacao import CtmAutorizacaoProrrogacao
from tiss.ctm_autorizacao_servico import CtmAutorizacaoServico
from tiss.cto_autorizacao_servico import CtoAutorizacaoServico

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtSituacaoAutorizacao:
    class Meta:
        name = "ct_situacaoAutorizacao"

    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    autorizacao_internacao: Optional[CtmAutorizacaoInternacao] = field(
        default=None,
        metadata={
            "name": "autorizacaoInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    autorizacao_servico: Optional[CtmAutorizacaoServico] = field(
        default=None,
        metadata={
            "name": "autorizacaoServico",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    autorizacao_prorrogacao: Optional[CtmAutorizacaoProrrogacao] = field(
        default=None,
        metadata={
            "name": "autorizacaoProrrogacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    autorizacao_servico_odonto: Optional[CtoAutorizacaoServico] = field(
        default=None,
        metadata={
            "name": "autorizacaoServicoOdonto",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

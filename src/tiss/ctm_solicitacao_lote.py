from dataclasses import dataclass, field
from typing import Optional

from tiss.ctm_internacao_solicitacao_guia import CtmInternacaoSolicitacaoGuia
from tiss.ctm_prorrogacao_solicitacao_guia import CtmProrrogacaoSolicitacaoGuia
from tiss.ctm_sp_sadt_solicitacao_guia import CtmSpSadtSolicitacaoGuia
from tiss.cto_odonto_solicitacao_guia import CtoOdontoSolicitacaoGuia

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmSolicitacaoLote:
    class Meta:
        name = "ctm_solicitacaoLote"

    solicitacao_sp_sadt: Optional[CtmSpSadtSolicitacaoGuia] = field(
        default=None,
        metadata={
            "name": "solicitacaoSP-SADT",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    solicitacao_internacao: Optional[CtmInternacaoSolicitacaoGuia] = field(
        default=None,
        metadata={
            "name": "solicitacaoInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    solicitacao_prorrogacao: Optional[CtmProrrogacaoSolicitacaoGuia] = field(
        default=None,
        metadata={
            "name": "solicitacaoProrrogacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    solicitacao_odontologia: Optional[CtoOdontoSolicitacaoGuia] = field(
        default=None,
        metadata={
            "name": "solicitacaoOdontologia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

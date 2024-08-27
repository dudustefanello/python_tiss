from dataclasses import dataclass

from tiss.ctm_solicitacao_lote import CtmSolicitacaoLote

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtSolicitacaoProcedimento(CtmSolicitacaoLote):
    class Meta:
        name = "ct_solicitacaoProcedimento"

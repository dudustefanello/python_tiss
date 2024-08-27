from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_guia_cabecalho import CtGuiaCabecalho

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtAutorizacaoSolicitaStatus:
    class Meta:
        name = "ct_autorizacaoSolicitaStatus"

    identificacao_solicitacao: Optional[CtGuiaCabecalho] = field(
        default=None,
        metadata={
            "name": "identificacaoSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_beneficiario: Optional[CtBeneficiarioDados] = field(
        default=None,
        metadata={
            "name": "dadosBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_contratado: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosContratado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ctm_anexo_solicitacao_opme import CtmAnexoSolicitacaoOpme
from tiss.ctm_anexo_solicitacao_quimio import CtmAnexoSolicitacaoQuimio
from tiss.ctm_anexo_solicitacao_radio import CtmAnexoSolicitacaoRadio
from tiss.cto_anexo_situacao_inicial import CtoAnexoSituacaoInicial

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtAnexoLote:
    """
    Estrutura da resposta da operadora a um lote de anexos.
    """

    class Meta:
        name = "ct_anexoLote"

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
    anexos_guias_tiss: Optional["CtAnexoLote.AnexosGuiasTiss"] = field(
        default=None,
        metadata={
            "name": "AnexosGuiasTISS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class AnexosGuiasTiss:
        anexo_situacao_inicial: List[CtoAnexoSituacaoInicial] = field(
            default_factory=list,
            metadata={
                "name": "anexoSituacaoInicial",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
            },
        )
        anexo_solicitacao_radio: Optional[CtmAnexoSolicitacaoRadio] = field(
            default=None,
            metadata={
                "name": "anexoSolicitacaoRadio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        anexo_solicitacao_quimio: Optional[CtmAnexoSolicitacaoQuimio] = field(
            default=None,
            metadata={
                "name": "anexoSolicitacaoQuimio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        anexo_solicitacao_opme: Optional[CtmAnexoSolicitacaoOpme] = field(
            default=None,
            metadata={
                "name": "anexoSolicitacaoOPME",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

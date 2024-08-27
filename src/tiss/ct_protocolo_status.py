from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_lote_status import CtLoteStatus
from tiss.ct_motivo_glosa import CtMotivoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProtocoloStatus:
    """
    Estrutura utilizada na resposta da operadora sobre a situação do protocolo.
    """

    class Meta:
        name = "ct_protocoloStatus"

    identificacao_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "identificacaoOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "max_length": 6,
            "pattern": r"[0-9]{6}",
        },
    )
    dados_prestador: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    lote: Optional["CtProtocoloStatus.Lote"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class Lote:
        detalhe_lote: Optional[CtLoteStatus] = field(
            default=None,
            metadata={
                "name": "detalheLote",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        mensagem_erro: Optional[CtMotivoGlosa] = field(
            default=None,
            metadata={
                "name": "mensagemErro",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

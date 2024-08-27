from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ctm_demonstrativo_analise_conta import CtmDemonstrativoAnaliseConta
from tiss.ctm_demonstrativo_pagamento import CtmDemonstrativoPagamento
from tiss.cto_demonstrativo_odontologia import CtoDemonstrativoOdontologia
from tiss.dm_status_protocolo import DmStatusProtocolo
from tiss.dm_tipo_demonstrativo import DmTipoDemonstrativo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDemonstrativoRetorno:
    class Meta:
        name = "ct_demonstrativoRetorno"

    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    demonstrativo_analise_conta: List[CtmDemonstrativoAnaliseConta] = field(
        default_factory=list,
        metadata={
            "name": "demonstrativoAnaliseConta",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "max_occurs": 30,
        },
    )
    demonstrativo_pagamento: Optional[CtmDemonstrativoPagamento] = field(
        default=None,
        metadata={
            "name": "demonstrativoPagamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    demonstrativo_pagamento_odonto: Optional[CtoDemonstrativoOdontologia] = (
        field(
            default=None,
            metadata={
                "name": "demonstrativoPagamentoOdonto",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )
    situacao_demonstrativo_retorno: Optional[
        "CtDemonstrativoRetorno.SituacaoDemonstrativoRetorno"
    ] = field(
        default=None,
        metadata={
            "name": "situacaoDemonstrativoRetorno",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class SituacaoDemonstrativoRetorno:
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
        protocolo_solicitacao_demonstrativo: Optional[str] = field(
            default=None,
            metadata={
                "name": "protocoloSolicitacaoDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 12,
            },
        )
        tipo_demonstrativo: Optional[DmTipoDemonstrativo] = field(
            default=None,
            metadata={
                "name": "tipoDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        data_situacao_demonstrativo: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataSituacaoDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        situacao_demonstrativo: Optional[DmStatusProtocolo] = field(
            default=None,
            metadata={
                "name": "situacaoDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

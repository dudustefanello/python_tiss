from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.dm_tipo_demonstrativo_pagamento import DmTipoDemonstrativoPagamento

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtDemonstrativoSolicitacao:
    """
    Estrutura para solicitação de demonstrativo de pagamento.
    """

    class Meta:
        name = "ct_demonstrativoSolicitacao"

    demonstrativo_pagamento: Optional[
        "CtDemonstrativoSolicitacao.DemonstrativoPagamento"
    ] = field(
        default=None,
        metadata={
            "name": "demonstrativoPagamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    demonstrativo_analise: Optional[
        "CtDemonstrativoSolicitacao.DemonstrativoAnalise"
    ] = field(
        default=None,
        metadata={
            "name": "demonstrativoAnalise",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class DemonstrativoPagamento:
        dados_prestador: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "dadosPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        data_solicitacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataSolicitacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        tipo_demonstrativo: Optional[DmTipoDemonstrativoPagamento] = field(
            default=None,
            metadata={
                "name": "tipoDemonstrativo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        periodo: Optional[
            "CtDemonstrativoSolicitacao.DemonstrativoPagamento.Periodo"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class Periodo:
            data_pagamento: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "dataPagamento",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            competencia: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "pattern": r"[0-9]{4}[0-9]{2}",
                },
            )

    @dataclass
    class DemonstrativoAnalise:
        dados_prestador: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "dadosPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        data_solicitacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataSolicitacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        protocolos: Optional[
            "CtDemonstrativoSolicitacao.DemonstrativoAnalise.Protocolos"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class Protocolos:
            numero_protocolo: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "numeroProtocolo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_occurs": 1,
                    "max_occurs": 30,
                    "min_length": 1,
                    "max_length": 12,
                },
            )

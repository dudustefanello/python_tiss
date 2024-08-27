from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_conta_medica_resumo import CtContaMedicaResumo
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_demonstrativo_cabecalho import CtDemonstrativoCabecalho

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmDemonstrativoAnaliseConta:
    class Meta:
        name = "ctm_demonstrativoAnaliseConta"

    cabecalho_demonstrativo: Optional[CtDemonstrativoCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoDemonstrativo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_prestador: Optional[
        "CtmDemonstrativoAnaliseConta.DadosPrestador"
    ] = field(
        default=None,
        metadata={
            "name": "dadosPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_conta: Optional["CtmDemonstrativoAnaliseConta.DadosConta"] = field(
        default=None,
        metadata={
            "name": "dadosConta",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    valor_informado_geral: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorInformadoGeral",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_processado_geral: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorProcessadoGeral",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_liberado_geral: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorLiberadoGeral",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_glosa_geral: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorGlosaGeral",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )

    @dataclass
    class DadosPrestador:
        dados_contratado: Optional[CtContratadoDados] = field(
            default=None,
            metadata={
                "name": "dadosContratado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        cnes: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNES",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 7,
            },
        )

    @dataclass
    class DadosConta:
        dados_protocolo: List[CtContaMedicaResumo] = field(
            default_factory=list,
            metadata={
                "name": "dadosProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_opcao_fabricante import DmOpcaoFabricante

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoAutorizado:
    class Meta:
        name = "ct_procedimentoAutorizado"

    sequencial_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequencialItem",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 4,
        },
    )
    procedimento: Optional[CtProcedimentoDados] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    quantidade_solicitada: Optional[int] = field(
        default=None,
        metadata={
            "name": "quantidadeSolicitada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    quantidade_autorizada: Optional[int] = field(
        default=None,
        metadata={
            "name": "quantidadeAutorizada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    valor_solicitado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorSolicitado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    valor_autorizado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorAutorizado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    opcao_fabricante: Optional[DmOpcaoFabricante] = field(
        default=None,
        metadata={
            "name": "opcaoFabricante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    registro_anvisa: Optional[str] = field(
        default=None,
        metadata={
            "name": "registroANVISA",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 15,
        },
    )
    codigo_ref_fabricante: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoRefFabricante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 60,
        },
    )
    autorizacao_funcionamento: Optional[str] = field(
        default=None,
        metadata={
            "name": "autorizacaoFuncionamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 30,
        },
    )
    motivos_negativa: Optional["CtProcedimentoAutorizado.MotivosNegativa"] = (
        field(
            default=None,
            metadata={
                "name": "motivosNegativa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )

    @dataclass
    class MotivosNegativa:
        motivo_negativa: List[CtMotivoGlosa] = field(
            default_factory=list,
            metadata={
                "name": "motivoNegativa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

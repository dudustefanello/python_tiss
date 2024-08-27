from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_dente import DmDente
from tiss.dm_regiao import DmRegiao
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRespostaRecursoItemOdonto:
    class Meta:
        name = "ct_respostaRecursoItemOdonto"

    numero_guia_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    numero_guia_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )
    senha: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )
    recurso_procedimento: List[
        "CtRespostaRecursoItemOdonto.RecursoProcedimento"
    ] = field(
        default_factory=list,
        metadata={
            "name": "recursoProcedimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
        },
    )

    @dataclass
    class RecursoProcedimento:
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
        data_realizacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataRealizacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        dente_regiao: Optional[
            "CtRespostaRecursoItemOdonto.RecursoProcedimento.DenteRegiao"
        ] = field(
            default=None,
            metadata={
                "name": "denteRegiao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        dente_face: Optional[str] = field(
            default=None,
            metadata={
                "name": "denteFace",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "pattern": r"[OLMVDIP]{1,5}",
            },
        )
        quantidade: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 2,
            },
        )
        proc_recurso: Optional[CtProcedimentoDados] = field(
            default=None,
            metadata={
                "name": "procRecurso",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        cod_glosa_proc: Optional[DmTipoGlosa] = field(
            default=None,
            metadata={
                "name": "codGlosaProc",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        valor_recursado: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorRecursado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )
        justificativa_prestador: Optional[str] = field(
            default=None,
            metadata={
                "name": "justificativaPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 500,
            },
        )
        valor_acatado: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorAcatado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )
        justificativa_operadora: Optional[str] = field(
            default=None,
            metadata={
                "name": "justificativaOperadora",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 500,
            },
        )

        @dataclass
        class DenteRegiao:
            cod_dente: Optional[DmDente] = field(
                default=None,
                metadata={
                    "name": "codDente",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            cod_regiao: Optional[DmRegiao] = field(
                default=None,
                metadata={
                    "name": "codRegiao",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )

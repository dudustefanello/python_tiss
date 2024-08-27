from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRespostaGlosaItemMedico:
    class Meta:
        name = "ct_respostaGlosaItemMedico"

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
    data_realizacao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataRealizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_fim: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataFim",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
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
    proc_recurso: Optional[CtProcedimentoDados] = field(
        default=None,
        metadata={
            "name": "procRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    cod_glosa: Optional[DmTipoGlosa] = field(
        default=None,
        metadata={
            "name": "codGlosa",
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
    valor_acatadado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorAcatadado",
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

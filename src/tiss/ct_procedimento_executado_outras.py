from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlTime

from tiss.dm_tabela import DmTabela
from tiss.dm_unidade_medida import DmUnidadeMedida

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoExecutadoOutras:
    class Meta:
        name = "ct_procedimentoExecutadoOutras"

    data_execucao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataExecucao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    hora_inicial: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaInicial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    hora_final: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaFinal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    codigo_tabela: Optional[DmTabela] = field(
        default=None,
        metadata={
            "name": "codigoTabela",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    codigo_procedimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoProcedimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )
    quantidade_executada: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "quantidadeExecutada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 9,
            "fraction_digits": 4,
        },
    )
    unidade_medida: Optional[DmUnidadeMedida] = field(
        default=None,
        metadata={
            "name": "unidadeMedida",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    reducao_acrescimo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "reducaoAcrescimo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 2,
        },
    )
    valor_unitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorUnitario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    valor_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    descricao_procedimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "descricaoProcedimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 150,
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

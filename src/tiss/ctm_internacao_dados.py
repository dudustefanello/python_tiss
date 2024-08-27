from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlTime

from tiss.dm_carater_atendimento import DmCaraterAtendimento
from tiss.dm_regime_internacao import DmRegimeInternacao
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_faturamento import DmTipoFaturamento
from tiss.dm_tipo_internacao import DmTipoInternacao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmInternacaoDados:
    class Meta:
        name = "ctm_internacaoDados"

    carater_atendimento: Optional[DmCaraterAtendimento] = field(
        default=None,
        metadata={
            "name": "caraterAtendimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    tipo_faturamento: Optional[DmTipoFaturamento] = field(
        default=None,
        metadata={
            "name": "tipoFaturamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_inicio_faturamento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataInicioFaturamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    hora_inicio_faturamento: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaInicioFaturamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_final_faturamento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataFinalFaturamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    hora_final_faturamento: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaFinalFaturamento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    tipo_internacao: Optional[DmTipoInternacao] = field(
        default=None,
        metadata={
            "name": "tipoInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    regime_internacao: Optional[DmRegimeInternacao] = field(
        default=None,
        metadata={
            "name": "regimeInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    declaracoes: List["CtmInternacaoDados.Declaracoes"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "max_occurs": 8,
        },
    )

    @dataclass
    class Declaracoes:
        declaracao_nascido: Optional[str] = field(
            default=None,
            metadata={
                "name": "declaracaoNascido",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 11,
                "pattern": r"[a-zA-Z0-9]+",
            },
        )
        diagnostico_obito: Optional[str] = field(
            default=None,
            metadata={
                "name": "diagnosticoObito",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 4,
            },
        )
        declaracao_obito: Optional[str] = field(
            default=None,
            metadata={
                "name": "declaracaoObito",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 11,
                "pattern": r"[a-zA-Z0-9]+",
            },
        )
        indicador_dorn: Optional[DmSimNao] = field(
            default=None,
            metadata={
                "name": "indicadorDORN",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

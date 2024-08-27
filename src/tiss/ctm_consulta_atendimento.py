from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.dm_cob_esp import DmCobEsp
from tiss.dm_regime_atendimento import DmRegimeAtendimento
from tiss.dm_saude_ocupacional import DmSaudeOcupacional
from tiss.dm_tabela import DmTabela
from tiss.dm_tipo_consulta import DmTipoConsulta

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmConsultaAtendimento:
    class Meta:
        name = "ctm_consultaAtendimento"

    cobertura_especial: Optional[DmCobEsp] = field(
        default=None,
        metadata={
            "name": "coberturaEspecial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    regime_atendimento: Optional[DmRegimeAtendimento] = field(
        default=None,
        metadata={
            "name": "regimeAtendimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    saude_ocupacional: Optional[DmSaudeOcupacional] = field(
        default=None,
        metadata={
            "name": "saudeOcupacional",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    data_atendimento: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataAtendimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    tipo_consulta: Optional[DmTipoConsulta] = field(
        default=None,
        metadata={
            "name": "tipoConsulta",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    procedimento: Optional["CtmConsultaAtendimento.Procedimento"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class Procedimento:
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
        valor_procedimento: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorProcedimento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )

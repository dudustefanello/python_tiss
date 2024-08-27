from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_indicador_acidente import DmIndicadorAcidente
from tiss.dm_motivo_saida_obito import DmMotivoSaidaObito
from tiss.dm_regime_atendimento import DmRegimeAtendimento
from tiss.dm_saude_ocupacional import DmSaudeOcupacional
from tiss.dm_tipo_atendimento import DmTipoAtendimento
from tiss.dm_tipo_consulta import DmTipoConsulta

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmSpSadtAtendimento:
    class Meta:
        name = "ctm_sp-sadtAtendimento"

    tipo_atendimento: Optional[DmTipoAtendimento] = field(
        default=None,
        metadata={
            "name": "tipoAtendimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    indicacao_acidente: Optional[DmIndicadorAcidente] = field(
        default=None,
        metadata={
            "name": "indicacaoAcidente",
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
        },
    )
    motivo_encerramento: Optional[DmMotivoSaidaObito] = field(
        default=None,
        metadata={
            "name": "motivoEncerramento",
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

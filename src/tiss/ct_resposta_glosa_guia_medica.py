from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRespostaGlosaGuiaMedica:
    class Meta:
        name = "ct_respostaGlosaGuiaMedica"

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
    cod_glosa: Optional[DmTipoGlosa] = field(
        default=None,
        metadata={
            "name": "codGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    recurso_guia_acatado: Optional[DmSimNao] = field(
        default=None,
        metadata={
            "name": "recursoGuiaAcatado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    justificativa_opsnao_acatado_guia: Optional[str] = field(
        default=None,
        metadata={
            "name": "justificativaOPSnaoAcatadoGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 500,
        },
    )

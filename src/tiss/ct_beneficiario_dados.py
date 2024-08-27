from dataclasses import dataclass, field
from typing import Optional

from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_ident import DmTipoIdent

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtBeneficiarioDados:
    class Meta:
        name = "ct_beneficiarioDados"

    numero_carteira: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroCarteira",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    atendimento_rn: Optional[DmSimNao] = field(
        default=None,
        metadata={
            "name": "atendimentoRN",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    tipo_ident: Optional[DmTipoIdent] = field(
        default=None,
        metadata={
            "name": "tipoIdent",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    identificador_beneficiario: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "identificadorBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "format": "base64",
        },
    )

from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_ident import DmTipoIdent

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtElegibilidadeRecibo:
    class Meta:
        name = "ct_elegibilidadeRecibo"

    registro_ans: Optional[str] = field(
        default=None,
        metadata={
            "name": "registroANS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "max_length": 6,
            "pattern": r"[0-9]{6}",
        },
    )
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
    ausencia_cod_validacao: Optional[DmAusenciaCodValidacao] = field(
        default=None,
        metadata={
            "name": "ausenciaCodValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    cod_validacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "codValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 10,
        },
    )
    validade_carteira: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "validadeCarteira",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    nome_beneficiario: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    nome_social_beneficiario: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeSocialBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 70,
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
    resposta_solicitacao: Optional[DmSimNao] = field(
        default=None,
        metadata={
            "name": "respostaSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    motivos_negativa: Optional["CtElegibilidadeRecibo.MotivosNegativa"] = (
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

from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_situacao_clinica import CtSituacaoClinica

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtoAnexoSituacaoInicialnaGto:
    class Meta:
        name = "cto_anexoSituacaoInicialnaGTO"

    numero_guia_anexo: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaAnexo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    numero_guia_referenciada: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaReferenciada",
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
    ct_situacao_inicial: Optional[
        "CtoAnexoSituacaoInicialnaGto.CtSituacaoInicial"
    ] = field(
        default=None,
        metadata={
            "name": "ct_situacaoInicial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class CtSituacaoInicial:
        situacao_clinica: Optional[CtSituacaoClinica] = field(
            default=None,
            metadata={
                "name": "situacaoClinica",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        doenca_periodontal: Optional[bool] = field(
            default=None,
            metadata={
                "name": "doencaPeriodontal",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        alteracao_tecido_mole: Optional[bool] = field(
            default=None,
            metadata={
                "name": "alteracaoTecidoMole",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        observacao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 500,
            },
        )

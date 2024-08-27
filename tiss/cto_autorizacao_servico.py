from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_autorizacao_dados import CtAutorizacaoDados
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_dente import DmDente
from tiss.dm_regiao import DmRegiao
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_status_solicitacao import DmStatusSolicitacao
from tiss.dm_tipo_glosa import DmTipoGlosa
from tiss.dm_tipo_ident import DmTipoIdent

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtoAutorizacaoServico:
    class Meta:
        name = "cto_autorizacaoServico"

    dados_autorizacao: Optional[CtAutorizacaoDados] = field(
        default=None,
        metadata={
            "name": "dadosAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    status_solicitacao: Optional[DmStatusSolicitacao] = field(
        default=None,
        metadata={
            "name": "statusSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    prestador_autorizado: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "prestadorAutorizado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    procedimentos_autorizados: List[
        "CtoAutorizacaoServico.ProcedimentosAutorizados"
    ] = field(
        default_factory=list,
        metadata={
            "name": "procedimentosAutorizados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    motivos_negativa: Optional["CtoAutorizacaoServico.MotivosNegativa"] = (
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
    class ProcedimentosAutorizados:
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
        proc_solic: Optional[CtProcedimentoDados] = field(
            default=None,
            metadata={
                "name": "procSolic",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        dente_regiao: Optional[
            "CtoAutorizacaoServico.ProcedimentosAutorizados.DenteRegiao"
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
                "min_length": 1,
                "max_length": 5,
            },
        )
        qtd_proc: Optional[int] = field(
            default=None,
            metadata={
                "name": "qtdProc",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 2,
            },
        )
        qtd_us: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "qtdUS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )
        valor_proc: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorProc",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )
        valor_franquia: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorFranquia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )
        aut: Optional[DmSimNao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        motivos_negativa: Optional[
            "CtoAutorizacaoServico.ProcedimentosAutorizados.MotivosNegativa"
        ] = field(
            default=None,
            metadata={
                "name": "motivosNegativa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
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

        @dataclass
        class MotivosNegativa:
            codigo_glosa: List[DmTipoGlosa] = field(
                default_factory=list,
                metadata={
                    "name": "codigoGlosa",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_occurs": 1,
                },
            )

    @dataclass
    class MotivosNegativa:
        codigo_glosa: List[DmTipoGlosa] = field(
            default_factory=list,
            metadata={
                "name": "codigoGlosa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

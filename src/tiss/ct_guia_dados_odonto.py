from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_procedimento_executado_odonto import CtProcedimentoExecutadoOdonto
from tiss.ct_valor_total import CtValorTotal
from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_ident import DmTipoIdent

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGuiaDadosOdonto:
    class Meta:
        name = "ct_guiaDadosOdonto"

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
    vl_informado_guia: Optional[CtValorTotal] = field(
        default=None,
        metadata={
            "name": "vlInformadoGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    glosa_guia: Optional["CtGuiaDadosOdonto.GlosaGuia"] = field(
        default=None,
        metadata={
            "name": "glosaGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    procedimentos_realizados: Optional[
        "CtGuiaDadosOdonto.ProcedimentosRealizados"
    ] = field(
        default=None,
        metadata={
            "name": "procedimentosRealizados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class GlosaGuia:
        motivo_glosa: List[CtMotivoGlosa] = field(
            default_factory=list,
            metadata={
                "name": "motivoGlosa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

    @dataclass
    class ProcedimentosRealizados:
        procedimento_realizado: List[
            "CtGuiaDadosOdonto.ProcedimentosRealizados.ProcedimentoRealizado"
        ] = field(
            default_factory=list,
            metadata={
                "name": "procedimentoRealizado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

        @dataclass
        class ProcedimentoRealizado(CtProcedimentoExecutadoOdonto):
            glosas_procedimento: Optional[
                "CtGuiaDadosOdonto.ProcedimentosRealizados.ProcedimentoRealizado.GlosasProcedimento"
            ] = field(
                default=None,
                metadata={
                    "name": "glosasProcedimento",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )

            @dataclass
            class GlosasProcedimento:
                motivo_glosa: List[CtMotivoGlosa] = field(
                    default_factory=list,
                    metadata={
                        "name": "motivoGlosa",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "min_occurs": 1,
                    },
                )
                valor_glosa_procedimento: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "valorGlosaProcedimento",
                        "type": "Element",
                        "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                        "required": True,
                        "total_digits": 10,
                        "fraction_digits": 2,
                    },
                )

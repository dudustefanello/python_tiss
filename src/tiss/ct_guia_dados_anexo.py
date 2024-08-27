from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.ct_valor_total import CtValorTotal
from tiss.dm_opcao_fabricante import DmOpcaoFabricante

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGuiaDadosAnexo:
    class Meta:
        name = "ct_guiaDadosAnexo"

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
    dados_beneficiario: Optional[CtBeneficiarioDados] = field(
        default=None,
        metadata={
            "name": "dadosBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_emissao_solicitacao_anexo: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEmissao_SolicitacaoAnexo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    vl_informado_guia: Optional[CtValorTotal] = field(
        default=None,
        metadata={
            "name": "vlInformadoGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    glosa_anexo: Optional["CtGuiaDadosAnexo.GlosaAnexo"] = field(
        default=None,
        metadata={
            "name": "glosaAnexo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    procedimentos_solicitados: Optional[
        "CtGuiaDadosAnexo.ProcedimentosSolicitados"
    ] = field(
        default=None,
        metadata={
            "name": "procedimentosSolicitados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class GlosaAnexo:
        motivo_glosa: List[CtMotivoGlosa] = field(
            default_factory=list,
            metadata={
                "name": "motivoGlosa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )
        vl_glosa_anexo: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "vlGlosaAnexo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 10,
                "fraction_digits": 2,
            },
        )

    @dataclass
    class ProcedimentosSolicitados:
        procedimento_solicitado: List[
            "CtGuiaDadosAnexo.ProcedimentosSolicitados.ProcedimentoSolicitado"
        ] = field(
            default_factory=list,
            metadata={
                "name": "procedimentoSolicitado",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

        @dataclass
        class ProcedimentoSolicitado:
            procedimento: Optional[CtProcedimentoDados] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            opcao_fabricante: Optional[DmOpcaoFabricante] = field(
                default=None,
                metadata={
                    "name": "opcaoFabricante",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            qtd_solicitada: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "qtdSolicitada",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 5,
                    "fraction_digits": 2,
                },
            )
            valor_solicitado: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorSolicitado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "total_digits": 8,
                    "fraction_digits": 2,
                },
            )
            qtd_autorizada: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "qtdAutorizada",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 5,
                    "fraction_digits": 2,
                },
            )
            valor_autorizado: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "valorAutorizado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 8,
                    "fraction_digits": 2,
                },
            )
            glosas_procedimento: Optional[
                "CtGuiaDadosAnexo.ProcedimentosSolicitados.ProcedimentoSolicitado.GlosasProcedimento"
            ] = field(
                default=None,
                metadata={
                    "name": "glosasProcedimento",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
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

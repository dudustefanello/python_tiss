from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from tiss.ct_anexo_cabecalho import CtAnexoCabecalho
from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.ctm_anexo_solicitante import CtmAnexoSolicitante
from tiss.dm_opcao_fabricante import DmOpcaoFabricante

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmAnexoSolicitacaoOpme:
    class Meta:
        name = "ctm_anexoSolicitacaoOPME"

    cabecalho_anexo: Optional[CtAnexoCabecalho] = field(
        default=None,
        metadata={
            "name": "cabecalhoAnexo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    profissional_solicitante: Optional[CtmAnexoSolicitante] = field(
        default=None,
        metadata={
            "name": "profissionalSolicitante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    justificativa_tecnica: Optional[str] = field(
        default=None,
        metadata={
            "name": "justificativaTecnica",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 1000,
        },
    )
    especificacao_material: Optional[str] = field(
        default=None,
        metadata={
            "name": "especificacaoMaterial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 500,
        },
    )
    opme_solicitadas: Optional["CtmAnexoSolicitacaoOpme.OpmeSolicitadas"] = (
        field(
            default=None,
            metadata={
                "name": "opmeSolicitadas",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    observacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "Observacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 500,
        },
    )

    @dataclass
    class OpmeSolicitadas:
        opme_solicitada: List[
            "CtmAnexoSolicitacaoOpme.OpmeSolicitadas.OpmeSolicitada"
        ] = field(
            default_factory=list,
            metadata={
                "name": "opmeSolicitada",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )

        @dataclass
        class OpmeSolicitada:
            identificacao_opme: Optional[CtProcedimentoDados] = field(
                default=None,
                metadata={
                    "name": "identificacaoOPME",
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
                    "required": True,
                },
            )
            quantidade_solicitada: Optional[int] = field(
                default=None,
                metadata={
                    "name": "quantidadeSolicitada",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "total_digits": 3,
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
            registro_anvisa: Optional[str] = field(
                default=None,
                metadata={
                    "name": "registroANVISA",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 15,
                },
            )
            codigo_ref_fabricante: Optional[str] = field(
                default=None,
                metadata={
                    "name": "codigoRefFabricante",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 60,
                },
            )
            autorizacao_funcionamento: Optional[str] = field(
                default=None,
                metadata={
                    "name": "autorizacaoFuncionamento",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 30,
                },
            )

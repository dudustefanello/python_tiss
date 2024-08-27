from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_contratado_profissional_dados import CtContratadoProfissionalDados
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.ctm_anexo_solicitacao_opme import CtmAnexoSolicitacaoOpme
from tiss.ctm_anexo_solicitacao_quimio import CtmAnexoSolicitacaoQuimio
from tiss.ctm_anexo_solicitacao_radio import CtmAnexoSolicitacaoRadio
from tiss.dm_tipo_acomodacao import DmTipoAcomodacao
from tiss.dm_tipo_ident import DmTipoIdent

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmProrrogacaoSolicitacaoGuia:
    class Meta:
        name = "ctm_prorrogacaoSolicitacaoGuia"

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
    nr_guia_referenciada: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrGuiaReferenciada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    dados_beneficiario: Optional[
        "CtmProrrogacaoSolicitacaoGuia.DadosBeneficiario"
    ] = field(
        default=None,
        metadata={
            "name": "dadosBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    dados_contratado_solicitante: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosContratadoSolicitante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    nome_contratado_solicitante: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeContratadoSolicitante",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    dados_profissional_solicitante: Optional[CtContratadoProfissionalDados] = (
        field(
            default=None,
            metadata={
                "name": "dadosProfissionalSolicitante",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
    )
    dados_internacao: Optional[
        "CtmProrrogacaoSolicitacaoGuia.DadosInternacao"
    ] = field(
        default=None,
        metadata={
            "name": "dadosInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    procedimentos_adicionais: List[
        "CtmProrrogacaoSolicitacaoGuia.ProcedimentosAdicionais"
    ] = field(
        default_factory=list,
        metadata={
            "name": "procedimentosAdicionais",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    anexo_clinico_prorrogacao: Optional[
        "CtmProrrogacaoSolicitacaoGuia.AnexoClinicoProrrogacao"
    ] = field(
        default=None,
        metadata={
            "name": "anexoClinicoProrrogacao",
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
    data_solicitacao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataSolicitacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class DadosBeneficiario:
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

    @dataclass
    class DadosInternacao:
        qt_diarias_adicionais: Optional[int] = field(
            default=None,
            metadata={
                "name": "qtDiariasAdicionais",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "total_digits": 3,
            },
        )
        tipo_acomodacao_solicitada: Optional[DmTipoAcomodacao] = field(
            default=None,
            metadata={
                "name": "tipoAcomodacaoSolicitada",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        indicacao_clinica: Optional[str] = field(
            default=None,
            metadata={
                "name": "indicacaoClinica",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 500,
            },
        )

    @dataclass
    class ProcedimentosAdicionais:
        procedimento: Optional[CtProcedimentoDados] = field(
            default=None,
            metadata={
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

    @dataclass
    class AnexoClinicoProrrogacao:
        solicitacao_quimioterapia: Optional[CtmAnexoSolicitacaoQuimio] = field(
            default=None,
            metadata={
                "name": "solicitacaoQuimioterapia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        solicitacao_radioterapia: Optional[CtmAnexoSolicitacaoRadio] = field(
            default=None,
            metadata={
                "name": "solicitacaoRadioterapia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        solicitacao_opme: Optional[CtmAnexoSolicitacaoOpme] = field(
            default=None,
            metadata={
                "name": "solicitacaoOPME",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ctm_autorizacao_opme import CtmAutorizacaoOpme
from tiss.ctm_autorizacao_quimio import CtmAutorizacaoQuimio
from tiss.ctm_autorizacao_radio import CtmAutorizacaoRadio
from tiss.cto_anexo_situacao_inicial import CtoAnexoSituacaoInicial

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtAnexoRecebimento:
    """
    Estrutura de recibo do recebimento de um lote de anexos dos prestadores.
    """

    class Meta:
        name = "ct_anexoRecebimento"

    nr_protocolo_recebimento: Optional[str] = field(
        default=None,
        metadata={
            "name": "nrProtocoloRecebimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
    data_envio_anexo: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataEnvioAnexo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    numero_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 12,
        },
    )
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
    dados_prestador: Optional[CtContratadoDados] = field(
        default=None,
        metadata={
            "name": "dadosPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    qt_anexos_clinicos: Optional[int] = field(
        default=None,
        metadata={
            "name": "qtAnexosClinicos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    anexos_clinicos: Optional["CtAnexoRecebimento.AnexosClinicos"] = field(
        default=None,
        metadata={
            "name": "anexosClinicos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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

    @dataclass
    class AnexosClinicos:
        anexo_opme: Optional[CtmAutorizacaoOpme] = field(
            default=None,
            metadata={
                "name": "anexoOPME",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        anexo_quimio: Optional[CtmAutorizacaoQuimio] = field(
            default=None,
            metadata={
                "name": "anexoQuimio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        anexo_radio: Optional[CtmAutorizacaoRadio] = field(
            default=None,
            metadata={
                "name": "anexoRadio",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        anexo_situacao_inicial: List[
            "CtAnexoRecebimento.AnexosClinicos.AnexoSituacaoInicial"
        ] = field(
            default_factory=list,
            metadata={
                "name": "anexoSituacaoInicial",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
            },
        )

        @dataclass
        class AnexoSituacaoInicial(CtoAnexoSituacaoInicial):
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

from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_resposta_recurso_guia_odonto import CtRespostaRecursoGuiaOdonto
from tiss.ct_resposta_recurso_item_odonto import CtRespostaRecursoItemOdonto
from tiss.dm_objeto_recurso import DmObjetoRecurso
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_glosa import DmTipoGlosa

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtGlosaReciboOdonto:
    """
    Retorno do recurso de glosa de odonto.
    """

    class Meta:
        name = "ct_glosaReciboOdonto"

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
    numero_guia_rec_glosa_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaRecGlosaPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    nome_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    numero_guia_rec_glosa_operadora: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaRecGlosaOperadora",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )
    objeto_recurso: Optional[DmObjetoRecurso] = field(
        default=None,
        metadata={
            "name": "objetoRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    codigo_prestador: Optional[str] = field(
        default=None,
        metadata={
            "name": "codigoPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 14,
        },
    )
    numero_lote: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 12,
        },
    )
    numero_protocolo: Optional[int] = field(
        default=None,
        metadata={
            "name": "numeroProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 12,
        },
    )
    opcao_recurso: Optional["CtGlosaReciboOdonto.OpcaoRecurso"] = field(
        default=None,
        metadata={
            "name": "opcaoRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    data_recurso: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataRecurso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    valor_total_recursado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalRecursado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )
    valor_total_acatado: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalAcatado",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 10,
            "fraction_digits": 2,
        },
    )

    @dataclass
    class OpcaoRecurso:
        recurso_protocolo: Optional[
            "CtGlosaReciboOdonto.OpcaoRecurso.RecursoProtocolo"
        ] = field(
            default=None,
            metadata={
                "name": "recursoProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        recurso_guia: List["CtGlosaReciboOdonto.OpcaoRecurso.RecursoGuia"] = (
            field(
                default_factory=list,
                metadata={
                    "name": "recursoGuia",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
        )

        @dataclass
        class RecursoProtocolo:
            codigo_glosa_protocolo: Optional[DmTipoGlosa] = field(
                default=None,
                metadata={
                    "name": "codigoGlosaProtocolo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )
            justificativa_protocolo: Optional[str] = field(
                default=None,
                metadata={
                    "name": "justificativaProtocolo",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                    "min_length": 1,
                    "max_length": 500,
                },
            )
            recurso_acatado: Optional[DmSimNao] = field(
                default=None,
                metadata={
                    "name": "recursoAcatado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "required": True,
                },
            )

        @dataclass
        class RecursoGuia:
            resposta_recurso_guia_odonto: Optional[
                CtRespostaRecursoGuiaOdonto
            ] = field(
                default=None,
                metadata={
                    "name": "respostaRecursoGuiaOdonto",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            resposta_recurso_item_odonto: Optional[
                CtRespostaRecursoItemOdonto
            ] = field(
                default=None,
                metadata={
                    "name": "respostaRecursoItemOdonto",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )

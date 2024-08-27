from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_glosa_recibo import CtGlosaRecibo
from tiss.ct_glosa_recibo_odonto import CtGlosaReciboOdonto
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.dm_status_protocolo import DmStatusProtocolo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtRespostaGlosa:
    class Meta:
        name = "ct_respostaGlosa"

    recibo_glosa: Optional[CtGlosaRecibo] = field(
        default=None,
        metadata={
            "name": "reciboGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recibo_glosa_odonto: Optional[CtGlosaReciboOdonto] = field(
        default=None,
        metadata={
            "name": "reciboGlosaOdonto",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recibo_glosa_status: Optional["CtRespostaGlosa.ReciboGlosaStatus"] = field(
        default=None,
        metadata={
            "name": "reciboGlosaStatus",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    mensagem_erro: Optional[CtMotivoGlosa] = field(
        default=None,
        metadata={
            "name": "mensagemErro",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class ReciboGlosaStatus:
        nr_protocolo_recurso_glosa: Optional[str] = field(
            default=None,
            metadata={
                "name": "nrProtocoloRecursoGlosa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 12,
            },
        )
        data_envio_recurso: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataEnvioRecurso",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        data_recebimento_recurso: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataRecebimentoRecurso",
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
        nr_protocolo_situacao_recurso_glosa: Optional[str] = field(
            default=None,
            metadata={
                "name": "nrProtocoloSituacaoRecursoGlosa",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 12,
            },
        )
        data_situacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataSituacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        situacao_protocolo: Optional[DmStatusProtocolo] = field(
            default=None,
            metadata={
                "name": "situacaoProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

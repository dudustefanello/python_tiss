from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_anexo_recebimento import CtAnexoRecebimento
from tiss.ct_demonstrativo_retorno import CtDemonstrativoRetorno
from tiss.ct_elegibilidade_recibo import CtElegibilidadeRecibo
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_recebimento_lote import CtRecebimentoLote
from tiss.ct_recebimento_recurso import CtRecebimentoRecurso
from tiss.ct_recibo_cancela_guia import CtReciboCancelaGuia
from tiss.ct_recibo_comunicacao import CtReciboComunicacao
from tiss.ct_recibo_documentos import CtReciboDocumentos
from tiss.ct_resposta_glosa import CtRespostaGlosa
from tiss.ct_situacao_autorizacao import CtSituacaoAutorizacao
from tiss.ct_situacao_protocolo import CtSituacaoProtocolo

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class OperadoraPrestador:
    class Meta:
        name = "operadoraPrestador"

    recebimento_lote: Optional[CtRecebimentoLote] = field(
        default=None,
        metadata={
            "name": "recebimentoLote",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recebimento_anexo: Optional["OperadoraPrestador.RecebimentoAnexo"] = field(
        default=None,
        metadata={
            "name": "recebimentoAnexo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recebimento_recurso_glosa: Optional[CtRecebimentoRecurso] = field(
        default=None,
        metadata={
            "name": "recebimentoRecursoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    demonstrativos_retorno: Optional[CtDemonstrativoRetorno] = field(
        default=None,
        metadata={
            "name": "demonstrativosRetorno",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    situacao_protocolo: Optional[CtSituacaoProtocolo] = field(
        default=None,
        metadata={
            "name": "situacaoProtocolo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    autorizacao_servicos: Optional[CtSituacaoAutorizacao] = field(
        default=None,
        metadata={
            "name": "autorizacaoServicos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    situacao_autorizacao: Optional[CtSituacaoAutorizacao] = field(
        default=None,
        metadata={
            "name": "situacaoAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    resposta_elegibilidade: Optional[
        "OperadoraPrestador.RespostaElegibilidade"
    ] = field(
        default=None,
        metadata={
            "name": "respostaElegibilidade",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recibo_cancela_guia: Optional[CtReciboCancelaGuia] = field(
        default=None,
        metadata={
            "name": "reciboCancelaGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recibo_comunicacao: Optional[CtReciboComunicacao] = field(
        default=None,
        metadata={
            "name": "reciboComunicacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    resposta_recurso_glosa: Optional[CtRespostaGlosa] = field(
        default=None,
        metadata={
            "name": "respostaRecursoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recebimento_documentos: Optional[
        "OperadoraPrestador.RecebimentoDocumentos"
    ] = field(
        default=None,
        metadata={
            "name": "recebimentoDocumentos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class RecebimentoAnexo:
        mensagem_erro: Optional[CtMotivoGlosa] = field(
            default=None,
            metadata={
                "name": "mensagemErro",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        protocolo_recebimento_anexo: Optional[CtAnexoRecebimento] = field(
            default=None,
            metadata={
                "name": "protocoloRecebimentoAnexo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

    @dataclass
    class RespostaElegibilidade:
        mensagem_erro: Optional[CtMotivoGlosa] = field(
            default=None,
            metadata={
                "name": "mensagemErro",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        recibo_elegibilidade: Optional[CtElegibilidadeRecibo] = field(
            default=None,
            metadata={
                "name": "reciboElegibilidade",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

    @dataclass
    class RecebimentoDocumentos:
        mensagem_erro: Optional[CtMotivoGlosa] = field(
            default=None,
            metadata={
                "name": "mensagemErro",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        recibo_documento: Optional[CtReciboDocumentos] = field(
            default=None,
            metadata={
                "name": "reciboDocumento",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

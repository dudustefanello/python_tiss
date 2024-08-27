from dataclasses import dataclass, field
from typing import Optional

from tiss.ct_anexo_lote import CtAnexoLote
from tiss.ct_autorizacao_solicita_status import CtAutorizacaoSolicitaStatus
from tiss.ct_demonstrativo_solicitacao import CtDemonstrativoSolicitacao
from tiss.ct_elegibilidade_verifica import CtElegibilidadeVerifica
from tiss.ct_envio_documentos import CtEnvioDocumentos
from tiss.ct_guia_cancelamento import CtGuiaCancelamento
from tiss.ct_guia_recurso_lote import CtGuiaRecursoLote
from tiss.ct_protocolo_solicitacao_status import CtProtocoloSolicitacaoStatus
from tiss.ct_solicitacao_procedimento import CtSolicitacaoProcedimento
from tiss.ctm_beneficiario_comunicacao import CtmBeneficiarioComunicacao
from tiss.ctm_guia_lote import CtmGuiaLote

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class PrestadorOperadora:
    class Meta:
        name = "prestadorOperadora"

    lote_guias: Optional[CtmGuiaLote] = field(
        default=None,
        metadata={
            "name": "loteGuias",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    lote_anexos: Optional[CtAnexoLote] = field(
        default=None,
        metadata={
            "name": "loteAnexos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    solicitacao_demonstrativo_retorno: Optional[CtDemonstrativoSolicitacao] = (
        field(
            default=None,
            metadata={
                "name": "solicitacaoDemonstrativoRetorno",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )
    solicitacao_status_protocolo: Optional[CtProtocoloSolicitacaoStatus] = (
        field(
            default=None,
            metadata={
                "name": "solicitacaoStatusProtocolo",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
    )
    solicitacao_procedimento: Optional[CtSolicitacaoProcedimento] = field(
        default=None,
        metadata={
            "name": "solicitacaoProcedimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    solicita_status_autorizacao: Optional[CtAutorizacaoSolicitaStatus] = field(
        default=None,
        metadata={
            "name": "solicitaStatusAutorizacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    verifica_elegibilidade: Optional[CtElegibilidadeVerifica] = field(
        default=None,
        metadata={
            "name": "verificaElegibilidade",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    cancela_guia: Optional[CtGuiaCancelamento] = field(
        default=None,
        metadata={
            "name": "cancelaGuia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    comunicacao_internacao: Optional[CtmBeneficiarioComunicacao] = field(
        default=None,
        metadata={
            "name": "comunicacaoInternacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    recurso_glosa: Optional[CtGuiaRecursoLote] = field(
        default=None,
        metadata={
            "name": "recursoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    solicitacao_status_recurso_glosa: Optional[
        CtProtocoloSolicitacaoStatus
    ] = field(
        default=None,
        metadata={
            "name": "solicitacaoStatusRecursoGlosa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    envio_documentos: Optional[CtEnvioDocumentos] = field(
        default=None,
        metadata={
            "name": "envioDocumentos",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

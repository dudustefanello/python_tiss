from tiss.autorizacao_procedimento_ws import AutorizacaoProcedimentoWs
from tiss.cabecalho_transacao import CabecalhoTransacao
from tiss.cancela_guia_ws import CancelaGuiaWs
from tiss.canonicalization_method import CanonicalizationMethod
from tiss.canonicalization_method_type import CanonicalizationMethodType
from tiss.comunicacao_beneficiario_ws import ComunicacaoBeneficiarioWs
from tiss.ct_anexo_cabecalho import CtAnexoCabecalho
from tiss.ct_anexo_lote import CtAnexoLote
from tiss.ct_anexo_recebimento import CtAnexoRecebimento
from tiss.ct_autorizacao_dados import CtAutorizacaoDados
from tiss.ct_autorizacao_internacao import CtAutorizacaoInternacao
from tiss.ct_autorizacao_sadt import CtAutorizacaoSadt
from tiss.ct_autorizacao_solicita_status import CtAutorizacaoSolicitaStatus
from tiss.ct_beneficiario_dados import CtBeneficiarioDados
from tiss.ct_conta_medica_resumo import CtContaMedicaResumo
from tiss.ct_contratado_dados import CtContratadoDados
from tiss.ct_contratado_dados_nome import CtContratadoDadosNome
from tiss.ct_contratado_profissional_dados import CtContratadoProfissionalDados
from tiss.ct_credito_odonto import CtCreditoOdonto
from tiss.ct_dados_complementares_beneficiario import (
    CtDadosComplementaresBeneficiario,
)
from tiss.ct_dados_complementares_beneficiario_radio import (
    CtDadosComplementaresBeneficiarioRadio,
)
from tiss.ct_dados_resumo_demonstrativo import CtDadosResumoDemonstrativo
from tiss.ct_demonstrativo_cabecalho import CtDemonstrativoCabecalho
from tiss.ct_demonstrativo_retorno import CtDemonstrativoRetorno
from tiss.ct_demonstrativo_solicitacao import CtDemonstrativoSolicitacao
from tiss.ct_descontos import CtDescontos
from tiss.ct_diagnostico import CtDiagnostico
from tiss.ct_diagnostico_oncologico import CtDiagnosticoOncologico
from tiss.ct_drogas_solicitadas import CtDrogasSolicitadas
from tiss.ct_elegibilidade_recibo import CtElegibilidadeRecibo
from tiss.ct_elegibilidade_verifica import CtElegibilidadeVerifica
from tiss.ct_envio_documentos import CtEnvioDocumentos
from tiss.ct_fonte_pagadora import CtFontePagadora
from tiss.ct_glosa_recibo import CtGlosaRecibo
from tiss.ct_glosa_recibo_odonto import CtGlosaReciboOdonto
from tiss.ct_guia_cabecalho import CtGuiaCabecalho
from tiss.ct_guia_cancelamento import CtGuiaCancelamento
from tiss.ct_guia_cancelamento_recibo import CtGuiaCancelamentoRecibo
from tiss.ct_guia_dados import CtGuiaDados
from tiss.ct_guia_dados_anexo import CtGuiaDadosAnexo
from tiss.ct_guia_dados_odonto import CtGuiaDadosOdonto
from tiss.ct_guia_recurso import CtGuiaRecurso
from tiss.ct_guia_recurso_lote import CtGuiaRecursoLote
from tiss.ct_guia_valor_total import CtGuiaValorTotal
from tiss.ct_guia_valor_total_sadt import CtGuiaValorTotalSadt
from tiss.ct_hipotese_diagnostica import CtHipoteseDiagnostica
from tiss.ct_ident_equipe import CtIdentEquipe
from tiss.ct_ident_equipe_sadt import CtIdentEquipeSadt
from tiss.ct_intervalo_ciclos import CtIntervaloCiclos
from tiss.ct_login_senha import CtLoginSenha
from tiss.ct_lote_anexo_status import CtLoteAnexoStatus
from tiss.ct_lote_status import CtLoteStatus
from tiss.ct_motivo_glosa import CtMotivoGlosa
from tiss.ct_opm_utilizada import CtOpmUtilizada
from tiss.ct_opme_dados import CtOpmeDados
from tiss.ct_outras_despesas import CtOutrasDespesas
from tiss.ct_pagamento_dados import CtPagamentoDados
from tiss.ct_pagamento_resumo import CtPagamentoResumo
from tiss.ct_prestador_identificacao import CtPrestadorIdentificacao
from tiss.ct_procedimento_autorizado import CtProcedimentoAutorizado
from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.ct_procedimento_executado import CtProcedimentoExecutado
from tiss.ct_procedimento_executado_honor_indiv import (
    CtProcedimentoExecutadoHonorIndiv,
)
from tiss.ct_procedimento_executado_int import CtProcedimentoExecutadoInt
from tiss.ct_procedimento_executado_odonto import CtProcedimentoExecutadoOdonto
from tiss.ct_procedimento_executado_outras import CtProcedimentoExecutadoOutras
from tiss.ct_procedimento_executado_sadt import CtProcedimentoExecutadoSadt
from tiss.ct_procedimento_solicitado import CtProcedimentoSolicitado
from tiss.ct_procedimentos_complementares import CtProcedimentosComplementares
from tiss.ct_protocolo_anexo_status import CtProtocoloAnexoStatus
from tiss.ct_protocolo_detalhe import CtProtocoloDetalhe
from tiss.ct_protocolo_detalhe_anexo import CtProtocoloDetalheAnexo
from tiss.ct_protocolo_recebimento import CtProtocoloRecebimento
from tiss.ct_protocolo_recebimento_anexo import CtProtocoloRecebimentoAnexo
from tiss.ct_protocolo_recebimento_recurso import CtProtocoloRecebimentoRecurso
from tiss.ct_protocolo_recurso import CtProtocoloRecurso
from tiss.ct_protocolo_solicitacao_status import CtProtocoloSolicitacaoStatus
from tiss.ct_protocolo_status import CtProtocoloStatus
from tiss.ct_recebimento_lote import CtRecebimentoLote
from tiss.ct_recebimento_recurso import CtRecebimentoRecurso
from tiss.ct_recibo_cancela_guia import CtReciboCancelaGuia
from tiss.ct_recibo_comunicacao import CtReciboComunicacao
from tiss.ct_recibo_documentos import CtReciboDocumentos
from tiss.ct_recurso_glosa_recebimento import CtRecursoGlosaRecebimento
from tiss.ct_resposta_elegibilidade import CtRespostaElegibilidade
from tiss.ct_resposta_glosa import CtRespostaGlosa
from tiss.ct_resposta_glosa_guia_medica import CtRespostaGlosaGuiaMedica
from tiss.ct_resposta_glosa_item_medico import CtRespostaGlosaItemMedico
from tiss.ct_resposta_recurso_guia_odonto import CtRespostaRecursoGuiaOdonto
from tiss.ct_resposta_recurso_item_odonto import CtRespostaRecursoItemOdonto
from tiss.ct_situacao_autorizacao import CtSituacaoAutorizacao
from tiss.ct_situacao_clinica import CtSituacaoClinica
from tiss.ct_situacao_protocolo import CtSituacaoProtocolo
from tiss.ct_solicitacao_procedimento import CtSolicitacaoProcedimento
from tiss.ct_valor_credito_desconto import CtValorCreditoDesconto
from tiss.ct_valor_total import CtValorTotal
from tiss.ctm_anexo_solicitacao_opme import CtmAnexoSolicitacaoOpme
from tiss.ctm_anexo_solicitacao_quimio import CtmAnexoSolicitacaoQuimio
from tiss.ctm_anexo_solicitacao_radio import CtmAnexoSolicitacaoRadio
from tiss.ctm_anexo_solicitante import CtmAnexoSolicitante
from tiss.ctm_autorizacao_internacao import CtmAutorizacaoInternacao
from tiss.ctm_autorizacao_opme import CtmAutorizacaoOpme
from tiss.ctm_autorizacao_prorrogacao import CtmAutorizacaoProrrogacao
from tiss.ctm_autorizacao_quimio import CtmAutorizacaoQuimio
from tiss.ctm_autorizacao_radio import CtmAutorizacaoRadio
from tiss.ctm_autorizacao_servico import CtmAutorizacaoServico
from tiss.ctm_beneficiario_comunicacao import CtmBeneficiarioComunicacao
from tiss.ctm_beneficiario_comunicacao_recibo import (
    CtmBeneficiarioComunicacaoRecibo,
)
from tiss.ctm_beneficiario_comunicacao_ret import CtmBeneficiarioComunicacaoRet
from tiss.ctm_consulta_atendimento import CtmConsultaAtendimento
from tiss.ctm_consulta_guia import CtmConsultaGuia
from tiss.ctm_demonstrativo_analise_conta import CtmDemonstrativoAnaliseConta
from tiss.ctm_demonstrativo_pagamento import CtmDemonstrativoPagamento
from tiss.ctm_guia_lote import CtmGuiaLote
from tiss.ctm_honorario_individual_guia import CtmHonorarioIndividualGuia
from tiss.ctm_internacao_dados import CtmInternacaoDados
from tiss.ctm_internacao_dados_saida import CtmInternacaoDadosSaida
from tiss.ctm_internacao_resumo_guia import CtmInternacaoResumoGuia
from tiss.ctm_internacao_solicitacao_guia import CtmInternacaoSolicitacaoGuia
from tiss.ctm_prorrogacao_solicitacao_guia import CtmProrrogacaoSolicitacaoGuia
from tiss.ctm_recurso_glosa import CtmRecursoGlosa
from tiss.ctm_solicitacao_lote import CtmSolicitacaoLote
from tiss.ctm_sp_sadt_atendimento import CtmSpSadtAtendimento
from tiss.ctm_sp_sadt_guia import CtmSpSadtGuia
from tiss.ctm_sp_sadt_solicitacao_guia import CtmSpSadtSolicitacaoGuia
from tiss.cto_anexo_situacao_inicial import CtoAnexoSituacaoInicial
from tiss.cto_anexo_situacao_inicialna_gto import CtoAnexoSituacaoInicialnaGto
from tiss.cto_autorizacao_servico import CtoAutorizacaoServico
from tiss.cto_demonstrativo_odontologia import CtoDemonstrativoOdontologia
from tiss.cto_guia_odontologia import CtoGuiaOdontologia
from tiss.cto_odonto_solicitacao_guia import CtoOdontoSolicitacaoGuia
from tiss.cto_recurso_glosa_odonto import CtoRecursoGlosaOdonto
from tiss.demonstrativo_retorno_ws import DemonstrativoRetornoWs
from tiss.digest_method import DigestMethod
from tiss.digest_method_type import DigestMethodType
from tiss.digest_value import DigestValue
from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao
from tiss.dm_carater_atendimento import DmCaraterAtendimento
from tiss.dm_cbos import DmCbos
from tiss.dm_cob_esp import DmCobEsp
from tiss.dm_condicao_clinica import DmCondicaoClinica
from tiss.dm_conselho_profissional import DmConselhoProfissional
from tiss.dm_debito_credito_indicador import DmDebitoCreditoIndicador
from tiss.dm_debito_credito_tipo import DmDebitoCreditoTipo
from tiss.dm_dente import DmDente
from tiss.dm_diagnostico_imagem import DmDiagnosticoImagem
from tiss.dm_ecog import DmEcog
from tiss.dm_estadiamento import DmEstadiamento
from tiss.dm_etapas_autorizacao import DmEtapasAutorizacao
from tiss.dm_finalidade_tratamento import DmFinalidadeTratamento
from tiss.dm_forma_pagamento import DmFormaPagamento
from tiss.dm_formato_documento import DmFormatoDocumento
from tiss.dm_grau_part import DmGrauPart
from tiss.dm_indicador_acidente import DmIndicadorAcidente
from tiss.dm_metastase import DmMetastase
from tiss.dm_motivo_saida import DmMotivoSaida
from tiss.dm_motivo_saida_obito import DmMotivoSaidaObito
from tiss.dm_nodulo import DmNodulo
from tiss.dm_objeto_recurso import DmObjetoRecurso
from tiss.dm_opcao_fabricante import DmOpcaoFabricante
from tiss.dm_outras_despesas import DmOutrasDespesas
from tiss.dm_regiao import DmRegiao
from tiss.dm_regime_atendimento import DmRegimeAtendimento
from tiss.dm_regime_internacao import DmRegimeInternacao
from tiss.dm_saude_ocupacional import DmSaudeOcupacional
from tiss.dm_sexo import DmSexo
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_status_cancelamento import DmStatusCancelamento
from tiss.dm_status_protocolo import DmStatusProtocolo
from tiss.dm_status_solicitacao import DmStatusSolicitacao
from tiss.dm_tabela import DmTabela
from tiss.dm_tabelas_diagnostico import DmTabelasDiagnostico
from tiss.dm_tecnica_utilizada import DmTecnicaUtilizada
from tiss.dm_tipo_acomodacao import DmTipoAcomodacao
from tiss.dm_tipo_atendimento import DmTipoAtendimento
from tiss.dm_tipo_atendimento_odonto import DmTipoAtendimentoOdonto
from tiss.dm_tipo_consulta import DmTipoConsulta
from tiss.dm_tipo_demonstrativo import DmTipoDemonstrativo
from tiss.dm_tipo_demonstrativo_pagamento import DmTipoDemonstrativoPagamento
from tiss.dm_tipo_documento import DmTipoDocumento
from tiss.dm_tipo_evento import DmTipoEvento
from tiss.dm_tipo_faturamento import DmTipoFaturamento
from tiss.dm_tipo_faturamento_odonto import DmTipoFaturamentoOdonto
from tiss.dm_tipo_glosa import DmTipoGlosa
from tiss.dm_tipo_guia import DmTipoGuia
from tiss.dm_tipo_ident import DmTipoIdent
from tiss.dm_tipo_internacao import DmTipoInternacao
from tiss.dm_tipo_lancamento import DmTipoLancamento
from tiss.dm_tipo_pagamento import DmTipoPagamento
from tiss.dm_tipo_quimioterapia import DmTipoQuimioterapia
from tiss.dm_tipo_transacao import DmTipoTransacao
from tiss.dm_tumor import DmTumor
from tiss.dm_uf import DmUf
from tiss.dm_unidade_medida import DmUnidadeMedida
from tiss.dm_unidade_tempo_ciclo import DmUnidadeTempoCiclo
from tiss.dm_versao import DmVersao
from tiss.dm_via_administracao import DmViaAdministracao
from tiss.dm_via_de_acesso import DmViaDeAcesso
from tiss.dsakey_value import DsakeyValue
from tiss.dsakey_value_type import DsakeyValueType
from tiss.envio_documento_ws import EnvioDocumentoWs
from tiss.epilogo import Epilogo
from tiss.key_info import KeyInfo
from tiss.key_info_type import KeyInfoType
from tiss.key_name import KeyName
from tiss.key_value import KeyValue
from tiss.key_value_type import KeyValueType
from tiss.lote_anexo_ws import LoteAnexoWs
from tiss.lote_guias_ws import LoteGuiasWs
from tiss.lote_recurso_glosa_ws import LoteRecursoGlosaWs
from tiss.manifest import Manifest
from tiss.manifest_type import ManifestType
from tiss.mensagem_tiss import MensagemTiss
from tiss.mgmt_data import MgmtData
from tiss.object_mod import Object
from tiss.object_type import ObjectType
from tiss.operadora_prestador import OperadoraPrestador
from tiss.pedido_elegibilidade_ws import PedidoElegibilidadeWs
from tiss.pgpdata import Pgpdata
from tiss.pgpdata_type import PgpdataType
from tiss.prestador_operadora import PrestadorOperadora
from tiss.protocolo_recebimento_anexo_ws import ProtocoloRecebimentoAnexoWs
from tiss.protocolo_recebimento_recurso_ws import ProtocoloRecebimentoRecursoWs
from tiss.protocolo_recebimento_ws import ProtocoloRecebimentoWs
from tiss.recibo_cancela_guia_ws import ReciboCancelaGuiaWs
from tiss.recibo_comunicacao_ws import ReciboComunicacaoWs
from tiss.recibo_documentos_ws import ReciboDocumentosWs
from tiss.reference import Reference
from tiss.reference_type import ReferenceType
from tiss.resposta_elegibilidade_ws import RespostaElegibilidadeWs
from tiss.retrieval_method import RetrievalMethod
from tiss.retrieval_method_type import RetrievalMethodType
from tiss.rsakey_value import RsakeyValue
from tiss.rsakey_value_type import RsakeyValueType
from tiss.signature import Signature
from tiss.signature_1 import Signature1
from tiss.signature_method import SignatureMethod
from tiss.signature_method_type import SignatureMethodType
from tiss.signature_properties import SignatureProperties
from tiss.signature_properties_type import SignaturePropertiesType
from tiss.signature_property import SignatureProperty
from tiss.signature_property_type import SignaturePropertyType
from tiss.signature_type import SignatureType
from tiss.signature_value import SignatureValue
from tiss.signature_value_type import SignatureValueType
from tiss.signed_info import SignedInfo
from tiss.signed_info_type import SignedInfoType
from tiss.situacao_autorizacao_ws import SituacaoAutorizacaoWs
from tiss.situacao_protocolo_recurso_ws import SituacaoProtocoloRecursoWs
from tiss.situacao_protocolo_ws import SituacaoProtocoloWs
from tiss.solicitacao_demonstrativo_retorno_ws import (
    SolicitacaoDemonstrativoRetornoWs,
)
from tiss.solicitacao_procedimento_ws import SolicitacaoProcedimentoWs
from tiss.solicitacao_status_autorizacao_ws import (
    SolicitacaoStatusAutorizacaoWs,
)
from tiss.solicitacao_status_protocolo_ws import SolicitacaoStatusProtocoloWs
from tiss.solicitacao_status_recurso_glosa_ws import (
    SolicitacaoStatusRecursoGlosaWs,
)
from tiss.spkidata import Spkidata
from tiss.spkidata_type import SpkidataType
from tiss.st_tiss_fault import StTissFault
from tiss.tiss_cancela_guia_port_type_tiss_cancela_guia_operation import (
    TissCancelaGuiaPortTypeTissCancelaGuiaOperation,
)
from tiss.tiss_cancela_guia_port_type_tiss_cancela_guia_operation_input import (
    TissCancelaGuiaPortTypeTissCancelaGuiaOperationInput,
)
from tiss.tiss_cancela_guia_port_type_tiss_cancela_guia_operation_output import (
    TissCancelaGuiaPortTypeTissCancelaGuiaOperationOutput,
)
from tiss.tiss_comunicacao_beneficiario_port_type_tiss_comunicacao_beneficiario_operation import (
    TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperation,
)
from tiss.tiss_comunicacao_beneficiario_port_type_tiss_comunicacao_beneficiario_operation_input import (
    TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationInput,
)
from tiss.tiss_comunicacao_beneficiario_port_type_tiss_comunicacao_beneficiario_operation_output import (
    TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationOutput,
)
from tiss.tiss_envio_documentos_port_type_tiss_envio_documentos_operation import (
    TissEnvioDocumentosPortTypeTissEnvioDocumentosOperation,
)
from tiss.tiss_envio_documentos_port_type_tiss_envio_documentos_operation_input import (
    TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationInput,
)
from tiss.tiss_envio_documentos_port_type_tiss_envio_documentos_operation_output import (
    TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationOutput,
)
from tiss.tiss_fault_ws import TissFaultWs
from tiss.tiss_lote_anexo_port_type_tiss_lote_anexo_operation import (
    TissLoteAnexoPortTypeTissLoteAnexoOperation,
)
from tiss.tiss_lote_anexo_port_type_tiss_lote_anexo_operation_input import (
    TissLoteAnexoPortTypeTissLoteAnexoOperationInput,
)
from tiss.tiss_lote_anexo_port_type_tiss_lote_anexo_operation_output import (
    TissLoteAnexoPortTypeTissLoteAnexoOperationOutput,
)
from tiss.tiss_lote_guias_port_type_tiss_lote_guias_operation import (
    TissLoteGuiasPortTypeTissLoteGuiasOperation,
)
from tiss.tiss_lote_guias_port_type_tiss_lote_guias_operation_input import (
    TissLoteGuiasPortTypeTissLoteGuiasOperationInput,
)
from tiss.tiss_lote_guias_port_type_tiss_lote_guias_operation_output import (
    TissLoteGuiasPortTypeTissLoteGuiasOperationOutput,
)
from tiss.tiss_recurso_glosa_port_type_tiss_recurso_glosa_operation import (
    TissRecursoGlosaPortTypeTissRecursoGlosaOperation,
)
from tiss.tiss_recurso_glosa_port_type_tiss_recurso_glosa_operation_input import (
    TissRecursoGlosaPortTypeTissRecursoGlosaOperationInput,
)
from tiss.tiss_recurso_glosa_port_type_tiss_recurso_glosa_operation_output import (
    TissRecursoGlosaPortTypeTissRecursoGlosaOperationOutput,
)
from tiss.tiss_solicitacao_demonstrativo_retorno_port_type_tiss_solicitacao_demonstrativo_retorno_operation import (
    TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperation,
)
from tiss.tiss_solicitacao_demonstrativo_retorno_port_type_tiss_solicitacao_demonstrativo_retorno_operation_input import (
    TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationInput,
)
from tiss.tiss_solicitacao_demonstrativo_retorno_port_type_tiss_solicitacao_demonstrativo_retorno_operation_output import (
    TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationOutput,
)
from tiss.tiss_solicitacao_procedimento_port_type_tiss_solicitacao_procedimento_operation import (
    TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperation,
)
from tiss.tiss_solicitacao_procedimento_port_type_tiss_solicitacao_procedimento_operation_input import (
    TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationInput,
)
from tiss.tiss_solicitacao_procedimento_port_type_tiss_solicitacao_procedimento_operation_output import (
    TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationOutput,
)
from tiss.tiss_solicitacao_status_autorizacao_port_type_tiss_solicitacao_status_autorizacao_operation import (
    TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperation,
)
from tiss.tiss_solicitacao_status_autorizacao_port_type_tiss_solicitacao_status_autorizacao_operation_input import (
    TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationInput,
)
from tiss.tiss_solicitacao_status_autorizacao_port_type_tiss_solicitacao_status_autorizacao_operation_output import (
    TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationOutput,
)
from tiss.tiss_solicitacao_status_protocolo_port_type_tiss_solicitacao_status_protocolo_operation import (
    TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperation,
)
from tiss.tiss_solicitacao_status_protocolo_port_type_tiss_solicitacao_status_protocolo_operation_input import (
    TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationInput,
)
from tiss.tiss_solicitacao_status_protocolo_port_type_tiss_solicitacao_status_protocolo_operation_output import (
    TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationOutput,
)
from tiss.tiss_solicitacao_status_protocolo_recurso_port_type_tiss_solicitacao_status_protocolo_recurso_operation import (
    TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperation,
)
from tiss.tiss_solicitacao_status_protocolo_recurso_port_type_tiss_solicitacao_status_protocolo_recurso_operation_input import (
    TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationInput,
)
from tiss.tiss_solicitacao_status_protocolo_recurso_port_type_tiss_solicitacao_status_protocolo_recurso_operation_output import (
    TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationOutput,
)
from tiss.tiss_verifica_elegibilidade_port_type_tiss_verifica_elegibilidade_operation import (
    TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperation,
)
from tiss.tiss_verifica_elegibilidade_port_type_tiss_verifica_elegibilidade_operation_input import (
    TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationInput,
)
from tiss.tiss_verifica_elegibilidade_port_type_tiss_verifica_elegibilidade_operation_output import (
    TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationOutput,
)
from tiss.transform import Transform
from tiss.transform_type import TransformType
from tiss.transforms import Transforms
from tiss.transforms_type import TransformsType
from tiss.x509_data import X509Data
from tiss.x509_data_type import X509DataType
from tiss.x509_issuer_serial_type import X509IssuerSerialType

__all__ = [
    "AutorizacaoProcedimentoWs",
    "CabecalhoTransacao",
    "CancelaGuiaWs",
    "CanonicalizationMethod",
    "CanonicalizationMethodType",
    "ComunicacaoBeneficiarioWs",
    "CtAnexoCabecalho",
    "CtAnexoLote",
    "CtAnexoRecebimento",
    "CtAutorizacaoDados",
    "CtAutorizacaoInternacao",
    "CtAutorizacaoSadt",
    "CtAutorizacaoSolicitaStatus",
    "CtBeneficiarioDados",
    "CtContaMedicaResumo",
    "CtContratadoDados",
    "CtContratadoDadosNome",
    "CtContratadoProfissionalDados",
    "CtCreditoOdonto",
    "CtDadosComplementaresBeneficiario",
    "CtDadosComplementaresBeneficiarioRadio",
    "CtDadosResumoDemonstrativo",
    "CtDemonstrativoCabecalho",
    "CtDemonstrativoRetorno",
    "CtDemonstrativoSolicitacao",
    "CtDescontos",
    "CtDiagnostico",
    "CtDiagnosticoOncologico",
    "CtDrogasSolicitadas",
    "CtElegibilidadeRecibo",
    "CtElegibilidadeVerifica",
    "CtEnvioDocumentos",
    "CtFontePagadora",
    "CtGlosaRecibo",
    "CtGlosaReciboOdonto",
    "CtGuiaCabecalho",
    "CtGuiaCancelamento",
    "CtGuiaCancelamentoRecibo",
    "CtGuiaDados",
    "CtGuiaDadosAnexo",
    "CtGuiaDadosOdonto",
    "CtGuiaRecurso",
    "CtGuiaRecursoLote",
    "CtGuiaValorTotal",
    "CtGuiaValorTotalSadt",
    "CtHipoteseDiagnostica",
    "CtIdentEquipe",
    "CtIdentEquipeSadt",
    "CtIntervaloCiclos",
    "CtLoginSenha",
    "CtLoteAnexoStatus",
    "CtLoteStatus",
    "CtMotivoGlosa",
    "CtOpmUtilizada",
    "CtOpmeDados",
    "CtOutrasDespesas",
    "CtPagamentoDados",
    "CtPagamentoResumo",
    "CtPrestadorIdentificacao",
    "CtProcedimentoAutorizado",
    "CtProcedimentoDados",
    "CtProcedimentoExecutado",
    "CtProcedimentoExecutadoHonorIndiv",
    "CtProcedimentoExecutadoInt",
    "CtProcedimentoExecutadoOdonto",
    "CtProcedimentoExecutadoOutras",
    "CtProcedimentoExecutadoSadt",
    "CtProcedimentoSolicitado",
    "CtProcedimentosComplementares",
    "CtProtocoloAnexoStatus",
    "CtProtocoloDetalhe",
    "CtProtocoloDetalheAnexo",
    "CtProtocoloRecebimento",
    "CtProtocoloRecebimentoAnexo",
    "CtProtocoloRecebimentoRecurso",
    "CtProtocoloRecurso",
    "CtProtocoloSolicitacaoStatus",
    "CtProtocoloStatus",
    "CtRecebimentoLote",
    "CtRecebimentoRecurso",
    "CtReciboCancelaGuia",
    "CtReciboComunicacao",
    "CtReciboDocumentos",
    "CtRecursoGlosaRecebimento",
    "CtRespostaElegibilidade",
    "CtRespostaGlosa",
    "CtRespostaGlosaGuiaMedica",
    "CtRespostaGlosaItemMedico",
    "CtRespostaRecursoGuiaOdonto",
    "CtRespostaRecursoItemOdonto",
    "CtSituacaoAutorizacao",
    "CtSituacaoClinica",
    "CtSituacaoProtocolo",
    "CtSolicitacaoProcedimento",
    "CtValorCreditoDesconto",
    "CtValorTotal",
    "CtmAnexoSolicitacaoOpme",
    "CtmAnexoSolicitacaoQuimio",
    "CtmAnexoSolicitacaoRadio",
    "CtmAnexoSolicitante",
    "CtmAutorizacaoInternacao",
    "CtmAutorizacaoOpme",
    "CtmAutorizacaoProrrogacao",
    "CtmAutorizacaoQuimio",
    "CtmAutorizacaoRadio",
    "CtmAutorizacaoServico",
    "CtmBeneficiarioComunicacao",
    "CtmBeneficiarioComunicacaoRecibo",
    "CtmBeneficiarioComunicacaoRet",
    "CtmConsultaAtendimento",
    "CtmConsultaGuia",
    "CtmDemonstrativoAnaliseConta",
    "CtmDemonstrativoPagamento",
    "CtmGuiaLote",
    "CtmHonorarioIndividualGuia",
    "CtmInternacaoDados",
    "CtmInternacaoDadosSaida",
    "CtmInternacaoResumoGuia",
    "CtmInternacaoSolicitacaoGuia",
    "CtmProrrogacaoSolicitacaoGuia",
    "CtmRecursoGlosa",
    "CtmSolicitacaoLote",
    "CtmSpSadtAtendimento",
    "CtmSpSadtGuia",
    "CtmSpSadtSolicitacaoGuia",
    "CtoAnexoSituacaoInicial",
    "CtoAnexoSituacaoInicialnaGto",
    "CtoAutorizacaoServico",
    "CtoDemonstrativoOdontologia",
    "CtoGuiaOdontologia",
    "CtoOdontoSolicitacaoGuia",
    "CtoRecursoGlosaOdonto",
    "DemonstrativoRetornoWs",
    "DigestMethod",
    "DigestMethodType",
    "DigestValue",
    "DmAusenciaCodValidacao",
    "DmCaraterAtendimento",
    "DmCbos",
    "DmCobEsp",
    "DmCondicaoClinica",
    "DmConselhoProfissional",
    "DmDebitoCreditoIndicador",
    "DmDebitoCreditoTipo",
    "DmDente",
    "DmDiagnosticoImagem",
    "DmEcog",
    "DmEstadiamento",
    "DmEtapasAutorizacao",
    "DmFinalidadeTratamento",
    "DmFormaPagamento",
    "DmFormatoDocumento",
    "DmGrauPart",
    "DmIndicadorAcidente",
    "DmMetastase",
    "DmMotivoSaida",
    "DmMotivoSaidaObito",
    "DmNodulo",
    "DmObjetoRecurso",
    "DmOpcaoFabricante",
    "DmOutrasDespesas",
    "DmRegiao",
    "DmRegimeAtendimento",
    "DmRegimeInternacao",
    "DmSaudeOcupacional",
    "DmSexo",
    "DmSimNao",
    "DmStatusCancelamento",
    "DmStatusProtocolo",
    "DmStatusSolicitacao",
    "DmTabela",
    "DmTabelasDiagnostico",
    "DmTecnicaUtilizada",
    "DmTipoAcomodacao",
    "DmTipoAtendimento",
    "DmTipoAtendimentoOdonto",
    "DmTipoConsulta",
    "DmTipoDemonstrativo",
    "DmTipoDemonstrativoPagamento",
    "DmTipoDocumento",
    "DmTipoEvento",
    "DmTipoFaturamento",
    "DmTipoFaturamentoOdonto",
    "DmTipoGlosa",
    "DmTipoGuia",
    "DmTipoIdent",
    "DmTipoInternacao",
    "DmTipoLancamento",
    "DmTipoPagamento",
    "DmTipoQuimioterapia",
    "DmTipoTransacao",
    "DmTumor",
    "DmUf",
    "DmUnidadeMedida",
    "DmUnidadeTempoCiclo",
    "DmVersao",
    "DmViaAdministracao",
    "DmViaDeAcesso",
    "DsakeyValue",
    "DsakeyValueType",
    "EnvioDocumentoWs",
    "Epilogo",
    "KeyInfo",
    "KeyInfoType",
    "KeyName",
    "KeyValue",
    "KeyValueType",
    "LoteAnexoWs",
    "LoteGuiasWs",
    "LoteRecursoGlosaWs",
    "Manifest",
    "ManifestType",
    "MensagemTiss",
    "MgmtData",
    "Object",
    "ObjectType",
    "OperadoraPrestador",
    "PedidoElegibilidadeWs",
    "Pgpdata",
    "PgpdataType",
    "PrestadorOperadora",
    "ProtocoloRecebimentoAnexoWs",
    "ProtocoloRecebimentoRecursoWs",
    "ProtocoloRecebimentoWs",
    "ReciboCancelaGuiaWs",
    "ReciboComunicacaoWs",
    "ReciboDocumentosWs",
    "Reference",
    "ReferenceType",
    "RespostaElegibilidadeWs",
    "RetrievalMethod",
    "RetrievalMethodType",
    "RsakeyValue",
    "RsakeyValueType",
    "Signature",
    "Signature1",
    "SignatureMethod",
    "SignatureMethodType",
    "SignatureProperties",
    "SignaturePropertiesType",
    "SignatureProperty",
    "SignaturePropertyType",
    "SignatureType",
    "SignatureValue",
    "SignatureValueType",
    "SignedInfo",
    "SignedInfoType",
    "SituacaoAutorizacaoWs",
    "SituacaoProtocoloRecursoWs",
    "SituacaoProtocoloWs",
    "SolicitacaoDemonstrativoRetornoWs",
    "SolicitacaoProcedimentoWs",
    "SolicitacaoStatusAutorizacaoWs",
    "SolicitacaoStatusProtocoloWs",
    "SolicitacaoStatusRecursoGlosaWs",
    "Spkidata",
    "SpkidataType",
    "StTissFault",
    "TissCancelaGuiaPortTypeTissCancelaGuiaOperation",
    "TissCancelaGuiaPortTypeTissCancelaGuiaOperationInput",
    "TissCancelaGuiaPortTypeTissCancelaGuiaOperationOutput",
    "TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperation",
    "TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationInput",
    "TissComunicacaoBeneficiarioPortTypeTissComunicacaoBeneficiarioOperationOutput",
    "TissEnvioDocumentosPortTypeTissEnvioDocumentosOperation",
    "TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationInput",
    "TissEnvioDocumentosPortTypeTissEnvioDocumentosOperationOutput",
    "TissFaultWs",
    "TissLoteAnexoPortTypeTissLoteAnexoOperation",
    "TissLoteAnexoPortTypeTissLoteAnexoOperationInput",
    "TissLoteAnexoPortTypeTissLoteAnexoOperationOutput",
    "TissLoteGuiasPortTypeTissLoteGuiasOperation",
    "TissLoteGuiasPortTypeTissLoteGuiasOperationInput",
    "TissLoteGuiasPortTypeTissLoteGuiasOperationOutput",
    "TissRecursoGlosaPortTypeTissRecursoGlosaOperation",
    "TissRecursoGlosaPortTypeTissRecursoGlosaOperationInput",
    "TissRecursoGlosaPortTypeTissRecursoGlosaOperationOutput",
    "TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperation",
    "TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationInput",
    "TissSolicitacaoDemonstrativoRetornoPortTypeTissSolicitacaoDemonstrativoRetornoOperationOutput",
    "TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperation",
    "TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationInput",
    "TissSolicitacaoProcedimentoPortTypeTissSolicitacaoProcedimentoOperationOutput",
    "TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperation",
    "TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationInput",
    "TissSolicitacaoStatusAutorizacaoPortTypeTissSolicitacaoStatusAutorizacaoOperationOutput",
    "TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperation",
    "TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationInput",
    "TissSolicitacaoStatusProtocoloPortTypeTissSolicitacaoStatusProtocoloOperationOutput",
    "TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperation",
    "TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationInput",
    "TissSolicitacaoStatusProtocoloRecursoPortTypeTissSolicitacaoStatusProtocoloRecursoOperationOutput",
    "TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperation",
    "TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationInput",
    "TissVerificaElegibilidadePortTypeTissVerificaElegibilidadeOperationOutput",
    "Transform",
    "TransformType",
    "Transforms",
    "TransformsType",
    "X509Data",
    "X509DataType",
    "X509IssuerSerialType",
]

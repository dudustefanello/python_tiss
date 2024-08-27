from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlTime

from tiss.ct_login_senha import CtLoginSenha
from tiss.ct_prestador_identificacao import CtPrestadorIdentificacao
from tiss.dm_tipo_glosa import DmTipoGlosa
from tiss.dm_tipo_transacao import DmTipoTransacao
from tiss.dm_versao import DmVersao

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CabecalhoTransacao:
    class Meta:
        name = "cabecalhoTransacao"

    identificacao_transacao: Optional[
        "CabecalhoTransacao.IdentificacaoTransacao"
    ] = field(
        default=None,
        metadata={
            "name": "identificacaoTransacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    falha_negocio: Optional[DmTipoGlosa] = field(
        default=None,
        metadata={
            "name": "falhaNegocio",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    origem: Optional["CabecalhoTransacao.Origem"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    destino: Optional["CabecalhoTransacao.Destino"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    padrao: Optional[DmVersao] = field(
        default=None,
        metadata={
            "name": "Padrao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    login_senha_prestador: Optional[CtLoginSenha] = field(
        default=None,
        metadata={
            "name": "loginSenhaPrestador",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class IdentificacaoTransacao:
        tipo_transacao: Optional[DmTipoTransacao] = field(
            default=None,
            metadata={
                "name": "tipoTransacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        sequencial_transacao: Optional[str] = field(
            default=None,
            metadata={
                "name": "sequencialTransacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 12,
            },
        )
        data_registro_transacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataRegistroTransacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        hora_registro_transacao: Optional[XmlTime] = field(
            default=None,
            metadata={
                "name": "horaRegistroTransacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

    @dataclass
    class Origem:
        identificacao_prestador: Optional[CtPrestadorIdentificacao] = field(
            default=None,
            metadata={
                "name": "identificacaoPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        registro_ans: Optional[str] = field(
            default=None,
            metadata={
                "name": "registroANS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_length": 6,
                "pattern": r"[0-9]{6}",
            },
        )

    @dataclass
    class Destino:
        identificacao_prestador: Optional[CtPrestadorIdentificacao] = field(
            default=None,
            metadata={
                "name": "identificacaoPrestador",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        registro_ans: Optional[str] = field(
            default=None,
            metadata={
                "name": "registroANS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_length": 6,
                "pattern": r"[0-9]{6}",
            },
        )

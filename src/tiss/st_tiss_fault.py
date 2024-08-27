from enum import Enum

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


class StTissFault(Enum):
    DESTINATARIO_INVALIDO = "DestinatarioInvalido"
    REMETENTE_INVALIDO = "RemetenteInvalido"
    LOGIN_INVALIDO = "LoginInvalido"
    VERSAO_INVALIDA = "VersaoInvalida"
    HASH_INVALIDO = "HashInvalido"
    SCHEMA_INVALIDO = "SchemaInvalido"
    ERRO_INESPERADO_SERVIDOR = "ErroInesperadoServidor"

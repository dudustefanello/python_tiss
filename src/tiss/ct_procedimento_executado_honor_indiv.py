from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlTime

from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.dm_cbos import DmCbos
from tiss.dm_conselho_profissional import DmConselhoProfissional
from tiss.dm_grau_part import DmGrauPart
from tiss.dm_tecnica_utilizada import DmTecnicaUtilizada
from tiss.dm_uf import DmUf
from tiss.dm_via_de_acesso import DmViaDeAcesso

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtProcedimentoExecutadoHonorIndiv:
    class Meta:
        name = "ct_procedimentoExecutadoHonorIndiv"

    sequencial_item: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequencialItem",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 4,
        },
    )
    data_execucao: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataExecucao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    hora_inicial: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaInicial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    hora_final: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "horaFinal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    procedimento: Optional[CtProcedimentoDados] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    quantidade_executada: Optional[int] = field(
        default=None,
        metadata={
            "name": "quantidadeExecutada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
        },
    )
    via_acesso: Optional[DmViaDeAcesso] = field(
        default=None,
        metadata={
            "name": "viaAcesso",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    tecnica_utilizada: Optional[DmTecnicaUtilizada] = field(
        default=None,
        metadata={
            "name": "tecnicaUtilizada",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    reducao_acrescimo: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "reducaoAcrescimo",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 3,
            "fraction_digits": 2,
        },
    )
    valor_unitario: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorUnitario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    valor_total: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    profissionais: List["CtProcedimentoExecutadoHonorIndiv.Profissionais"] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_occurs": 1,
            },
        )
    )

    @dataclass
    class Profissionais:
        grau_participacao: Optional[DmGrauPart] = field(
            default=None,
            metadata={
                "name": "grauParticipacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        cod_profissional: Optional[
            "CtProcedimentoExecutadoHonorIndiv.Profissionais.CodProfissional"
        ] = field(
            default=None,
            metadata={
                "name": "codProfissional",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        nome_profissional: Optional[str] = field(
            default=None,
            metadata={
                "name": "nomeProfissional",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 70,
            },
        )
        conselho_profissional: Optional[DmConselhoProfissional] = field(
            default=None,
            metadata={
                "name": "conselhoProfissional",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        numero_conselho_profissional: Optional[str] = field(
            default=None,
            metadata={
                "name": "numeroConselhoProfissional",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 15,
            },
        )
        uf: Optional[DmUf] = field(
            default=None,
            metadata={
                "name": "UF",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        cbo: Optional[DmCbos] = field(
            default=None,
            metadata={
                "name": "CBO",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

        @dataclass
        class CodProfissional:
            codigo_prestador_na_operadora: Optional[str] = field(
                default=None,
                metadata={
                    "name": "codigoPrestadorNaOperadora",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "min_length": 1,
                    "max_length": 14,
                },
            )
            cpf_contratado: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cpfContratado",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                    "pattern": r"[0-9]{11}",
                },
            )

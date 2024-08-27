from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate

from tiss.ct_procedimento_dados import CtProcedimentoDados
from tiss.cto_anexo_situacao_inicial import CtoAnexoSituacaoInicial
from tiss.dm_ausencia_cod_validacao import DmAusenciaCodValidacao
from tiss.dm_cbos import DmCbos
from tiss.dm_dente import DmDente
from tiss.dm_regiao import DmRegiao
from tiss.dm_sim_nao import DmSimNao
from tiss.dm_tipo_atendimento_odonto import DmTipoAtendimentoOdonto
from tiss.dm_tipo_ident import DmTipoIdent
from tiss.dm_uf import DmUf

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtoOdontoSolicitacaoGuia:
    class Meta:
        name = "cto_odontoSolicitacaoGuia"

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
    numero_guia_principal: Optional[str] = field(
        default=None,
        metadata={
            "name": "numeroGuiaPrincipal",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 20,
        },
    )
    ausencia_cod_validacao: Optional[DmAusenciaCodValidacao] = field(
        default=None,
        metadata={
            "name": "ausenciaCodValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    cod_validacao: Optional[str] = field(
        default=None,
        metadata={
            "name": "codValidacao",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 10,
        },
    )
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
    atendimento_rn: Optional[DmSimNao] = field(
        default=None,
        metadata={
            "name": "atendimentoRN",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
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
    plano_beneficiario: Optional[str] = field(
        default=None,
        metadata={
            "name": "planoBeneficiario",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "min_length": 1,
            "max_length": 40,
        },
    )
    nome_empresa: Optional[str] = field(
        default=None,
        metadata={
            "name": "nomeEmpresa",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_length": 1,
            "max_length": 40,
        },
    )
    dados_profissionais_responsaveis: Optional[
        "CtoOdontoSolicitacaoGuia.DadosProfissionaisResponsaveis"
    ] = field(
        default=None,
        metadata={
            "name": "dadosProfissionaisResponsaveis",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    procedimentos_solicitados: List[
        "CtoOdontoSolicitacaoGuia.ProcedimentosSolicitados"
    ] = field(
        default_factory=list,
        metadata={
            "name": "procedimentosSolicitados",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "min_occurs": 1,
        },
    )
    data_termino_trat: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dataTerminoTrat",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )
    tipo_atendimento: Optional[DmTipoAtendimentoOdonto] = field(
        default=None,
        metadata={
            "name": "tipoAtendimento",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )
    qtd_total_us: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "qtdTotalUS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    valor_total_proc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalProc",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    valor_total_franquia: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "valorTotalFranquia",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "total_digits": 8,
            "fraction_digits": 2,
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
    odonto_inicial: Optional[CtoAnexoSituacaoInicial] = field(
        default=None,
        metadata={
            "name": "odontoInicial",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
        },
    )

    @dataclass
    class DadosProfissionaisResponsaveis:
        nome_prof_solic: Optional[str] = field(
            default=None,
            metadata={
                "name": "nomeProfSolic",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 70,
            },
        )
        cro_solic: Optional[str] = field(
            default=None,
            metadata={
                "name": "croSolic",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 20,
            },
        )
        uf_solic: Optional[DmUf] = field(
            default=None,
            metadata={
                "name": "ufSolic",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        cbos_solic: Optional[DmCbos] = field(
            default=None,
            metadata={
                "name": "cbosSolic",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        codigo_prof_exec: Optional[str] = field(
            default=None,
            metadata={
                "name": "codigoProfExec",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 14,
            },
        )
        cro_exec: Optional[str] = field(
            default=None,
            metadata={
                "name": "croExec",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 20,
            },
        )
        uf_exec: Optional[DmUf] = field(
            default=None,
            metadata={
                "name": "ufExec",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        cnes_exec: Optional[str] = field(
            default=None,
            metadata={
                "name": "cnesExec",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "min_length": 1,
                "max_length": 7,
            },
        )
        nome_prof_exec2: Optional[str] = field(
            default=None,
            metadata={
                "name": "nomeProfExec2",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 70,
            },
        )
        cro_exec2: Optional[str] = field(
            default=None,
            metadata={
                "name": "croExec2",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 20,
            },
        )
        uf_exec2: Optional[DmUf] = field(
            default=None,
            metadata={
                "name": "ufExec2",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        cbos_exec2: Optional[DmCbos] = field(
            default=None,
            metadata={
                "name": "cbosExec2",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )

    @dataclass
    class ProcedimentosSolicitados:
        proc_solic: Optional[CtProcedimentoDados] = field(
            default=None,
            metadata={
                "name": "procSolic",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        dente_regiao: Optional[
            "CtoOdontoSolicitacaoGuia.ProcedimentosSolicitados.DenteRegiao"
        ] = field(
            default=None,
            metadata={
                "name": "denteRegiao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )
        dente_face: Optional[str] = field(
            default=None,
            metadata={
                "name": "denteFace",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "min_length": 1,
                "max_length": 5,
            },
        )
        qtd_proc: Optional[int] = field(
            default=None,
            metadata={
                "name": "qtdProc",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 2,
            },
        )
        qtd_us: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "qtdUS",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "total_digits": 7,
                "fraction_digits": 2,
            },
        )
        valor_proc: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorProc",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )
        valor_franquia: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "valorFranquia",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "total_digits": 8,
                "fraction_digits": 2,
            },
        )
        aut: Optional[DmSimNao] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "required": True,
            },
        )
        data_realizacao: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "dataRealizacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            },
        )

        @dataclass
        class DenteRegiao:
            cod_dente: Optional[DmDente] = field(
                default=None,
                metadata={
                    "name": "codDente",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )
            cod_regiao: Optional[DmRegiao] = field(
                default=None,
                metadata={
                    "name": "codRegiao",
                    "type": "Element",
                    "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                },
            )

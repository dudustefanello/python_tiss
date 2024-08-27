from dataclasses import dataclass, field
from typing import List, Optional

from tiss.ctm_consulta_guia import CtmConsultaGuia
from tiss.ctm_honorario_individual_guia import CtmHonorarioIndividualGuia
from tiss.ctm_internacao_resumo_guia import CtmInternacaoResumoGuia
from tiss.ctm_sp_sadt_guia import CtmSpSadtGuia
from tiss.cto_guia_odontologia import CtoGuiaOdontologia

__NAMESPACE__ = "http://www.ans.gov.br/padroes/tiss/schemas"


@dataclass
class CtmGuiaLote:
    class Meta:
        name = "ctm_guiaLote"

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
    guias_tiss: Optional["CtmGuiaLote.GuiasTiss"] = field(
        default=None,
        metadata={
            "name": "guiasTISS",
            "type": "Element",
            "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
            "required": True,
        },
    )

    @dataclass
    class GuiasTiss:
        guia_sp_sadt: List[CtmSpSadtGuia] = field(
            default_factory=list,
            metadata={
                "name": "guiaSP-SADT",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
            },
        )
        guia_resumo_internacao: List[CtmInternacaoResumoGuia] = field(
            default_factory=list,
            metadata={
                "name": "guiaResumoInternacao",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
            },
        )
        guia_honorarios: List[CtmHonorarioIndividualGuia] = field(
            default_factory=list,
            metadata={
                "name": "guiaHonorarios",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
            },
        )
        guia_consulta: List[CtmConsultaGuia] = field(
            default_factory=list,
            metadata={
                "name": "guiaConsulta",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
            },
        )
        guia_odonto: List[CtoGuiaOdontologia] = field(
            default_factory=list,
            metadata={
                "name": "guiaOdonto",
                "type": "Element",
                "namespace": "http://www.ans.gov.br/padroes/tiss/schemas",
                "max_occurs": 100,
            },
        )

import tempfile
import unittest

from KOBLLUX_motor_137_delta import Motor137Delta, pipeline_value
from ativar_malha_viva import ativar_malha_viva_completa
from cerebro_oraculo_v1 import (
    ARCHETYPE_HZ,
    KOB_CICLO,
    KOB_FRACTAL,
    Aion_ancorar_temporalidade,
    Atlas_detectar_contexto,
    Artemis_mapear_precisao,
    Bllue_fluidificar_fluxo,
    Genus_organizar_estrutura,
    Jesus_centrar_em_verdade,
    Kaos_revelar_brechas,
    Kobllux_unificar_tudo,
    Kodux_codificar_mapa,
    Lumine_abrir_clareza,
    Nova_extrair_centelha,
    Pulse_medir_ressonancia,
    Rhea_preservar_memoria,
    Serena_acolher_integrar,
    Solus_sintetizar,
    Vitalis_identificar_cura,
)
from kobllux_contract import ARCHETYPES
from kobllux_loop import PIPELINE
from kobllux_memory import ARCHETYPES_META


class KoblluxContractTests(unittest.TestCase):
    def test_canonical_cycle_and_fractal_are_preserved(self):
        self.assertEqual(KOB_CICLO, (3, 6, 9, 7))
        self.assertEqual(KOB_FRACTAL, 1134)
        self.assertEqual(
            set(pipeline_value(432)),
            {"3_DETECTAR", "6_INTEGRAR", "9_EXPANDIR", "7_SELAR", "resultado", "alpha_137"},
        )

    def test_canonical_frequency_table_contains_all_sixteen_archetypes(self):
        self.assertEqual(len(ARCHETYPES), 16)
        self.assertEqual(ARCHETYPE_HZ["atlas"], 594)
        self.assertEqual(ARCHETYPE_HZ["kobllux"], 1134)

    def test_all_loop_handlers_use_canonical_frequencies(self):
        for handler in PIPELINE:
            with self.subTest(archetype=handler.nome):
                self.assertEqual(handler.hz, ARCHETYPE_HZ[handler.nome.casefold()])

    def test_loop_memory_records_all_canonical_archetype_tags(self):
        from kobllux_loop import EstadoKobllux

        record = EstadoKobllux("KOBLLUX").to_dict()
        self.assertEqual(len(record["arquetipos"]), 16)
        self.assertIn("archetype:aion", record["tags"])
        self.assertEqual(record["cycle"], [3, 6, 9, 7])
        self.assertEqual(record["fractal"], 1134)

    def test_memory_metadata_uses_canonical_frequencies(self):
        for name, hz in ARCHETYPE_HZ.items():
            with self.subTest(archetype=name):
                self.assertEqual(ARCHETYPES_META[name]["hz"], hz)

    def test_137_motor_overlays_codex_frequency_variants(self):
        motor = Motor137Delta()
        for archetype in motor.arqs:
            canonical_hz = ARCHETYPE_HZ.get(archetype["id"].casefold())
            if canonical_hz is not None:
                with self.subTest(archetype=archetype["id"]):
                    self.assertEqual(archetype["hz"], canonical_hz)

    def test_activation_agents_use_canonical_frequencies(self):
        result = ativar_malha_viva_completa()
        agents = {agent["nome"].casefold(): agent for agent in result["agentes"]}
        self.assertEqual(
            {name: agent["freq"] for name, agent in agents.items()},
            ARCHETYPE_HZ,
        )

    def test_oracle_handlers_report_canonical_frequencies(self):
        checks = (
            (Atlas_detectar_contexto, "Atlas"),
            (Nova_extrair_centelha, "Nova"),
            (Pulse_medir_ressonancia, "Pulse"),
            (Vitalis_identificar_cura, "Vitalis"),
            (Artemis_mapear_precisao, "Artemis"),
            (Kaos_revelar_brechas, "Kaos"),
            (Serena_acolher_integrar, "Serena"),
            (Genus_organizar_estrutura, "Genus"),
            (Lumine_abrir_clareza, "Lumine"),
            (Aion_ancorar_temporalidade, "Aion"),
        )
        for handler, archetype in checks:
            with self.subTest(archetype=archetype):
                result = handler("sample")
                self.assertEqual(result["hz"], ARCHETYPE_HZ[archetype.casefold()])

        with tempfile.TemporaryDirectory() as directory:
            result = Rhea_preservar_memoria("sample", f"{directory}/memory.jsonl")
            self.assertEqual(result["hz"], ARCHETYPE_HZ["rhea"])

        for handler, archetype in (
            (Kodux_codificar_mapa, "Kodux"),
            (Solus_sintetizar, "Solus"),
        ):
            with self.subTest(archetype=archetype):
                result = handler([])
                self.assertEqual(result["hz"], ARCHETYPE_HZ[archetype.casefold()])

        synthesis = Kobllux_unificar_tudo([], "sample")
        self.assertEqual(synthesis["hz"], ARCHETYPE_HZ["kobllux"])
        state = Jesus_centrar_em_verdade("sample", {})
        self.assertEqual(state["centro"], "JESUS = VERBO = GRAVIDADE")
        self.assertEqual(Bllue_fluidificar_fluxo("KOBLLUX"), "[KOBLLUX·9·BLLUE] KOBLLUX")


if __name__ == "__main__":
    unittest.main()

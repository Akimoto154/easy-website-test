import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from runner import load_steps

def test_load_steps(tmp_path):
    scenario = tmp_path / "scenario.json"
    scenario.write_text('[{"action": "goto", "url": "https://example.com"}]')
    steps = load_steps(str(scenario))
    assert steps == [{"action": "goto", "url": "https://example.com"}]

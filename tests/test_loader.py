import sys
import pathlib
import pytest

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from runner import load_steps


def test_load_steps(tmp_path):
    scenario = tmp_path / "scenario.json"
    scenario.write_text('[{"action": "goto", "url": "https://example.com"}]')
    steps = load_steps(str(scenario))
    assert steps == [{"action": "goto", "url": "https://example.com"}]


def test_load_steps_requires_action(tmp_path):
    scenario = tmp_path / "scenario.json"
    scenario.write_text('[{"url": "https://example.com"}]')
    with pytest.raises(ValueError):
        load_steps(str(scenario))


def test_load_steps_requires_dict(tmp_path):
    scenario = tmp_path / "scenario.json"
    scenario.write_text('[123]')
    with pytest.raises(ValueError):
        load_steps(str(scenario))


def test_load_steps_unknown_action(tmp_path):
    scenario = tmp_path / "scenario.json"
    scenario.write_text('[{"action": "dance"}]')
    with pytest.raises(ValueError):
        load_steps(str(scenario))

import importlib.util
from pathlib import Path


MAIN_PATH = Path(__file__).resolve().parents[1] / "main.py"

spec = importlib.util.spec_from_file_location("friday_main", MAIN_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_detect_intent_handles_memory_and_identity_commands():
    assert module.detect_intent("remember my name is Alex") == "remember"
    assert module.detect_intent("who am i") == "profile"
    assert module.detect_intent("what is my name") == "my_name"


def test_handle_memory_command_updates_memory():
    memory = {}
    result = module.handle_memory_command("remember my name is Alex", memory)

    assert result is True
    assert memory["name"] == "Alex"

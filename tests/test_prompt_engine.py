from src.prompt_engine import build_prompt


def test_prompt_contains_user_controls():
    prompt = build_prompt(
        "Please send the report.",
        "Business",
        "Professional",
        "Short",
        "Improve",
    )
    assert "Business" in prompt
    assert "Professional" in prompt
    assert "Short" in prompt
    assert "Please send the report." in prompt


def test_prompt_has_no_invented_fact_instruction():
    prompt = build_prompt("Hello", "General", "Friendly", "Medium", "Rewrite")
    assert "Do not invent" in prompt

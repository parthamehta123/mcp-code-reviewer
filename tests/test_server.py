import json
from mcp_code_reviewer import mcp_server


def test_analyze_code_detects_print():
    code = "def foo():\n    print('hi')"
    raw = mcp_server.analyze_code(code)
    result = json.loads(raw)
    assert "issues" in result
    assert any("print" in issue for issue in result["issues"])
    assert result["line_count"] == 2


def test_refactor_changes_print():
    code = "print('x')"
    raw = mcp_server.suggest_refactor(code)
    result = json.loads(raw)
    assert "original" in result
    assert "refactored" in result
    assert "logger.info(" in result["refactored"]


def test_write_tests_generates_code():
    code = "def foo(): return 1"
    raw = mcp_server.write_tests(code)
    result = json.loads(raw)
    assert "tests" in result
    assert "def test_" in result["tests"]

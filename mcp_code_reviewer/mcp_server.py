import logging, sys, json
from typing import Annotated
from mcp.server.fastmcp import FastMCP

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("mcp_server.log"), logging.StreamHandler(sys.stderr)],
)
logger = logging.getLogger("mcp-code-reviewer")

mcp = FastMCP("code-reviewer")


@mcp.tool()
def analyze_code(code: Annotated[str, "Source code to analyze"]) -> str:
    """Analyze code and return JSON with issues + line count."""
    issues = []
    if "print(" in code:
        issues.append("Consider using logging instead of print statements.")
    if len(code.splitlines()) > 50:
        issues.append("Function too long, consider refactoring.")
    result = {"issues": issues, "line_count": len(code.splitlines())}
    return json.dumps(result)


@mcp.tool()
def suggest_refactor(code: Annotated[str, "Source code to refactor"]) -> str:
    """Suggests a simple refactor (returns JSON)."""
    refactored = code.replace("print(", "logger.info(")
    return json.dumps({"original": code, "refactored": refactored})


@mcp.tool()
def write_tests(code: Annotated[str, "Source code to test"]) -> str:
    """Generates a dummy pytest test (returns JSON)."""
    test_code = "def test_placeholder():\n    assert True"
    return json.dumps({"tests": test_code})


def main():
    logger.info("🚀 Starting MCP Code Reviewer Server")
    mcp.run()


if __name__ == "__main__":
    main()

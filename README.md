[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/parthamehta123-mcp-code-reviewer-badge.png)](https://mseep.ai/app/parthamehta123-mcp-code-reviewer)


# 🤖 MCP Code Reviewer Demo

[![CI](https://github.com/parthamehta123/mcp-code-reviewer/actions/workflows/ci.yml/badge.svg)](https://github.com/parthamehta123/mcp-code-reviewer/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This project demonstrates **Model Context Protocol (MCP)** with an **AI-powered Code Reviewer**.

## Features
- `analyze_code`: Finds basic issues in Python code
- `suggest_refactor`: Suggests improvements (e.g., replace print with logging)
- `write_tests`: Auto-generates placeholder unit tests
- **Agentic Mode**: Automatically analyzes → refactors → re-analyzes code until clean

## Quick Start
```bash
pip install -r requirements.txt
python -m mcp_code_reviewer.mcp_server   # start server
python -m mcp_code_reviewer.mcp_client   # run demo client
```

## 🚀 Using Makefile
For convenience, a `Makefile` is provided:

```bash
make install       # install dependencies
make server        # run MCP server
make client        # run demo client
make client-agent  # run demo client in agentic loop mode
make test          # run tests
make clean         # remove caches and logs
```

## 📊 Demo Output

### Standard Demo (`make client`)
```
Available tools: ['analyze_code', 'suggest_refactor', 'write_tests']

🔍 Analysis:
{
  "issues": ["Consider using logging instead of print statements."],
  "line_count": 2
}

🛠 Refactor Suggestion:
{
  "original": "def foo():\n    print('Hello')",
  "refactored": "def foo():\n    logger.info('Hello')"
}

🧪 Generated Tests:
{
  "tests": "def test_placeholder():\n    assert True"
}
```

### 🤖 Agentic Mode Demo (`make client-agent`)
```
🔄 Iteration 1: Analyzing code...
Analysis: {
  "issues": ["Consider using logging instead of print statements."],
  "line_count": 2
}
⚠️ Issues found, applying refactor...

🔄 Iteration 2: Analyzing code...
Analysis: {
  "issues": [],
  "line_count": 2
}
✅ No issues found! Code is clean.

Final Code:
def foo():
    logger.info('Hello')
```

## Why This Project?
- Showcases **MCP server + client** implementation
- Demonstrates **GenAI-style tooling** (review, refactor, tests)
- Adds **Agentic AI loop** to show self-improving code refinement
- Strong example of MCP + GenAI + automation for recruiters

## Next Steps
- Integrate with real LLMs for deeper code analysis
- Expand test coverage & CI integration
- Record an **asciinema demo** and embed it here for a live showcase

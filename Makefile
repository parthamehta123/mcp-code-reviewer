# Makefile for MCP Code Reviewer

PYTHON := python3
PIP := pip

.PHONY: install server client test clean

install:
	$(PIP) install -r requirements.txt

server:
	$(PYTHON) -m mcp_code_reviewer.mcp_server

client:
	$(PYTHON) -m mcp_code_reviewer.mcp_client

client-agent:
	$(PYTHON) -m mcp_code_reviewer.mcp_client --agentic

test:
	pytest -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f mcp_server.log

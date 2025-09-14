import asyncio, os, sys, json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_demo():
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_code_reviewer.mcp_server"],
        env=dict(os.environ),
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = (await session.list_tools()).tools
            print("Available tools:", [t.name for t in tools])

            code_snippet = "def foo():\n    print('Hello')"

            # Standard demo (one-shot calls)
            await run_standard_demo(session, code_snippet)

async def run_standard_demo(session, code_snippet: str):
    # Analyze
    result = await session.call_tool("analyze_code", {"code": code_snippet})
    data = json.loads(result.content[0].text)
    print("\n🔍 Analysis:", json.dumps(data, indent=2))

    # Refactor
    suggestion = await session.call_tool("suggest_refactor", {"code": code_snippet})
    data = json.loads(suggestion.content[0].text)
    print("\n🛠 Refactor Suggestion:", json.dumps(data, indent=2))

    # Tests
    tests = await session.call_tool("write_tests", {"code": code_snippet})
    data = json.loads(tests.content[0].text)
    print("\n🧪 Generated Tests:", json.dumps(data, indent=2))


async def run_agentic_loop():
    """Agentic loop: analyze → refactor → re-analyze until no issues."""
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_code_reviewer.mcp_server"],
        env=dict(os.environ),
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            code_snippet = "def foo():\n    print('Hello')"
            iteration = 0
            while iteration < 3:  # limit iterations
                iteration += 1
                print(f"\n🔄 Iteration {iteration}: Analyzing code...")

                result = await session.call_tool("analyze_code", {"code": code_snippet})
                analysis = json.loads(result.content[0].text)
                print("Analysis:", json.dumps(analysis, indent=2))

                if not analysis["issues"]:
                    print("✅ No issues found! Code is clean.")
                    break

                print("⚠️ Issues found, applying refactor...")
                suggestion = await session.call_tool("suggest_refactor", {"code": code_snippet})
                refactored = json.loads(suggestion.content[0].text)["refactored"]
                code_snippet = refactored

            print("\nFinal Code:\n", code_snippet)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="MCP Client for Code Reviewer")
    parser.add_argument("--agentic", action="store_true", help="Run agentic loop instead of standard demo")
    args = parser.parse_args()

    if args.agentic:
        asyncio.run(run_agentic_loop())
    else:
        asyncio.run(run_demo())


if __name__ == "__main__":
    main()

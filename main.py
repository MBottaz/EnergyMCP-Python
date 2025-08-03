from mcp.server.fastmcp import FastMCP

mcp = FastMCP("EnergyMCP", log_level="ERROR")

@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


def main():
    """Entry point for the direct execution server."""
    mcp.run()


if __name__ == "__main__":
    main()
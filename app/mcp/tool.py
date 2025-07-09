

def tool(fn):
    """
    Decorator that tags a function as an MCP tool.
    
    """
    fn.is_mcp_tool = True
    return fn

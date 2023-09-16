from .config import load_config_schema
from .utils import ShellSpec


class LeanLanguageServer(ShellSpec):
    key = "lean-language-server"
    languages = ["lean", "plain"]
    cmd = "lake"
    args = [
        "serve"
    ]
    spec = dict(
        display_name="Lean 4 Language Server (from spec)",
        mime_types=["text/plain", "text/python", "text/x-python", "text/lean", "text/x-lean", "text/x-lean4"],
        urls=dict(
            home="https://github.com/leanprover/lean4/tree/master/src/Lean/Server",
            issues="https://github.com/leanprover/lean4/issues",
        ),
        config_schema=load_config_schema(key),
    )

"""mkdocs-macros: exposes catalog.yaml and workshops.yaml (copied here by factory/tools/build-catalog.py) to the pages."""
import pathlib, yaml
HERE = pathlib.Path(__file__).parent
PRODUCT_NAMES = {
    "agents-lowcode": "Agents (low-code)", "agents-coded": "Agents (coded)", "conversational-agents": "Conversational Agents",
    "evals": "Agent Evals", "uip-cli": "uip CLI & skills", "maestro-bpmn": "Maestro BPMN", "maestro-case": "Maestro Case",
    "maestro-flow": "Maestro Flow", "coded-apps": "Coded Apps", "action-center": "Action Center", "ixp": "IXP",
    "data-fabric": "Data Fabric", "integration-service": "Integration Service", "orchestrator": "Orchestrator", "rpa": "RPA",
    "api-workflows": "API Workflows", "functions": "Functions", "context-grounding": "Context Grounding", "cartographer": "Cartographer",
}
def define_env(env):
    cat = yaml.safe_load((HERE / "catalog.yaml").read_text()) if (HERE / "catalog.yaml").exists() else {"courses": []}
    ws = yaml.safe_load((HERE / "workshops.yaml").read_text()) if (HERE / "workshops.yaml").exists() else {"workshops": []}
    courses = [c for c in cat.get("courses", []) if c.get("status", "live") != "retired"]
    by_ref = {f"{e['course']}/{e['slug']}": e for c in courses for e in c.get("exercises", [])}
    products = sorted({p for c in courses for e in c.get("exercises", []) for p in e.get("products", [])})
    env.variables["courses"] = courses
    env.variables["workshops"] = ws.get("workshops", [])
    env.variables["exercise_by_ref"] = by_ref
    env.variables["products"] = products
    env.variables["product_name"] = lambda p: PRODUCT_NAMES.get(p, p)
    env.variables["generated"] = cat.get("generated", "")

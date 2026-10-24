import json, sys
from client import AutonomousContractSlaComplianceAuditorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "contract-sla-auditor", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "audit_contract_sla_compliance", "description": "Audits service availability logs against contract SLA tiers and calculates penalty credit memos."}]}}
    elif method == "tools/call":
        client = AutonomousContractSlaComplianceAuditorClient()
        res = client.audit_contract_sla_compliance()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AutonomousContractSlaComplianceAuditorClient()
        print(json.dumps(client.audit_contract_sla_compliance(), indent=2))

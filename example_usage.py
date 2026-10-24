import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AutonomousContractSlaComplianceAuditorClient

def main():
    client = AutonomousContractSlaComplianceAuditorClient()
    res = client.audit_contract_sla_compliance()
    print("=== Autonomous Contract SLA Compliance Auditor Output ===")
    print(f"Target SLA: {res['contract_sla_target']} | Actual: {res['actual_uptime_achieved']} ({res['audit_status']})")
    print(f"Outage: {res['actual_logged_outage_min']} mins (Allowed: {res['allowed_monthly_outage_min']} mins)")
    print(f"Credit Memo: ${res['reimbursable_credit_memo_usd']} ({res['applicable_credit_percentage']})")

if __name__ == '__main__':
    main()

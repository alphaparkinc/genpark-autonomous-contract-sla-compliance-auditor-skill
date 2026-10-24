import json
from typing import Dict, Any, List, Optional

class AutonomousContractSlaComplianceAuditorClient:
    """
    Production-grade B2B SaaS and cloud contract SLA compliance auditor.
    Evaluates logged downtime against contract availability tiers and computes financial credit memos.
    """
    def __init__(self):
        pass

    def audit_contract_sla_compliance(self, contract_sla_uptime_pct: float = 99.9, monthly_contract_value_usd: float = 12500.0, monthly_outage_minutes: int = 145) -> Dict[str, Any]:
        total_monthly_minutes = 43200  # 30 days * 24h * 60m
        actual_uptime_pct = round(((total_monthly_minutes - monthly_outage_minutes) / total_monthly_minutes) * 100, 3)

        allowed_outage_minutes = round(total_monthly_minutes * (1.0 - (contract_sla_uptime_pct / 100.0)), 1)
        breached = actual_uptime_pct < contract_sla_uptime_pct

        if breached:
            # Tiered credit percentage
            if actual_uptime_pct < 99.0: credit_pct = 0.25
            elif actual_uptime_pct < 99.5: credit_pct = 0.15
            else: credit_pct = 0.10
            credit_memo_amount = round(monthly_contract_value_usd * credit_pct, 2)
            audit_status = "SLA_BREACH_FINANCIAL_REMEDY_TRIGGERED"
        else:
            credit_pct = 0.0
            credit_memo_amount = 0.0
            audit_status = "SLA_COMPLIANT_TARGET_MET"

        return {
            "audit_id": "sla_aud_8819",
            "contract_sla_target": f"{contract_sla_uptime_pct}%",
            "actual_uptime_achieved": f"{actual_uptime_pct}%",
            "allowed_monthly_outage_min": allowed_outage_minutes,
            "actual_logged_outage_min": monthly_outage_minutes,
            "sla_breach_detected": breached,
            "audit_status": audit_status,
            "applicable_credit_percentage": f"{credit_pct*100:.0f}%",
            "reimbursable_credit_memo_usd": credit_memo_amount
        }

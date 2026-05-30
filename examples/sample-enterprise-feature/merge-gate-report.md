# Merge Gate Report - Approval Dashboard

## Operating principle

Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

## Owner

- Implementation owner: Frontend Team
- Supervisor: Frontend Lead
- Reviewer: Platform Team

## Change summary

- What changed: added Approval Dashboard UI and tests.
- Why: managers need a controlled approval workflow for discount requests.
- Scope: frontend UI only; backend API contract unchanged.

## Evidence

- Tests/evals đã chạy: component tests, contract mock tests, accessibility check.
- Contract không vỡ: API calls match `module-contract.md`.
- Integration/E2E result: pending list and approve/reject happy path covered.
- Screenshot diff nếu có UI: dashboard default/loading/empty/error approved.
- Accessibility/responsive result: keyboard focus and mobile stacked rows checked.
- Security/threat-model check: no frontend bypass of permission model.

## Reviewer approval

| Reviewer | Area | Decision | Notes |
|---|---|---|---|
| Sample Product Lead | Product/domain | Approved | Workflow matches spec |
| Sample Architect | Architecture | Approved | Boundary respected |
| Sample Design Lead | Design/UI | Approved | Uses design system |
| Frontend Lead | Engineering | Approved | Tests pass |

## Checklist pass/fail

- Pass vì evidence đầy đủ và reviewer đã duyệt.
- Fail nếu thiếu screenshot diff, contract test hoặc approval.

## Reviewer

- Final approver: Frontend Lead


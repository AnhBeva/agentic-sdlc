# Agent Task Brief - Approval Dashboard UI

## Operating principle

Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

## Owner

- Human supervisor: Frontend Lead
- Agent/tool: Codex
- Reviewer: Frontend Lead

## Input bắt buộc

- Feature spec: `feature-spec.md`
- ADR: `adr.md`
- UI contract: `ui-component-contract.md`
- Module contract: `module-contract.md`

## Output bắt buộc

- Allowed scope: approval dashboard UI files and related tests.
- Forbidden scope: backend permission logic, API schema changes, design token changes.
- Tests/evals: component tests, accessibility check, visual regression for dashboard states.
- Escalation: stop if API contract is insufficient or UI requires a new component pattern.

## Checklist pass/fail

- Pass khi implementation không tự quyết architecture, UI standard hoặc module contract.
- Fail khi agent sửa backend authorization hoặc hard-code style.

## Reviewer

- Supervisor: Frontend Lead
- Design reviewer: Sample Design Lead
- Domain reviewer: Sales Operations if workflow changes


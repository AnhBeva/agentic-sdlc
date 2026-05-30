# Quality Control Matrix Template

## Mục tiêu

Ánh xạ rủi ro sang nguồn sự thật, guardrail, checkpoint và pass/fail.

## Owner

- Engineering lead:
- Quality owner:
- Supervisor:

## Input bắt buộc

- Feature spec:
- Architecture/ADR:
- UI/module contracts:
- Agent plan:

## Output bắt buộc

| Khu vực | Nguồn sự thật | Guardrail tự động | Checkpoint con người | Pass/fail |
|---|---|---|---|---|
| UI/UX | Design tokens, component library | Token linter, screenshot diff, a11y | Designer/product |  |
| Architecture | Spec, ADR, threat model | Architecture tests, security scans | Architect/security/domain |  |
| Module lớn | Domain map, contracts, AGENTS.md | Contract, integration, E2E | Domain/module owner |  |
| Multi-agent | Ownership map, branch policy | CI per branch, trace/cost guard | Supervisor |  |
| Observability | Trace schema, eval taxonomy | Sampling, alert, regression | Ops/engineering |  |

## Checklist pass/fail

- Pass khi mỗi rủi ro có guardrail và checkpoint.
- Fail khi có rủi ro chỉ được mô tả bằng lời nhưng không có kiểm soát.

## Reviewer

- Engineering:
- Product/domain:
- Security/design nếu liên quan:


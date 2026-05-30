# Root AGENTS.md Template

## Mục tiêu

Định nghĩa nguyên tắc toàn cục để mọi agent làm việc trong repo không tự quyết kiến trúc, UI standard, contract hoặc scope.

## Operating Principle

Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

## Owner

- Engineering lead:
- Agent supervisor:
- Architecture owner:

## Input bắt buộc

- Repo architecture overview:
- Design system contract nếu có UI:
- Test/eval commands:
- Security/permission rules:
- Module ownership map:

## Output bắt buộc

- Global agent rules:
- Required artifacts before implementation:
- Quality gates:
- Forbidden actions:
- Escalation rules:

## Global Rules

- Do not decide architecture, storage, permission model, API boundary or event schema without approved spec/ADR.
- Do not create UI outside the design system without approved design/component contract.
- Do not modify files outside the assigned scope.
- Do not overlap with another agent's ownership area.
- Run the tests/evals/checks specified in the task brief.
- Stop and escalate if requirements, contracts, permissions or data ownership are ambiguous.

## Required Inputs Before Implementation

- Feature spec.
- ADR for architectural changes.
- UI contract for UI changes.
- Module contract for module boundary/API/data changes.
- Agent task brief.
- Expected tests/evals.

## Quality Gates

- Unit/integration/contract/E2E tests as applicable.
- Visual regression and accessibility checks for UI.
- Security checks for permission/data/tool changes.
- Merge gate report before merge.

## Forbidden Actions

- Broad refactor outside scope.
- Silent schema change.
- Hard-coded UI style outside tokens.
- Production-impacting action without human approval.
- Merge when gate fails.

## Checklist pass/fail

- Pass khi agent có đủ rule toàn cục để dừng, hỏi hoặc thực thi trong constraint.
- Fail khi agent vẫn phải tự đoán kiến trúc, UI standard, quyền, test command hoặc scope.

## Reviewer

- Engineering:
- Architecture:
- Security/design nếu liên quan:

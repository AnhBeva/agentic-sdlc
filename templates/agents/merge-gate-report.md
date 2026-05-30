# Merge Gate Report Template

## Mục tiêu

Cung cấp bằng chứng trước khi merge thay đổi do agent hoặc multi-agent tạo ra.

## Operating principle

Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

## Owner

- Implementation owner:
- Supervisor:
- Reviewer:

## Input bắt buộc

- Feature spec link:
- ADR link:
- UI contract link nếu có:
- Module contract link nếu có:
- Agent task brief:
- Ownership map nếu multi-agent:

## Output bắt buộc

### Change summary

- What changed:
- Why:
- Scope:

### Evidence

- Tests/evals đã chạy:
- Contract không vỡ:
- Integration/E2E result:
- Screenshot diff nếu có UI:
- Accessibility/responsive result nếu có UI:
- Security/threat-model check nếu có:
- Trace/cost/loop evidence nếu có:

### Reviewer approval

| Reviewer | Area | Decision | Notes |
|---|---|---|---|
|  | Product/domain |  |  |
|  | Architecture |  |  |
|  | Design/UI |  |  |
|  | Engineering |  |  |

## Checklist pass/fail

- Pass khi bằng chứng đầy đủ và reviewer liên quan đã duyệt.
- Fail khi thiếu test/eval, contract bị vỡ, screenshot diff chưa duyệt, ADR/spec thiếu link hoặc reviewer chưa approval.

## Reviewer

- Final approver:
- Required reviewers:


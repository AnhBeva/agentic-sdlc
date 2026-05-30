# Release Gate Template

## Mục tiêu

Chặn release nếu chất lượng, bảo mật, hợp đồng hoặc vận hành chưa đạt.

## Owner

- Release owner:
- Engineering lead:
- QA/quality owner:

## Input bắt buộc

- Merge gate report:
- Eval results:
- Test results:
- Risk review:
- Rollback plan:

## Output bắt buộc

- Release decision: approve / reject / canary only
- Known risks:
- Rollback plan:
- Monitoring plan:
- Owner on call:

## Checklist pass/fail

- [ ] Feature acceptance criteria đạt.
- [ ] Contract/integration/E2E tests đạt.
- [ ] UI/UX review đạt nếu có UI.
- [ ] Security/threat model đạt nếu có quyền/dữ liệu nhạy cảm.
- [ ] Observability và alert đủ cho production.
- [ ] Rollback/canary plan rõ.

## Reviewer

- Release:
- Engineering:
- Product/domain:
- Security/ops nếu liên quan:


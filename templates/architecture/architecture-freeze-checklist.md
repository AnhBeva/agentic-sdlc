# Architecture Freeze Checklist

## Mục tiêu

Khóa đủ quyết định kiến trúc trước khi agent build.

## Owner

- Architect:
- Engineering lead:

## Input bắt buộc

- Feature spec:
- ADR:
- Architecture review:
- Threat model:
- Module contract:

## Output bắt buộc

- Freeze decision: approved / rejected / needs revision
- Approved implementation boundaries:
- Required tests/evals:
- Rollback/migration path:

## Checklist pass/fail

- [ ] Spec đã duyệt.
- [ ] ADR đầy đủ context, decision, alternatives, consequences, rollback path.
- [ ] Module boundary và data ownership rõ.
- [ ] API/schema/event contract rõ nếu có.
- [ ] Threat model có mitigation.
- [ ] Test strategy đã định nghĩa.
- [ ] Agent task scope có thể viết mà không cần agent tự quyết kiến trúc.

## Reviewer

- Architect:
- Security:
- Domain:
- Engineering:


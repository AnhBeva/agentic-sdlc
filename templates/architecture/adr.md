# ADR Template

## Mục tiêu

Ghi lại quyết định kiến trúc quan trọng trước khi agent implement.

## Owner

- Architect:
- Engineering owner:
- Domain owner:

## Input bắt buộc

- Feature spec:
- Context hệ thống:
- Ràng buộc phi chức năng:
- Module/data/API liên quan:
- Rủi ro đã biết:

## Output bắt buộc

### Context

Vấn đề, giả định, ràng buộc và lý do cần quyết định.

### Decision

Quyết định được chọn và phạm vi áp dụng.

### Alternatives

Các phương án bị loại và lý do loại.

### Consequences

Tác động tới scale, cost, security, testability, operability và maintainability.

### Rollback path

Cách đảo quyết định, giảm thiểu thiệt hại hoặc migration path nếu giả định sai.

## Checklist pass/fail

- Pass khi decision, alternatives, consequences và rollback path rõ.
- Fail khi agent vẫn phải tự chọn storage, API boundary, event schema, permission model hoặc dependency direction.

## Reviewer

- Architect:
- Security:
- Domain:
- Engineering:


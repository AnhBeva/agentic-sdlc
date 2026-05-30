# Module Contract Template

## Mục tiêu

Khóa hợp đồng module để agent implement mà không làm đứt logic hệ thống lớn.

## Owner

- Module owner:
- Domain owner:
- Architect:

## Input bắt buộc

- Domain boundary:
- ADR nếu có:
- Data ownership:
- API/schema/event requirement:
- E2E business flow:

## Output bắt buộc

- Module responsibility:
- Public API:
- Events emitted:
- Events consumed:
- Data owned:
- Data read-only:
- Error model:
- Retry/idempotency rules:
- Security boundary:
- Contract tests:
- Integration/E2E tests:

## Checklist pass/fail

- Pass khi consumer có thể tích hợp qua contract mà không biết implementation nội bộ.
- Fail khi agent phải tự định nghĩa API, data owner, error flow hoặc permission.

## Reviewer

- Module owner:
- Consumer owner:
- Domain:
- Architect:


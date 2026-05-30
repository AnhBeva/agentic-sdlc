# ADR - Approval Dashboard Boundary

## Mục tiêu

Chốt boundary cho feature Approval Dashboard trước khi agent implement.

## Owner

- Architect: Sample Architect
- Engineering owner: Platform Team
- Domain owner: Sales Operations

## Context

Yêu cầu duyệt chiết khấu đang nằm trong Sales domain. Dashboard mới chỉ được đọc request và gửi quyết định approve/reject qua API đã kiểm quyền.

## Decision

Dashboard thuộc module `approval-ui`. Logic quyền và trạng thái request thuộc module `discount-approval`. UI không ghi trực tiếp dữ liệu request.

## Alternatives

- Đưa logic duyệt vào frontend: loại vì dễ bypass quyền.
- Cho UI ghi thẳng database: loại vì phá data ownership và audit.

## Consequences

- Frontend phụ thuộc API contract của `discount-approval`.
- Backend phải cung cấp error model rõ cho exceeded-limit, stale-request và forbidden.
- Audit trail nằm trong backend.

## Rollback path

Ẩn dashboard bằng feature flag và quay về flow duyệt cũ nếu contract/API có lỗi.

## Checklist pass/fail

- Pass vì data ownership, permission model và rollback path rõ.
- Fail nếu frontend tự quyết quyền hoặc ghi dữ liệu trực tiếp.

## Reviewer

- Architect: approved
- Security: approved with audit requirement
- Domain: approved


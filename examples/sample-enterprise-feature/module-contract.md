# Module Contract - discount-approval

## Mục tiêu

Định nghĩa contract giữa Approval Dashboard và module duyệt chiết khấu.

## Owner

- Module owner: Sales Platform
- Domain owner: Sales Operations
- Architect: Sample Architect

## Output bắt buộc

- Module responsibility: kiểm quyền, trạng thái request, approve/reject, audit.
- Public API:
  - `GET /approval-requests?status=pending`
  - `GET /approval-requests/{id}`
  - `POST /approval-requests/{id}/approve`
  - `POST /approval-requests/{id}/reject`
- Data owned: approval request, approval decision, audit event.
- Error model: forbidden, exceeded_limit, stale_request, validation_error.
- Security boundary: manager role + approval limit.
- Contract tests: request visibility, approve success, reject success, exceeded limit, stale request.

## Checklist pass/fail

- Pass khi UI chỉ dùng API contract và không ghi data trực tiếp.
- Fail khi data ownership hoặc error model bị thay đổi mà không cập nhật ADR/contract.

## Reviewer

- Module owner: Sales Platform
- Consumer owner: Frontend Team
- Domain: Sales Operations


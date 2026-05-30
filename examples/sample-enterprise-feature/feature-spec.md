# Sample Feature Spec - Approval Dashboard

## Mục tiêu

Cho phép quản lý duyệt yêu cầu chiết khấu trong một dashboard thống nhất, giảm thời gian xử lý và tránh duyệt sai quyền.

## Owner

- Product owner: Sample Product Lead
- Domain owner: Sales Operations
- Engineering owner: Platform Team

## Input bắt buộc

- Người dùng: sales manager.
- Business outcome: giảm thời gian duyệt yêu cầu chiết khấu.
- Ràng buộc: không cho phép duyệt nếu vượt hạn mức quyền.

## Output bắt buộc

- Danh sách yêu cầu chờ duyệt.
- Chi tiết yêu cầu.
- Hành động approve/reject với lý do.
- Audit trail cho mọi hành động.

## Acceptance criteria

- [ ] Manager chỉ thấy yêu cầu trong phạm vi quyền.
- [ ] Yêu cầu vượt hạn mức bị chặn và hiển thị lý do.
- [ ] Approve/reject ghi audit trail.
- [ ] UI có loading, empty, error, disabled states.

## Checklist pass/fail

- Pass khi workflow nghiệp vụ, UI, quyền và audit đều rõ.
- Fail nếu agent phải tự quyết permission model hoặc UI pattern.

## Reviewer

- Product: Sample Product Lead
- Domain: Sales Operations
- Engineering: Platform Team


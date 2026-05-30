# UI Component Contract - Approval Request Table

## Mục tiêu

Đảm bảo dashboard dùng đúng design system và đủ state.

## Owner

- Designer: Sample Design Lead
- Frontend owner: Frontend Team

## Output bắt buộc

- Component name: `ApprovalRequestTable`
- Purpose: hiển thị danh sách request chờ duyệt.
- States: default, loading, empty, error, row-selected, action-disabled.
- Token usage: dùng token spacing, typography, color semantic status.
- Responsive behavior: desktop table, mobile stacked rows.
- Accessibility: keyboard navigation, visible focus, status text không chỉ dựa vào màu.

## Checklist pass/fail

- Pass khi đủ states, không hard-code style và screenshot diff được duyệt.
- Fail khi text tràn, thiếu empty/error state hoặc tạo button style mới.

## Reviewer

- Design: Sample Design Lead
- Frontend: Frontend Team
- Product: Sample Product Lead


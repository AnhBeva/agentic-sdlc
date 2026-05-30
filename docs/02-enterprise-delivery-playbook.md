# Enterprise Delivery Playbook

Playbook này áp dụng khi dự án có phần mềm lớn, nhiều nghiệp vụ, nhiều nhóm hoặc nhiều agent cùng tham gia.

> [!TIP]
> Để trực quan hóa các cổng chất lượng và sơ đồ giao hàng doanh nghiệp, xem [Bản đồ Cổng Kiểm soát Chất lượng Doanh nghiệp (Sơ đồ 6)](../Agentic_SDLC_Master_Map.md#6-bản-đồ-cổng-kiểm-soát-chất-lượng-doanh-nghiệp-enterprise-quality-control-gates-map) và [Sơ đồ Trình tự Phát triển Tính năng (Sơ đồ 2)](../Agentic_SDLC_Master_Map.md#2-sơ-đồ-trình-tự-phát-triển-tính-năng-feature-development-sequence-diagram).

## Nguyên tắc vận hành

> Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

Agent không tự quyết:

- kiến trúc nền tảng;
- chuẩn UI/UX mới;
- ranh giới module;
- schema/event contract;
- quyền truy cập production;
- merge khi gate chưa đạt.

## Quy trình delivery

1. Product owner viết feature spec và acceptance criteria.
2. Architect duyệt kiến trúc, ADR và rollback path.
3. Designer/domain owner duyệt UI contract hoặc module contract.
4. Supervisor chia task, ownership map và phạm vi cho từng agent.
5. Agent implement trong branch/worktree riêng.
6. CI/manual gate kiểm test, eval, contract, UI screenshot và security.
7. Human reviewer duyệt merge gate report.
8. Production trace được lấy mẫu để bổ sung regression/eval.

## Cách chia mức rủi ro

| Mức | Ví dụ | Gate |
|---|---|---|
| Thấp | copy text, test nhỏ, refactor local | Agent tự làm + CI |
| Trung bình | UI thay đổi, API nhỏ, module nội bộ | Reviewer + checklist |
| Cao | kiến trúc, schema, permission, data migration | ADR + architecture freeze + human approval |
| Không hoàn tác | xóa dữ liệu, gửi tiền, thay production policy | Human approval bắt buộc trước hành động |


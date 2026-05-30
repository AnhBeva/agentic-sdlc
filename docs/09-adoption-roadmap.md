# Adoption Roadmap

Không nên triển khai toàn bộ Agentic SDLC cùng lúc. Bắt đầu từ observability, eval và template trước khi mở rộng multi-agent.

## Giai đoạn 1 - Chuẩn hóa tài liệu

- Dùng feature spec, ADR, module contract và merge gate report.
- Tạo root `AGENTS.md` cho repo sản phẩm.
- Bắt đầu checklist UI/UX, architecture và release.

## Giai đoạn 2 - Quality gates

- Thêm contract tests.
- Thêm visual regression cho màn hình trọng yếu.
- Thêm eval plan cho agent output.
- Yêu cầu merge gate report cho PR do agent tạo.

## Giai đoạn 3 - Multi-agent có kiểm soát

- Chạy supervisor + 2-3 sub-agent trên worktree riêng.
- Dùng ownership map.
- Chỉ fan-out task khi spec/contract đã rõ.

## Giai đoạn 4 - 24/7 và cải thiện liên tục

- Trace mọi run.
- Sampling production.
- Tạo regression từ lỗi thật.
- Cập nhật template và `AGENTS.md` theo bài học.


# Agentic SDLC Operating System

Repo này biến `Agentic_SDLC_Deep_Dive.md` thành bộ tài liệu và mẫu triển khai Agentic SDLC cho phần mềm lớn, nhiều nghiệp vụ, có UI/UX phức tạp và nhiều AI agent cùng tham gia.

Nguyên lý điều hành:

> Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

## Dùng repo này như thế nào

1. Xem [Bản đồ Quy trình trực quan](Agentic_SDLC_Master_Map.md) để có cái nhìn toàn cảnh bằng sơ đồ luồng.
2. Đọc [overview](docs/00-overview.md) để hiểu cấu trúc bộ tài liệu.
3. Chọn playbook theo vấn đề cần giải quyết:
   - [Agentic SDLC lifecycle](docs/01-agentic-sdlc-lifecycle.md)
   - [Enterprise delivery playbook](docs/02-enterprise-delivery-playbook.md)
   - [Quality control matrix](docs/03-quality-control-matrix.md)
   - [UI/UX control system](docs/04-ui-ux-control-system.md)
   - [Architecture governance](docs/05-architecture-governance.md)
   - [Large module delivery](docs/06-large-module-delivery.md)
   - [Multi-agent orchestration](docs/07-multi-agent-orchestration.md)
   - [Observability, evals, governance](docs/08-observability-evals-governance.md)
   - [Adoption roadmap](docs/09-adoption-roadmap.md)
4. Copy template phù hợp từ `templates/` vào repo sản phẩm thật.
5. Dùng checklist trong `checklists/` trước khi merge hoặc release.
6. Xem ví dụ hoàn chỉnh trong `examples/sample-enterprise-feature/`.

## Artifact chính

- [Agentic_SDLC_Master_Map.md](Agentic_SDLC_Master_Map.md): Bản đồ quy trình trực quan hóa bằng 6 sơ đồ Mermaid chi tiết.
- [Agentic_SDLC_Deep_Dive.md](Agentic_SDLC_Deep_Dive.md): tài liệu nền tảng và giải thích sâu.
- `docs/`: playbook vận hành ngắn theo từng chủ đề.
- `templates/`: mẫu spec, ADR, UI contract, module contract, AGENTS.md, eval plan, merge gate.
- `examples/`: một feature mẫu đi từ spec đến merge gate.
- `checklists/`: checklist độc lập cho review và release.

## Khi nào cần dùng template nào

| Nhu cầu | Template nên dùng |
|---|---|
| Bắt đầu feature mới | `templates/specs/feature-spec.md` |
| Chốt kiến trúc trước khi agent code | `templates/architecture/adr.md`, `templates/architecture/architecture-freeze-checklist.md` |
| Làm UI/UX nhất quán | `templates/ui-ux/design-system-contract.md`, `templates/ui-ux/component-contract.md` |
| Chia module lớn | `templates/modules/domain-boundary.md`, `templates/modules/module-contract.md` |
| Chạy nhiều agent song song | `templates/agents/agent-task-brief.md`, `templates/agents/multi-agent-ownership-map.md` |
| Chuẩn bị merge/release | `templates/agents/merge-gate-report.md`, `templates/quality/release-gate.md` |


# Quality Control Matrix

Mỗi rủi ro lớn phải có nguồn sự thật, guardrail tự động, checkpoint con người và tiêu chí pass/fail.

> [!TIP]
> Bản đồ trực quan của các cổng chất lượng được mô tả chi tiết tại [Bản đồ Cổng Kiểm soát Chất lượng Doanh nghiệp (Sơ đồ 6)](../Agentic_SDLC_Master_Map.md#6-bản-đồ-cổng-kiểm-soát-chất-lượng-doanh-nghiệp-enterprise-quality-control-gates-map).

| Khu vực | Nguồn sự thật | Guardrail tự động | Checkpoint | Pass/fail |
|---|---|---|---|---|
| UI/UX | Design tokens, component library, UX guidelines | Token linter, component-only rule, screenshot diff, accessibility | Designer/product review | Không hard-code style, không lệch baseline ngoài ngưỡng, đủ states |
| Architecture | Spec, ADR, principles, threat model | Dependency rules, architecture tests, security scans | Architect + security + domain lead | ADR duyệt, boundary rõ, rollback path có |
| Module lớn | Domain map, contracts, data ownership, AGENTS.md | Contract tests, integration tests, E2E flows | Domain owner | Không phá contract, E2E nghiệp vụ đạt |
| Multi-agent | Ownership map, branch/worktree policy, merge protocol | CI per branch, trace/cost/loop guard | Supervisor/human lead | Không sửa chồng lấn, không merge khi gate fail |
| Observability | Trace schema, eval taxonomy, alert policy | Sampling, regression suite, cost/latency alerts | Ops/engineering lead | Có trace đầy đủ và failure feedback loop |

## Cách dùng

- Điền matrix ở đầu mỗi initiative lớn.
- Mỗi hàng phải có ít nhất một guardrail máy kiểm được.
- Nếu chưa có checkpoint owner, không giao task cho agent.
- Nếu pass/fail không rõ, chưa đủ điều kiện chạy song song multi-agent.


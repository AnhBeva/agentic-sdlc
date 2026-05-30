# Production Readiness Checklist Template

## Mục tiêu

Đảm bảo hệ thống sẵn sàng vận hành sau merge/release.

## Owner

- Engineering lead:
- Ops/SRE owner:
- Product owner:

## Input bắt buộc

- Release gate:
- Monitoring plan:
- Eval plan:
- Rollback plan:

## Output bắt buộc

- Readiness decision:
- Outstanding risks:
- Monitoring dashboard/trace links:
- Post-release review date:

## Checklist pass/fail

- [ ] Trace ghi đủ agent/tool/action.
- [ ] Dashboard có quality, cost, reliability.
- [ ] Alert có owner và escalation path.
- [ ] Sampling production được bật nếu cần.
- [ ] Rollback/circuit breaker có.
- [ ] Failure feedback loop được định nghĩa.

## Reviewer

- Engineering:
- Ops/SRE:
- Product/domain:


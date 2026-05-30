# Architecture Governance

Kiến trúc là cổng chất lượng trước khi agent implement, không phải kết quả ngẫu nhiên trong lúc coding.

## Architecture Freeze Before Agent Build

Trước khi giao task cho agent, phải có:

- feature spec đã duyệt;
- ADR cho quyết định khó đảo;
- module boundary và data ownership rõ;
- threat model cho vùng rủi ro;
- rollback path hoặc migration path;
- test strategy.

## Review đa vai

| Vai | Câu hỏi chính |
|---|---|
| Architect | Boundary có rõ không, dependency có đúng chiều không? |
| Security | Quyền, dữ liệu nhạy cảm, audit trail đã đủ chưa? |
| Scalability | Bottleneck, state, queue, cache, throughput ra sao? |
| Maintainability | Testability, versioning, migration, cognitive load thế nào? |
| Cost | Hạ tầng, token/tool call, vận hành 24/7 có kiểm soát không? |
| Domain expert | Logic nghiệp vụ và exception flow có đúng không? |

## Không giao cho agent khi

- API/schema/event chưa chốt.
- Data owner còn mơ hồ.
- Permission model chưa được duyệt.
- ADR thiếu alternatives hoặc consequences.
- Reviewer chưa đồng ý rollback path.


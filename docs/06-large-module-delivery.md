# Large Module Delivery

Hệ thống lớn phải được chia theo domain capability và interface contract, không chia tùy tiện theo màn hình hoặc file.

## Bounded context

Mỗi bounded context cần có:

- năng lực nghiệp vụ sở hữu;
- thuật ngữ chính;
- data ownership;
- inbound/outbound API;
- event phát ra và event tiêu thụ;
- error model;
- test contract.

## Contract trước implementation

Agent chỉ được implement khi module contract đã rõ:

- input/output;
- versioning;
- backward compatibility;
- idempotency/retry;
- quyền truy cập;
- E2E flow liên quan.

## AGENTS.md phân tầng

- Root `AGENTS.md`: nguyên tắc toàn cục, test command, security, coding rules.
- Module `AGENTS.md`: boundary, domain terms, allowed dependencies, forbidden dependencies.
- Package `AGENTS.md`: local conventions, known pitfalls, test command.

## Gate

- Contract tests ở biên module.
- Integration tests giữa module.
- E2E tests theo kịch bản nghiệp vụ thật.
- Regression mới cho mỗi bug production.


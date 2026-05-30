# Threat Model Template

## Mục tiêu

Xác định rủi ro bảo mật, quyền hạn và dữ liệu trước khi agent thực thi.

## Owner

- Security owner:
- Engineering owner:

## Input bắt buộc

- Feature spec:
- Architecture/ADR:
- Data classification:
- Tool/API permissions:
- External integrations:

## Output bắt buộc

| Threat | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| Prompt injection |  |  |  |  |
| Tool misuse |  |  |  |  |
| Excessive privilege |  |  |  |  |
| Data exposure |  |  |  |  |
| Unsafe output handling |  |  |  |  |

## Checklist pass/fail

- Pass khi mỗi rủi ro cao có guardrail/eval/alert hoặc HITL.
- Fail khi agent được cấp quyền rộng, credentials không scoped hoặc hành động không hoàn tác thiếu approval.

## Reviewer

- Security:
- Engineering:
- Compliance/domain:


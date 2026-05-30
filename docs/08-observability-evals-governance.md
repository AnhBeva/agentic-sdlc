# Observability, Evals, Governance

Agentic SDLC cần quan sát được, đánh giá được và có kiểm soát quyền hạn.

## Observability

Theo dõi tối thiểu:

- trace từng run;
- tool calls;
- số bước/loop;
- token/cost;
- latency;
- failure mode;
- human escalation.

## Evals

Ba lớp đánh giá:

- Unit evals: định dạng, tool call, schema, ground truth.
- Regression suite: LLM-as-judge hoặc rubric review cho chất lượng chủ quan.
- Production sampling: lấy mẫu trace thật để bắt drift.

## Governance

- Least privilege cho agent.
- Scoped credentials.
- Guardrails đầu vào và đầu ra.
- HITL cho hành động không hoàn tác.
- Audit trail cho hành động quan trọng.

## Feedback loop

Mỗi lỗi production phải tạo một artifact mới: test, eval, guardrail, checklist item hoặc cập nhật `AGENTS.md`.


# Multi-Agent Ownership Map Template

## Mục tiêu

Tránh xung đột khi nhiều agent làm song song.

## Operating principle

Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

## Owner

- Supervisor:
- Engineering lead:

## Input bắt buộc

- Approved spec:
- ADR/contracts:
- Task list:
- Repo/module map:

## Output bắt buộc

| Agent | Branch/worktree | Scope được phép | Scope cấm sửa | Contract liên quan | Required gates | Reviewer |
|---|---|---|---|---|---|---|
| Agent A |  |  |  |  |  |  |
| Agent B |  |  |  |  |  |  |

## Checklist pass/fail

- Pass khi không có scope chồng lấn và mỗi agent có branch/worktree riêng.
- Fail khi nhiều agent cùng sửa boundary chưa chốt hoặc không có merge order.

## Reviewer

- Supervisor:
- Architect nếu chạm boundary:
- Domain/design nếu liên quan:


# Module AGENTS.md Template

## Mục tiêu

Định nghĩa ngữ cảnh local cho agent khi làm việc trong một module cụ thể.

## Owner

- Module owner:
- Domain owner:
- Engineering owner:

## Input bắt buộc

- Domain boundary:
- Module contract:
- Data ownership:
- Dependency rules:
- Test commands:

## Output bắt buộc

- Module context:
- Domain boundary:
- Contracts:
- Allowed/forbidden dependencies:
- Commands:
- Known pitfalls:
- Agent rules:

## Module Context

- Module name:
- Domain capability:
- Module owner:
- Domain owner:

## Domain Boundary

- In scope:
- Out of scope:
- Key business terms:
- Business invariants:

## Contracts

- Public APIs:
- Events emitted:
- Events consumed:
- Data owned:
- Data read-only:
- Error model:

## Dependencies

- Allowed dependencies:
- Forbidden dependencies:
- Dependency direction rules:

## Commands

- Local test command:
- Contract test command:
- E2E/eval command:
- Lint/typecheck command:

## Known Pitfalls

- Pitfall 1:
- Pitfall 2:
- Pitfall 3:

## Agent Rules

- Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.
- Do not change module boundary without ADR/reviewer approval.
- Do not write data owned by another module.
- Do not introduce new dependency direction without architecture approval.
- Escalate if business terminology or error behavior is unclear.

## Checklist pass/fail

- Pass khi agent hiểu rõ module này sở hữu gì, không sở hữu gì, được phụ thuộc vào đâu và phải chạy test nào.
- Fail khi boundary, dependency, data ownership hoặc command còn mơ hồ.

## Reviewer

- Module owner:
- Domain owner:
- Architecture/engineering:

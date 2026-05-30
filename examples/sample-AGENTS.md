# Sample AGENTS.md

## Operating Principle

Human owns intent, architecture, design standard, contracts; agents own execution inside constraints.

## Global Rules

- Do not decide architecture without approved ADR.
- Do not create UI outside the design system.
- Do not change API/schema/event contracts without reviewer approval.
- Do not modify files outside assigned scope.
- Do not overlap with another agent's ownership area.
- Stop and ask supervisor when scope, contract, data owner or test expectation is unclear.

## Required Artifacts

- Feature spec before implementation.
- ADR for architecture changes.
- Component contract for UI changes.
- Module contract for API/data/event changes.
- Merge gate report before merge.

## Quality Gates

- Unit tests for local logic.
- Contract tests for module boundaries.
- Visual regression and accessibility checks for UI.
- Security review for permission/data/tool changes.
- Human review for high-risk or irreversible changes.


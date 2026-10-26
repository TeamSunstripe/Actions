# Actions minutes measurement plan

## Baseline
Record the period, timezone, private repository, workflow name, run ID, event, conclusion, job duration, and billed minutes using GitHub Billing usage export and Actions metadata. Do not publish private URLs, private PR data, job logs, credentials, or code to this public repository.

## Comparison
Compare equally sized before/after periods and normalize for PR volume. Track:
- private billable Actions minutes (primary)
- count of launched jobs, cancelled/skipped jobs and failures
- public CI executions and confirmed validation outcomes
- any changes to workflows or billing policies

A lower private job count or higher public job count alone does not prove a decrease in private billable minutes. Costs, discounts and public runner conditions must be independently verified. Store private detailed evidence in a PRIVATE report only.

## Gates
Do not disable private security-critical Guard jobs until equivalent safety controls are demonstrated. Non-sensitive public tests may replace only tests which genuinely have no private dependencies.

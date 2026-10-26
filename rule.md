# Public CI Rules

## Purpose and boundaries
This public repository tests public, synthetic inputs only. It is not a proxy to run or inspect private repository code, jobs, or secrets.

## Forbidden content
- Personal information, passwords, API keys, tokens, private keys, credentials, production logs, non-public source, real database or server connection details.
- Private checkout, private files, private workflow artifacts, caches, internal PR payloads or credentials.
- Hidden secret values in screenshots, comments, test fixtures, generated files, documentation or commit messages.

Use invented sample data and public example domains. If disclosure is uncertain, do not publish it. Scan staged diffs and new files before commits. Never print discovered secret values.

## CI least privilege
- Use standard GitHub-hosted ubuntu-latest; default permissions: contents: read.
- Explicit job timeouts; no write token, no private checkout or production deployment.
- Do not combine untrusted PR code with pull_request_target or privileged credentials.
- Review all third-party actions; prefer pinning by full commit SHA.
- All public tests must be standalone, with no private network/API/data dependencies.
- A reusable workflow called by a private repository is subject to private caller billing; it is not a free workaround.
- Public mocks do NOT verify private production Guard correctness.

## Branch and PR flow
1. master: stable public release.
2. develop: integration.
3. feature/<topic>: branch from develop; propose Draft PR targeting develop.
4. Human review, public-safety review and successful CI at exact head SHA required before merge.
5. Squash merge feature PR to develop; use a reviewed release PR for master.
6. Do not force push, bypass protection, delete audit evidence, or merge without review.

## Mandatory publication review
- Read full changed files, diff, and changes to workflow privileges/triggers.
- Check for data leakage, exfiltration, injection, token permission escalation and risky dependencies.
- Confirm test evidence for current head SHA and human sign-off.
- Check that public PRs cannot access private data.
- Do not automatically merge drafts or failing/pending checks.

## Incident response
If a secret or private data may have been published: stop affected workflow, revoke/rotate credentials in private channels, assess exposure and history, then perform GitHub's documented remediation. Deleting the latest file is not sufficient to erase Git history. Do not repeat leaked values in reports.

## Cost and scope
Standard runners on public repositories are normally free; larger runners, storage and other products can be billable. Validate actual billing independently. Private workflows keep their own billing and permissions.

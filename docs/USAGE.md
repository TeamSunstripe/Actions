# Public CI Usage Guide

## What is validated
- Public workflow YAML syntax (not complete GitHub Actions semantics).
- Standalone synthetic Guard event classification (not production Guard code).
- Standalone PHP and JavaScript example functions and assertions (not private application source).

## Running locally
```sh
ruby -e 'require "yaml"; Dir[".github/workflows/*.{yml,yaml}"].each { |f| YAML.parse_file(f) }'
python3 -m unittest discover -s tests -p 'test_*.py' -v
php -l examples/php/Calculator.php
php tests/php/test_calculator.php
node --check examples/js/validation.cjs
node --check tests/js/test_validation.cjs
node tests/js/test_validation.cjs
```

## Running on GitHub
Create a feature branch from develop and open a PR to develop. The public CI validates the public repository changes with a read-only token. An authorized maintainer may also use workflow_dispatch. Avoid including confidential inputs in public issues, PRs, actions, logs, test artifacts or commits.

## Publishing new test data
Test inputs must be entirely synthetic. No checkout of private repositories, no private credentials, no copy of private logs or configurations. Approval of any shared source must occur before it enters a public branch.

## Required evidence
Review the Actions run for the exact PR head SHA; confirm each job reports success and inspect unexpected output. A green synthetic mock is not proof the private production Guard works.

## Cost verification
Review organization Billing -> Actions usage per repository / runner / day. Compare before and after changes, using measured billable minutes rather than estimating from the number of workflow runs. Public CI success does not demonstrate private-minute savings.

# TeamSunstripe Actions

Public CI sandbox for non-sensitive, synthetic verification. Never commit personal information, passwords, tokens, private source code, server configuration, or private CI logs.

## Branch flow
master -> develop -> feature/public-ci-foundation (review changes before merging).

## Phase 1
- YAML syntax parsing using Ruby YAML parser.
- Standalone synthetic Guard mock tests using Python unittest.
- Public GitHub-hosted ubuntu-latest with read-only permissions and no secrets.

**Limitation:** The sample scripts/guard_mock.py is not the private production Guard. Passing tests here does not establish correctness of the private Guard or private pull request checks.

## Security
Only publish synthetic examples and public-safe inputs. Do not check out the private repository or print any secret in Actions logs. Review all changes before merging.

## Local checks
```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
ruby -e 'require "yaml"; Dir[".github/workflows/*.{yml,yaml}"].each { |f| YAML.parse_file(f) }'
```

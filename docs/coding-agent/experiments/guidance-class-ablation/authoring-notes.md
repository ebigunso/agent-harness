# Pilot authoring record — Task_5 part A

Only the seven pilot sections were authored: 112 fixtures (84 planted, 28 clean), seven keys, and fourteen arms. No model calls, grading or scoring occurred. Source guidance, protocol.md, manifest.yaml, fixture-plan.md and score.py were not edited. The Orchestrator owns review, Git and the subsequent experiment run.

## Authority and evidence scope

The Orchestrator's 2026-09-07 rulings permit explicitly synthetic environment-dependent transcripts, treat reproduction notes as quality guidance, and permit minimal verified corrections to authoring errors while retaining each ID, language and primary check. The fixed protocol, manifest and decision rule remain unchanged. Package layouts are plausible version-specific scenarios, not claims of packages installed on this machine. Each applicable gRPC fixture states its project probe's normalized output contract separately from native client-library formatting.

Actual authoring runtimes: Windows version 10.0.26200.0; PowerShell 7.4.19; Windows PowerShell 5.1.26100.9168; CPython 3.12.10; Node 24.19.0; npm 11.17.0. Fixture profile versions are synthetic reproduction profiles, not these observed versions. A Docker read-only connection check was denied; no Docker hang reproduction is claimed or required under the ruling. No native-addon processes were stopped.

## Corrections to specification rows

| IDs | Correction and evidence |
|---|---|
| rb-windows-npm-eperm-locks-01 through -12; c1 through c3 | Modern npm error prefix replaces npm ERR!. Installed npm ci EUSAGE output and npm error-message.js/commands/ci.js confirmed formatting and lockfile/auth/permission wording. |
| rb-windows-python-console-encoding-03, -05, -07, -09 | CP1252 output exceptions name the codec charmap; sys.stdout.encoding remains cp1252. All twelve planted exception characters, positions and messages were generated using CPython codecs. |
| rb-powershell-json-array-cardinality-05, -09 | Windows PowerShell 5.1 preserves direct ConvertFrom-Json arrays; append Write-Output to exhibit downstream unrolling. Original controls and corrected failures were run. Row 09 prints raw whitespace between explicit angle-bracket markers. |
| rb-powershell-json-array-cardinality-06 | Direct no-enumeration cmdlet output through the function stayed an array. Assign to local $items, then emit $items to cause post-parse enumeration. Original control and corrected failure were run on pwsh. |
| rb-windows-docker-grpc-localhost-ipv6-03 | go run reports command exit 1 and appends exit status 2 when the probe exits 2; follows the Go launcher source. |
| rb-windows-docker-grpc-localhost-ipv6-07 | The exact command uses enabled server reflection, with no unmentioned descriptor flag. Dial deadline uses grpcurl's native failed-dial wording and exit 1; success is JSON containing value pong. |
| All sixteen gRPC HTTP comparisons | curl explicitly uses --silent, --show-error and --write-out; body, HTTP code and timing fields are distinct. No fictional timing wrapper or suppressed progress-meter default is implied. Timing values are synthetic. |
| rb-persistent-shell-cwd-normalization-02, -c2 | Quoted missing-script filename uses Python repr-style escaped Windows backslashes. Verified by an actual missing-script invocation (exit 2, stdout empty); Git missing-repo/ref messages were also checked locally. |
| rb-persistent-shell-cwd-normalization-12 | PHP 8.3.14 missing-input error is on stderr, contrary to the plan's general PHP stdout note; verified against the pinned PHP CLI source. |
| rb-persistent-shell-cwd-normalization-c1 | tsc compiler diagnostic is on stdout, not stderr. Correct cwd/config/source are present. |
| CWD decoy diagnostic listings | Selected paths use explicit Get-Item lookups rather than pretending nonrecursive Get-ChildItem output includes descendant files. |

Sources for nonlocal tool formatting: [Go run command](https://go.dev/src/cmd/go/internal/run/run.go), [Go launcher/error handling](https://go.dev/src/cmd/go/internal/base/base.go), [grpcurl 1.9.1](https://raw.githubusercontent.com/fullstorydev/grpcurl/v1.9.1/cmd/grpcurl/grpcurl.go), [PHP 8.3.14 CLI](https://raw.githubusercontent.com/php/php-src/php-8.3.14/sapi/cli/php_cli.c), [Bundler 2.5.23 error codes](https://raw.githubusercontent.com/rubygems/rubygems/bundler-v2.5.23/bundler/lib/bundler/errors.rb), [Bundler root lookup](https://raw.githubusercontent.com/rubygems/rubygems/bundler-v2.5.23/bundler/lib/bundler.rb). Bundler's GemfileNotFound code 10 and missing-root message were checked in that version's source; no Bundler runtime run is claimed.

## Verification

- From repo root, run: python docs/coding-agent/experiments/guidance-class-ablation/validate_pilot.py. This checks all manifest IDs/frontmatter, per-section 12/4 counts, keys/arms, byte-identical B source copies, C <= B/3 even after LF normalization, all 32 unified diffs via git apply --numstat, and fixture/key/arm whitespace.
- All sixteen JSON scripts ran on installed pwsh/Windows PowerShell and produced expected failed-command diagnostics. The HTTP row used a disposable Node server on an allocated local port; fixture port 5080 is synthetic. Only the temporary script process received execution-policy permission; no user/machine policy changed. The initial legacy probe was rejected by local execution policy and then rerun successfully with that process setting.
- cp-2-c1 after-diff Python passed LF/CRLF/empty/trailing-record/standalone-CR checks. cp-2-c3 actual TypeScript ran on Node and passed slash/no-slash cases through both callers. cp-9-c2 after-diff Python passed fresh-success, bounded-age, expired/future-cache and cache-miss cases, including a source failure that advances time.
- All 28 decoys were reread as hostile reviews against their section's defect and stated contracts. Self-review moved cp-9-c2's age sample after the failed read and used a zero-based bounded counter in cp-2-c2. Optional-thumbnail warnings, typed timeout propagation and permanent/final retry errors remain observable; no blocking defect was found within these contracts.
- git diff --check passed from the worktree root. Tracked diff was empty; artifacts are new. This Worker performed no commit, staging or branch mutation.
- C text is finalized before any experiment cell. Independent review and experimental grading remain Orchestrator-owned; this is author verification, not independent approval.

Quality routing: targeted fixture/diagnostic checks under engineering-quality-baselines core principles and testing-validation. Architecture, UI/E2E and package validators are out of scope: this part changes only temporary experiment artifacts and no runtime/package contracts. Residual limit: runtime checks cover installed versions and explicit synthetic scenarios, not full installation of every pinned client stack.

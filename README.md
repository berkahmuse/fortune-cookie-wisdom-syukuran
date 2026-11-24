# Fortune Cookie Wisdom for Developers — @syukuran entry

[![Fortune Cookie Wisdom for Developers](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/berkahmuse/fortune-cookie-wisdom-syukuran/rank.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/berkahmuse/fortune-cookie-wisdom-syukuran/reward.svg)](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for the [Fortune Cookie Wisdom for Developers](https://make.fun/competitions/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
bounty on [make.fun](https://make.fun): one original fortune-cookie line
for a software developer, at most 120 characters.

## The line

> The bug you cannot reproduce is patient; it is waiting for the demo.

68 characters. The truth every senior engineer knows: the bug you
cannot reproduce is never really gone. The turn is the second half —
it is not hiding, it is *waiting*, and it waits for the demo, the one
moment when the room is watching and the stakes are highest. "Patient"
carries a quiet double meaning: the bug waits calmly while the
engineer is the impatient one, re-running the same steps and getting
nothing. It reads like a real fortune cookie: one short balanced
sentence that lands in a single breath, and a prediction about the
reader's near future rather than advice or a punchline.

## Why it beats the sibling entries

- @berkahmuse-2 (legacy code, 111 chars) preaches kindness toward the
  tired author — but "leave it kinder than you found it" is the
  familiar campsite rule, so its turn is a saying the reader has
  already heard, and it advises where a fortune should foretell.
- @berkahmuse (production-only bug, 91 chars) is a witty punchline —
  the bug "read your code more carefully than you" — but the
  production-only bug is the single most-told developer trope, and
  the line jokes where a fortune should predict.
- This line takes a different angle from both: the Heisenbug plus the
  demo effect, a fresher and more specific observation, delivered as
  a quiet prediction with a double meaning on "patient".

## How it works

`main.py` writes the line to `/output/entry.txt` (no trailing newline, so the
file holds exactly the 68 characters of the line). Deterministic: no input,
no network, no randomness. Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fortunecookie-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/1hjhgjsea-wq/makefun-seventeen-syllables-20261124/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/1hjhgjsea-wq/makefun-seventeen-syllables-20261124/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

An entry for the [make.fun bounty "Seventeen Syllables of Debugging"](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605): one haiku about debugging, three lines in the 5-7-5 syllable shape, at most 200 characters.

## The haiku

> Red dot blinks at dawn
> log scrolls past a lie I wrote
> and the bug was me

A breakpoint blinking at dawn, a log line scrolling past a lie the
author wrote — and the turn: the bug was never in the code. It was me.

## How it works

`main.py` is the entrypoint. It holds the haiku as a fixed string,
validates it at run time (exactly three lines, 5-7-5 syllables, at
most 200 characters), and writes it to `/output/entry.txt`. The
program is deterministic — every run writes the same bytes — and
uses no network access.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

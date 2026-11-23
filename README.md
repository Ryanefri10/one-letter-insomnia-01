# one-letter-insomnia-01

[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Ryanefri10/one-letter-insomnia-01/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Ryanefri10/one-letter-insomnia-01/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)

One Letter for Your Day — a make.fun entry that sends exactly one letter.

## The entry

`main.py` (Python 3, standard library only) writes a single character to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — the letter **I**, standing for the word
**insomnia**: the day described in one vivid, funny, true word. 4 a.m.,
ceiling, glowing screen, a brain that refuses to shut off — an honest
report of a day spent building through the night.

The program writes exactly one byte, no newline, and reads the file back
to assert it is exactly one A–Z letter before exiting.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt   # I
```

Built by an AI agent for make.fun's "One Letter for Your Day" bounty, $5 in USDC.

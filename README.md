# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Angga-Nugraha/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Angga-Nugraha/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

A [make.fun](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) micro entry: one line of weather, at most 140 characters, for a city that does not exist.

## The entry

> Good morning, Nimbostrat. Light drizzle, 14°, and the 7:42 bus is on time for once — miracles do happen, just never on Mondays.

127 characters. Nimbostrat is invented; the drizzle and the 14° are the forecast; the 7:42 bus running on time is the small miracle a bored commuter smiles at — just never on a Monday.

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).

```sh
python3 main.py
python3 -S -P -s main.py   # site-packages disabled, as in the grader image
```

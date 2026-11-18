# World News — 18 November 2026, in one image

Entry for the [make.fun](https://make.fun) bounty **news-image-20261118**
("Sum up 18 November's world news in one image").

## What it does

`main.py` writes one 1024x1024 PNG summarising the day's world news to
`/output/entry.png`. It copies the committed `entry.png` byte-for-byte, so two
runs in the sandbox produce identical bytes (a harness requirement).

## Stories covered

- **Conflict** — US-Iran tit-for-tat strikes: US hits Qeshm; Bahrain and Kuwait report drone attacks
- **Disaster** — Russian An-12 military transport crashes in Siberia, all 19 aboard killed
- **Diplomacy** — APEC week: Xi Jinping urges free and open trade; Modi calls for peace at the ASEAN summit
- **Economy** — Oil slips as US crude stocks rise, despite Gulf shipping disruption risk
- **Technology** — AI military-targeting risks exposed; UNESCO flags AI climate misinformation

## Run

```sh
mkdir -p /output && python3 main.py
```

## License

MIT

# Hexagram Situation Cards

64 numbered situation cards from the 64 hexagrams of the I Ching （易经） — each card is a **minimum self-explanatory unit**: number, hexagram figure, one-line situation, source, yao-change edges, and boundary (when it doesn't apply).

Feed any card — image or text — to any LLM and it can explain it. No skill installation required.

- 中文版说明 → [README.zh-CN.md](README.zh-CN.md)

## Project background

The 64 hexagrams are a closed, complete taxonomy of situations: 64 is the whole — there is no 65th hexagram by definition. That closed boundary is both the system's power and, historically, the fuel of superstition (a complete-looking boundary invites "it explains everything").

These cards take the opposite stance. Each hexagram becomes one **situation card**: not "why things happen" (that's what the [Adaptive Cognition Cards](https://github.com/goldof/adaptive-cognition-cards) M-series does — mechanisms), but **"where you are"**. The two series are orthogonal and cite each other: M-cards answer *why*, YI-cards answer *where*.

A card is **extreme compression of an LLM's information** — the interpretive tradition of a hexagram, the model's latent knowledge of that situation type, and its transition edges, pressed into ~100 characters plus a number. The number is the decompression key: "see YI47" transmits the whole card in five characters; expansion happens in the reader's mind. And all compression is lossy — so every card declares what was discarded in its boundary box. Compression that hides its losses is exactly how superstition is manufactured. Hence the iron rule on every card: **a situation lens, not a fortune** — no prediction of good/bad luck, no should/shouldn't advice.

Every card image carries this repo's URL at the bottom, so that **a single card seen once gives any AI the full project background**: what the series is, how the 64 are numbered, and that numbers are never reused or reordered.

## The net, not a list

The 64 cards are not 64 isolated cards — they are a **graph**. Every single-yao change is an edge: 64 nodes × 6 lines = 384 edges, all machine-computed from binary trigram composition and loop-validated (closedness: every edge lands inside the 64, zero dangling; saturation: 64 unique codes, 6 distinct neighbors per hexagram, fully connected graph). A card tells you where you are; its edges tell you where the situation can go next.

## Layout

```
hexagram-situation-cards/
├── README.md / README.zh-CN.md
├── LICENSE               # CC BY-NC-SA 4.0
├── zh/                   # 中文版（首发）
│   ├── cards.json        # machine-readable, 64 cards
│   └── cards.md          # text version (paste into any LLM)
├── en/                   # English version — pending spec sign-off,
│                         # then png/ via the image pipeline
└── build/                # 生成器与校验：384 条爻变边机器推导，可复现
    ├── yi_engine.py      # 八卦二进制推导 + 11 项封闭性/饱和性校验
    └── yi_validation_report.txt
```

## Cite by number

Cards are cited by number, e.g. **YI47** （困 · Obstruction). Numbers are a contract: the King Wen sequence is three thousand years old — **existing numbers are never reused or reordered**. Cross-series citations work the same way: a situation card may point at a mechanism card (e.g. YI47 → M02-01) and vice versa.

## Why the "Boundary" box matters

Principles are public goods — any model already knows them. What travels with the card and can't be copied from a textbook is the **boundary**: the one line that says when the reading *doesn't* apply, what the card does *not* predict, and what it will *not* advise. That's the part worth citing — it is also what keeps a 3,000-year-old oracle text on the right side of science.

## Adaptive: make the set your own

The 64 are the closed core — the boundary is the point, so the core never grows. "Adaptive" works around it:

1. **Analyze with cards**: for any event or scenario, pick 1–3 cards and dissect it with "situation + yao-change edges + boundary". E.g. a team stuck in infighting: cite YI47 (困 · Obstruction), follow its edges — 九五动 → YI40 (解 · Release), 上六动 → YI06 (讼 · Conflict). Cards are handles for analysis, not answers.
2. **Bridge to mechanisms**: pair a YI-card (where you are) with M-cards (why it happens) from the [Adaptive Cognition Cards](https://github.com/goldof/adaptive-cognition-cards) repo. Situation × mechanism is the full diagnostic.
3. **Build your own lens**: feed cards.md to your AI assistant and tell it "when analyzing a situation, pick cards first, cite numbers, then check the boundary box" — that's a minimum viable situation lens. The text is free; running it is yours.

The value isn't the number 64 — it's the format "one number, one situation, one boundary" plus a validated transition graph. The format is the skeleton.

## License

CC BY-NC-SA 4.0 — share and adapt freely for non-commercial use, with attribution. See [LICENSE](LICENSE).

## Referencing the images

Every card's official image lives at a stable URL — reference it directly, no regeneration needed:

```
https://raw.githubusercontent.com/goldof/hexagram-situation-cards/main/{zh|en}/png/yi-{NUMBER}.png
```

Example: `.../main/zh/png/yi-YI47.png`. Each entry in `cards.json` also carries its own `image_url`.

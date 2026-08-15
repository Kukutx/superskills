# Divination sources

Maintenance-only. These sources support historical/calendrical/method boundaries and exact chart inputs. They do **not** establish the predictive validity of divination or astrology.

## High-trust reference anchors

- Hong Kong Observatory Almanac / calendar resources — traditional Chinese calendar, 24 solar terms, time zones, solar transit and apparent-solar-time concepts.
  - https://www.hko.gov.hk/en/gts/astron2026/almanac2026_index.htm
  - https://www.hko.gov.hk/en/gts/time/24solarterms.htm
- Stanford Encyclopedia of Philosophy, “Chinese Philosophy of Change (Yijing)” — history, 64-hexagram divination context and philosophical interpretation.
  - https://plato.stanford.edu/entries/chinese-change/
- Metropolitan Museum of Art, Tarot history/structure — historical deck structure and later occult/divinatory use.
  - https://www.metmuseum.org/perspectives/tarot-2
- Oxford Bibliographies in Hinduism, “Astrology” by Martin Gansten — scholarly overview of Jyotiṣa and branches such as jātaka, muhūrta and praśna.
  - https://academic.oup.com/reference/62357/reference-article-abstract/554513393

## Calculation-tool candidates

These are **optional implementation candidates**, not runtime dependencies and not authorities for interpretation.

### Planetary astrology

- **Swiss Ephemeris / Astrodienst** — mature high-precision planetary/lunar ephemeris used widely by astrology software. Suitable for verified planetary positions and sidereal/tropical calculations when correctly configured.
  - https://www.astro.com/swisseph/
  - Licensing matters: GPL/open-source use and commercial licensing differ.

### Chinese calendar / BaZi inputs

- **6tail/lunar-python** — MIT-licensed Python library with solar/lunar conversion, 干支、节气、八字、五行、十神 and related calendar data. Useful as a practical implementation candidate; still cross-check boundary-sensitive calculations before treating output as canonical.
  - https://github.com/6tail/lunar-python
- **sxtwl** — astronomical Chinese calendar implementation with solar/lunar conversion, stem-branch data, broad historical range and true-solar-time-related support. More implementation-heavy than a simple Python-only library but useful when astronomical calendrical control matters.
  - https://github.com/skydancep/sxtwl

Do not auto-install any of these simply because the Skill is used. Adopt a calculator only when exact chart computation is an actual requirement.

## Traditional text families

Use these as historical/traditional interpretive sources, **not scientific evidence**. Editions, commentaries and school lineages vary.

- Yijing / Zhouyi and commentarial traditions
- 《三命通会》
- 《滴天髓》 and commentarial traditions
- 《子平真诠》
- 《渊海子平》
- 《增删卜易》 / 《卜筮正宗》 for 六爻 traditions
- 《梅花易数》 tradition
- 奇门遁甲、六壬、太乙 classical/commentarial traditions
- Jyotiṣa classical and modern scholarly translations appropriate to the branch being used

Do not treat a single modern website, calculator or social-media school as universal authority.

## Runtime verification policy

When exact calculation matters, re-check the relevant subset:

```text
civil date/time
historical timezone / DST
coordinates
solar-term boundary / calendar conversion
ephemeris / planetary positions
ayanāṁśa / house-system convention
charting-school convention
```

A source can establish a calendar or astronomical input without validating the symbolic interpretation built on top of it.

## Source quality rule

Prefer:

```text
astronomical/calendar institution
-> mature calculation library verified against authoritative data
-> academic/history reference
-> primary/traditional text or reputable edition
-> specialist secondary commentary
-> popular calculator/blog only as convenience
```

Never copy large interpretation tables into runtime references merely to look comprehensive. Preserve the rules that prevent wrong charting, method mixing and false precision.

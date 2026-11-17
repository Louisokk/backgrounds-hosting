# Herkunft und Lizenz der Szenen

Gilt für alle Dateien unter `v2/scenes/`. Im Katalog (`v2/catalog/scenes.json`) tragen die
Szenen `"license": "own"` und `"author": { "name": "G-Aesthetics", "origin": "official" }`.

## Bilder der Cinematic-Szenen

Alle Motive sind KI-generiert mit **ElevenLabs Image** (Modell GPT Image 2) in der ElevenLabs-App,
Konto des Owners im Starter-Plan mit kommerzieller Lizenz (Owner-Entscheidung S-6, 16.11.2026).
Es sind keine Fotos oder Werke Dritter eingeflossen. Geprüft in voller Auflösung: keine lesbare
Schrift, keine Marken. Prompts und Varianten stehen im Prototyp
(`g-aesthetics-prototyp/szenen/motive/PROMPTS.md`, `HERKUNFT.md`).

| Szene          | Motivdatei                    | generiert von               | Datum      | Original         |
| -------------- | ----------------------------- | --------------------------- | ---------- | ---------------- |
| `wanderer`     | `00-stiltest-gpt-a.png`       | Owner                       | 16.11.2026 | 2048 × 1152, PNG |
| `neonregen`    | `01-neonregen-gpt-a.png`      | Owner                       | 16.11.2026 | 2048 × 1152, PNG |
| `nebelwald`    | `02-nebelwald-gpt-a.png`      | Owner                       | 16.11.2026 | 2048 × 1152, PNG |
| `sternensee`   | `03-sternensee-gpt-a.png`     | Owner                       | 16.11.2026 | 2048 × 1152, PNG |
| `wueste`       | `04-wuestenmonument-gpt-a.png` | Owner                      | 16.11.2026 | 2048 × 1152, PNG |
| `kirschbluete` | `05-kirschbluete-gpt-b.png`   | Claude im Auftrag des Owners | 17.11.2026 | 3840 × 2160, PNG |
| `kueste`       | `06-kueste-gpt-a.png`         | Claude im Auftrag des Owners | 17.11.2026 | 3840 × 2160, PNG |
| `winter`       | `07-winter-gpt-b.png`         | Claude im Auftrag des Owners | 17.11.2026 | 3840 × 2160, PNG |
| `wolkeninseln` | `08-wolkeninseln-gpt-a.png`   | Claude im Auftrag des Owners | 17.11.2026 | 3840 × 2160, PNG |

## Abgeleitete Dateien

| Datei          | Herkunft                                                                                                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `image.webp`   | Motiv auf 2048 px Breite verkleinert, WebP Qualität 84                                                                                                                   |
| `depth.png`    | Tiefenkarte, 1024 px, berechnet mit **Depth Anything V2 Small** (`depth-anything/Depth-Anything-V2-small-hf`, Lizenz **Apache-2.0**). Base und Large sind nicht genutzt. |
| `poster.webp`  | verwischte Verkleinerung von `image.webp`                                                                                                                                |
| `preview.webp` | Verkleinerung von `image.webp` (Cinematic) bzw. Standbild der Szene (Generativ)                                                                                          |

Werkzeuge: `tools/scenes/tiefenkarte.py` und `tools/scenes/bauen.ts` im Repo der Extension.

## Generative Szenen

`gen_satin`, `gen_ridges`, `gen_fluted_glass`, `gen_ink_veil`: prozedural, ohne Bild. Der Shader
liegt im Bundle der Extension; hier liegt nur das Vorschaubild, ein Standbild der Szene in den
Prüf-Farben Grund `#0b0f1c` und Akzent `#8ab4f8`.

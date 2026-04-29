# **NanoBananaPro Drawing Prompt — V29**

Create a single high-resolution NeurIPS/CVPR-style scientific architecture figure titled **"Figure 1"**, rendered in a clean, publication-grade, horizontal layout (aspect ratio ≈ 16 : 7). Pure white page background. Typography: clean sans-serif for labels, italic serif for tensor names and math symbols. All tensor shapes written in `ℝ^{…}` notation. Thin black arrows with small arrowheads; no drop shadows anywhere **except** inside Panel C's four input blocks.

The figure is divided into **four vertically-bordered panels (A, B, C, D)** from left to right, each panel has its own soft pastel background tint and a bold capital letter label in the top-left corner.

---

## **Panel A — Input & Sampling** (soft warm-grey background)

Panel A is split into two horizontal sub-panels, A-top and A-bottom, with a thin dividing line.

### A-top: "Learnable Prompt Construction"

Two horizontal prompt rows, rendered in **extreme minimalist 2D flat-vector style** — every token is a crisp flat rectangle with a 2 px rounded corner, pure single-fill color, **no gradients, no bevels, no shadows, no 3D perspective**, clean 1 px outline.

- **Row 1 (Normal prompts, ×9):**
  `[🔥 learnable flame, small orange flat icon] [V₁] [V₂] [⋯] [V₁₂] ["real"] ["video"] ["."]`
  - `V₁ … V₁₂` rendered as **flat mustard-yellow squares** with tiny subscript indices, single uniform fill.
  - `"real"`, `"video"`, `"."` rendered as **flat light-grey squares** with the word inside plain quotes.
  - A small right-side label `× normal (9)`.

- **Row 2 (Anomaly prompts, ×14):**
  `[🔥 learnable flame] [W₁] [W₂] [⋯] [W₁₂] ["fake"] ["video"] ["."]`
  - `W₁ … W₁₂` as **flat warm-orange squares** (distinct from mustard).
  - Same flat grey style for the fixed-vocabulary squares.
  - Right-side label `× anomaly (14)`.

Caption under the two rows: `n_ctx = 12, class = 'video'`.

### A-bottom: "Video Sampling Pipeline"

A left-to-right flow:

1. **Input Video** — small play-button glyph.
2. → small rounded box **"Uniform Temporal Sampling"**.
3. → a **Shared Frame Pool (T = 32)** depicted as a stack of film-strip thumbnails — tensor tag `[B, 32, 3, 336, 336]`.
4. This pool then **forks into two branches** that become the input to Panel B:

- **Upper branch — SSS:** a solid navy-blue banner labelled **`SSS: All 32 frames`** with a long filmstrip of 32 thumbnails. Caption: `Full temporal coverage`. Shape tag: `[B, 32, 3, 336, 336]`.
- **Lower branch — TKS (via Hybrid Kinematic Sampling):**
  - Small rounded sub-box **"Hybrid Kinematic Sampling"** containing two parallel mini-icons:
    - `L1 Pixel Diff`
    - `Optical Flow Var`
  - Their outputs join into a small **"Score Fusion"** node (tag `[B, 2304]`).
  - Arrow to a `Top-K = 16` label.
  - → a solid rust-orange banner labelled **`TKS: 16 Keyframes`** with a filmstrip of 16 thumbnails. Caption: `L1 Diff + Flow Var → Top-16`. Shape tag: `[B, 16, 3, 336, 336]`.

---

## **Panel B — Encoders** (soft peach background)

Title: **"Encoders"**.

The three encoders (Text / SSS / TKS) are arranged vertically in Panel B (Text on top, SSS in the middle, TKS at the bottom).

**Critical rendering rule for all three encoders** — each encoder is drawn as a **horizontal deck of vertical slab-plates**:
- Think of a loaf of bread lying on its side, sliced into many thin vertical slices that are still stacked next to each other. Each "slice" is a thin vertical rectangular plate, and many such plates are arranged side-by-side along the horizontal X-axis to form a 3D block.
- You should see the left-most plate's front face clearly, and the top edges of all the plates receding slightly to the right via a gentle isometric tilt. The result is an overall shape that is **wider than it is tall** (aspect ratio roughly 1.5 : 1 horizontal).
- Use crisp flat-illustration 3D: each plate has a solid single-tone fill plus a very slight lightness shift across its vertical face to hint at 3D volume; the top edge gets a slightly lighter tint. No gradients, no textures, no bevels, no photoreal shading.
- Alternate the plate tones very subtly (a darker plate, a lighter plate, repeat) so the "deck" reads clearly as a stack.
- **Do not** render the encoders as vertical pancake towers, as single flat rectangles, or as diagonal hex-stacks. The plates must be vertical and arranged horizontally.

The three encoders:

1. **Text Encoder** 🔥 (learnable flame above the deck, orange plate-deck).
   - Input: the two learnable prompt rows from Panel A-top.
   - Output: a single arrow exiting the right side of the deck labelled **"Text Features"**, which crosses into Panel C. **Do not draw any output boxes or feature labels inside Panel B** — the receiving cubes (`T*_normal`, `T*_anomaly`) live in Panel C only.

2. **SSS Encoder** ❄️ (frozen snowflake above the deck, steel-blue plate-deck) — tag `SSS (32 frames)` below the deck.
   - Output: a single arrow exiting the right side labelled **"SSS frame features"** with tensor tag `[B, 32, 768]`, crossing into Panel C. **No output boxes inside Panel B.**

3. **TKS Encoder** ❄️ (frozen snowflake above the deck, teal plate-deck) — tag `TKS (16 keyframes)` below the deck.
   - Output: a single arrow exiting the right side labelled **"TKS frame features"** with tensor tag `[B, 16, 768]`, crossing into Panel C. **No output boxes inside Panel B.**

A small vertical label **"Shared"** sits between the SSS and TKS encoders, indicating weight sharing.

**Panel B contains ONLY the three encoder plate-decks and their connecting arrows and labels.** All feature containers (`T*_normal`, `T*_anomaly`, `F*_SSS`, `F*_TKS`) are rendered exclusively as 3D cubes inside Panel C — they must never appear as extra boxes or pills inside Panel B.

---

## **Panel C — Feature Space & Fusion** (soft yellow-gold background) ★ *MAIN PANEL*

Title: **"Feature Space & Fusion"**.

### (1) The four input blocks — **rendered as small 3D cubes**

There are **exactly four cubes in Panel C, no more and no less** — one for each of `T*_normal`, `T*_anomaly`, `F*_SSS`, `F*_TKS`. **Do not draw any duplicate cube** for concatenated combinations such as `[T*_normal ; T*_anomaly]` — such combinations only exist as internal operations inside the Central Fusion Engine and must **never** be represented as an additional external cube. **Do not duplicate the input-cube column on both the top and bottom halves — it must appear only once per group.**

The four feature containers (`T*_normal`, `T*_anomaly`, `F*_SSS`, `F*_TKS`) are drawn as **small solid 3D isometric cubes** — each a single compact cube (roughly square aspect ratio), not stacks of plates, not card decks. Each cube shows three visible faces (top + two sides) with a clean isometric projection, a subtle soft drop shadow underneath, and a slightly lighter highlight on the top face to signal volume. Style is **flat-illustration 3D** (crisp single-tone faces with only a one-step lightness shift between faces), **not** photoreal, **no gradients, no textures, no bevels**. All four cubes are the **same size**.

- `T*_normal` — pink cube.
- `T*_anomaly` — rose cube (same size as `T*_normal`, distinguished only by its deeper rose tint).
- `F*_SSS` — medium-blue cube.
- `F*_TKS` — teal cube.

Each cube carries its `ℝ^{…}` shape tag and caption directly below it (e.g. `ℝ^{9×768}`, `ℝ^{14×768}`, `ℝ^{B×768}` — "Semantic context", `ℝ^{B×768}` — "Peak anomaly signal").

### Panel C global 2×2 quadrant layout (MANDATORY)

Panel C is divided into a clean 2×2 quadrant arrangement:

```
┌────────────────────────┬──────────────────────────────────────────┐
│  TOP-LEFT              │  TOP-RIGHT                               │
│                        │                                          │
│  Text cubes (2)        │  CMS sub-module                          │
│   • T*_normal          │  (Cross-Modal Similarity Scoring)        │
│   • T*_anomaly         │  ⑦ L2-Norm → ⑧ Dot → ⑨ ×τ → Sim scores  │
│  (vertically stacked)  │                                          │
├────────────────────────┼──────────────────────────────────────────┤
│  BOTTOM-LEFT           │  BOTTOM-RIGHT                            │
│                        │                                          │
│  Video cubes (2)       │  Gate sub-module                         │
│   • F*_SSS             │  (Gated Residual Fusion)                 │
│   • F*_TKS             │  ① Diff → ② Concat → ③ mini-MLP →        │
│  (vertically stacked)  │  ④ σ → G → ⑤ ⊗ → ⑥ ⊕ → F*_video          │
└────────────────────────┴──────────────────────────────────────────┘
```

Key rules for this layout:
- **Left column (both rows) holds ONLY cubes** — no engine modules touch the left column.
- **Right column (both rows) holds the engine's two sub-modules** — no cubes touch the right column.
- Within the top-left quadrant, `T*_normal` sits **above** `T*_anomaly` (vertical stack, **not side-by-side**). Shape tags sit directly below each cube.
- Within the bottom-left quadrant, `F*_SSS` sits **above** `F*_TKS` (vertical stack, **not side-by-side**). Shape tags and captions sit directly below each cube.
- The two engine sub-modules on the right column together form **one single rounded rectangle** — the "Central Fusion Engine" — spanning both top and bottom rows, sharing ONE unified soft-lavender background; a thin dotted horizontal divider inside this rectangle separates CMS (above) from Gate (below).

**Arrow routing (clean, no crossings):**
- The two **text cubes** on the top-left send horizontal arrows rightward → directly into the **TOP-RIGHT CMS sub-module**.
- The two **video cubes** on the bottom-left send horizontal arrows rightward → directly into the **BOTTOM-RIGHT Gate sub-module**.
- Because text feeds top and video feeds bottom on the same horizontal levels, the four input arrows are all straight and parallel — no crossings, no diagonals.

### (2) The **Central Fusion Engine** — one unified module (no more CMS / CRGN split label)

A single large rounded rectangle labelled **"Central Fusion Engine"** 🔥 with two ★★ stars indicating highest importance. It spans the full right column of Panel C. **Internally the layout is strictly flat 2D** (no isometric tricks inside), but densely populated and organised into **two horizontal lanes** — CMS on the top half, Gate on the bottom half — connected by a vertical relay. Use thin arrows and small circled step numbers ① → ⑨ to guide the reader.

**Bottom lane — Gated Residual Fusion (F_SSS, F_TKS → F*_video):**

Inputs enter from the left: the two video cubes `F*_SSS` and `F*_TKS` from the bottom-left quadrant.
 → **① |·−·|** (small box with absolute-value bars, labelled `Diff`, operating on both F_SSS and F_TKS)
 → **② [▢▢▢]** (concat icon, three stacked rectangles, label `Concat`, takes `[F_SSS, F_TKS, |F_SSS − F_TKS|]`)
 → **③ mini-MLP** (a tiny yellow 2-layer perceptron glyph)
 → **④ σ** (sigmoid S-curve inside a small circle), producing a purple pill labelled **`G`** (gate vector).
 → **⑤ G ⊗ F_TKS** (a circled-cross gated-multiply node).
 → **⑥ F_SSS ⊕ (G ⊗ F_TKS)** (a circled-plus element-wise sum node).
 → produces a purple pill labelled **`F*_video ∈ ℝ^{B×768}`** sitting at the lane's right end.

**Vertical relay inside the engine:** a single upward arrow takes `F*_video` from the right end of the bottom lane **up** into the right end of the top lane, where it joins the CMS scoring pipeline.

**Top lane — Cross-Modal Similarity Scoring (F*_video, T* → Similarity):**

Inputs enter from the left: the two text cubes `T*_normal` and `T*_anomaly` from the top-left quadrant (they are conceptually concatenated `[T*_normal ; T*_anomaly]` at the entry point — no separate cube needed).
 → **⑦ L2-Norm** (two parallel small boxes labelled `∥·∥₂ (text)` and `∥·∥₂ (video)`, stacked vertically; the video branch receives `F*_video` from the upward relay)
 → **⑧ · Dot Product** (a small filled dot inside a circle, with the label `⟨·,·⟩`)
 → **⑨ × τ** (learnable flame 🔥 on a small yellow box labelled `Temperature scaling τ`)
 → final output arrow exiting the engine to the right, feeding a thin pill labelled **`Similarity scores ∈ ℝ^{B×23}`**.

Design rules for the engine interior:
- Everything inside is **flat 2D** — no perspective, no shadows.
- **The entire engine interior uses ONE single unified background color — a uniform very-soft lavender wash across both lanes.** Do NOT give the two lanes different background tints; they share the same background because they are one merged module. Only a thin dotted horizontal divider separates the two lanes as a purely organisational guide — the background color on both sides of the divider must be identical.
- The two lane sub-headers ("Cross-Modal Similarity Scoring" on top, "Gated Residual Fusion" on bottom) sit directly on this shared lavender background, using the same typography and the same title color.
- Keep the step-number circles small and consistent; never put more than one operator per circled step.
- The density of elements must be **at least as high as the previous CMS + CRGN combined version**, but visually calmer because of the clean quadrant geometry.

The `Similarity scores [B, 23]` pill exits Panel C on the right, crossing into Panel D.

---

## **Panel D — Prediction & Loss (V24)** (soft lavender background)

Title: **"V24"**.

Top-to-bottom flow:

1. **Prompt Ensemble** — two circular **μ** icons side by side, labelled `Mean ×9` (over the 9 normal columns) and `Mean ×14` (over the 14 anomaly columns). They pool the `[B, 23]` scores into two class logits.
2. → circular **C** node (Concat) producing `[B, 2]`.
3. → rounded box **Softmax**.
4. → **Prediction** arrow labelled `→ Real / Fake`.
5. A short side-branch labelled **Loss** points from the prediction into:
   - **CE Loss** box with sub-text `weights = [1.0, 2.0]`, `smooth = 0.1`.
6. **Ground Truth** pill at the bottom: `y ∈ {0, 1}`, feeding into the CE Loss box with a dotted arrow.

---

## **Legend (bottom of the figure, single horizontal strip, white pill)**

`🔥 Learnable | ❄️ Frozen | × Cosine similarity | ⊕ Element-wise sum | ⊗ Gated multiply | μ Mean pooling | M Max pooling | C Concat | · Dot product`

Below the legend, centered, small italic serif caption: **`Figure 1`**.

---

## Global style reminders

- The **only 3D / stereoscopic elements in the entire figure are the four small input cubes of Panel C** (`T*_normal`, `T*_anomaly`, `F*_SSS`, `F*_TKS`). Every other component — including the Central Fusion Engine interior, the Panel A prompt tokens, the Panel B encoder stacks (these remain lightly isometric as in previous versions), and all of Panel D — stays consistent with the previous version's styling.
- The **Panel A learnable prompt tokens must be extreme-minimalist flat 2D vector** — absolutely no beveling, gradients, or shadows.
- Maintain alignment: arrows are strictly horizontal or vertical (no diagonals except inside the isometric stacks).
- Color palette stays restrained: orange/flame = learnable, teal/blue = frozen vision, pink/rose = text, lavender = fusion/output, grey = fixed tokens / data.

---

## Self-check

- ✅ Panel C's **4 input blocks** (T\*_normal, T\*_anomaly, F\*_SSS, F\*_TKS) are rendered as **small 3D isometric cubes** — exactly 4 cubes total, **no duplication across quadrants**.
- ✅ Panel B's three encoders (Text / SSS / TKS) are drawn as **horizontal decks of vertical slab-plates** (wider than tall). **No output feature boxes live inside Panel B** — all four feature cubes live in Panel C only.
- ✅ Panel C uses a **2×2 quadrant layout**:
  - Top-left: text cubes (`T*_normal` above `T*_anomaly`, vertically stacked)
  - Top-right: CMS sub-module (Cross-Modal Similarity Scoring)
  - Bottom-left: video cubes (`F*_SSS` above `F*_TKS`, vertically stacked)
  - Bottom-right: Gate sub-module (Gated Residual Fusion)
- ✅ Arrow routing is **horizontal and parallel** — no crossings: text → top-right CMS; video → bottom-right Gate. Only one internal vertical arrow relays `F*_video` upward from Gate (bottom) to CMS (top).
- ✅ Central Fusion Engine uses **one unified lavender background** across both lanes (CMS on top, Gate on bottom, merged into one rounded rectangle).
- ✅ Panel C's engine is **merged into a single "Central Fusion Engine"** — CMS / CRGN labels removed — with a **flat 2D two-lane interior** (top: Gated Residual Fusion ①–⑥, bottom: Cross-Modal Similarity Scoring ⑦–⑨) preserving the original element density but neater.
- ✅ Pipeline logic matches source code:
  `G = σ(MLP(Concat[F_SSS, F_TKS, |F_SSS − F_TKS|]))`
  → `F*_video = F_SSS ⊕ (G ⊗ F_TKS)`
  → `τ · ⟨L2(F*_video), L2([T_n; T_a])⟩`
  → `Similarity scores ∈ ℝ^{B×23}`.
- ✅ Panel A's `V₁…V₁₂` / `W₁…W₁₂` tokens specified as **minimalist 2D flat-vector squares** (no shadows / gradients / 3D).
- ✅ Panels B, D, legend, typography and color scheme remain visually consistent with V28.

# Deliverable 13: Design System
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document defines visual design rules for the website. It translates the approved UI/UX Research and Wireframes into concrete standards for color, typography, buttons, cards, spacing, icons, and components, so that future HTML/CSS/JavaScript development in VS Code follows a consistent visual language.

> **Note on the color palette:** No business screenshots have been shared in this conversation, so the palette below is a practical recommendation based on the travel/ticketing identity and trust-building goals defined in earlier documents — not colors extracted from actual brand assets. If the business already has brand colors (e.g., from its Facebook Page or logo), those should replace the recommendation below.

---

# 2. Design System Overview

A design system is the website's style rulebook. It keeps colors, fonts, buttons, cards, and spacing consistent, so that every page looks and feels like it belongs to the same, professional business — rather than looking like a patchwork of separately styled sections.

---

# 3. Brand Direction

The recommended brand feel for v1 is:
- **Professional** — appropriate for services involving money and government documents.
- **Travel-inspired** — subtle visual cues connecting to travel and journeys.
- **Friendly** — approachable, not cold or overly corporate.
- **Trustworthy** — consistent, honest, and free of exaggerated visual claims.
- **Clear** — content and structure that's easy to scan and understand.
- **Accessible** — usable by visitors with different visual or motor abilities.

---

# 4. Color System

| Name | Hex Code | Usage | Accessibility Note |
|---|---|---|---|
| Primary — Deep Ocean Blue | #0B4F6C | Header background, primary buttons, main navigation highlights | Passes contrast with white text (#FFFFFF) for buttons and headers |
| Secondary — Warm Sand | #F2A65A | Secondary buttons, highlight accents, icon backgrounds | Use with dark text (#1A1A1A) for sufficient contrast |
| Accent — Sunset Coral | #E76F51 | CTA buttons, "Inquire Now" highlights, important notices | Use with white text; avoid on light backgrounds without contrast check |
| Background — Soft White | #FAFAF8 | Page background | Provides comfortable contrast with dark text |
| Text — Charcoal Gray | #2B2B2B | Body text, headings | Meets standard contrast requirements against Soft White background |
| Success — Teal Green | #2A9D8F | Confirmation notes (e.g., "message sent" indicators, if used) | Use sparingly; verify contrast against background |
| Info — Sky Blue | #6FB3D2 | Informational notes or tips (e.g., FAQ callouts) | Use with dark text for readability |
| Warning — Muted Amber | #E9C46A | Important notices (e.g., "pricing confirmed upon inquiry") | Use with dark text; avoid overuse to prevent alarm-like appearance |

**General rule:** Primary and Background colors should dominate the page; Secondary and Accent colors are used sparingly for buttons and highlights; Success/Info/Warning colors are reserved only for their specific purpose and should not be used decoratively.

---

# 5. Typography System

**Font Choice (free Google Fonts only):**
- **Heading Font:** "Poppins" — clean, modern, slightly rounded, suitable for a friendly-but-professional travel brand.
- **Body Font:** "Inter" — highly readable at small sizes, works well across devices.

**Font Sizes (recommended base scale):**
- H1 (Page Title): 32–40px desktop / 26–28px mobile
- H2 (Section Heading): 24–28px desktop / 20–22px mobile
- H3 (Card/Subsection Heading): 18–20px
- Body Text: 16px minimum (never smaller, per accessibility guidance)
- Small Text (footer, notes): 14px minimum

**Font Weights:**
- Headings: Semi-Bold (600) or Bold (700)
- Body Text: Regular (400)
- Emphasis/Labels: Medium (500)

**Line Height:**
- Headings: 1.2–1.3
- Body Text: 1.5–1.6 for comfortable reading

**Mobile Readability Rules:**
- Body text must never render below 16px on mobile.
- Line length should stay comfortable (avoid full-width text stretching edge to edge on wide mobile screens; use container padding).
- Avoid excessive bold or all-caps text blocks, which reduce readability.

---

# 6. Button System

### Primary Button
- **Purpose:** Main action on a page (e.g., "View Our Services").
- **Visual Style:** Solid Primary color background, white text, rounded corners.
- **Usage Rules:** One primary button per section maximum, to avoid competing calls to action.

### Secondary Button
- **Purpose:** Supporting action alongside a primary button (e.g., "Learn More").
- **Visual Style:** Outlined or Secondary color background, dark text, same rounded style as primary.
- **Usage Rules:** Used when a second, less urgent option is needed next to a primary CTA.

### Contact Button
- **Purpose:** Directly opens a contact channel (phone, Messenger, Viber, WhatsApp, Telegram).
- **Visual Style:** Icon + label combination, Accent color or channel-appropriate styling, consistent size across all five channels.
- **Usage Rules:** Always grouped together (per FR-009); never presented as a single isolated button without its channel siblings, so visitors see all options at once.

### CTA Button ("Inquire Now")
- **Purpose:** Prompts an inquiry after reading service or package content.
- **Visual Style:** Accent color, bold label, slightly larger than standard secondary buttons to draw attention.
- **Usage Rules:** Appears once per service/package entry; wording must never imply booking confirmation or payment (per BR-002, BR-003).

### Disabled/Unavailable State
- **Purpose:** Not expected to be used in v1, since there are no forms or interactive submissions, but included for completeness in case of future partial content (e.g., a service temporarily unavailable).
- **Visual Style:** Muted gray background, reduced-opacity text, no hover effect.
- **Usage Rules:** Only used if the business owner explicitly marks a service as temporarily unavailable; not used by default.

---

# 7. Card System

### Service Cards
- Contain: service name, short description, icon (optional), "Inquire Now" CTA.
- Consistent card size and spacing across the Services page grid.

### Tour Package Cards
- Contain: package category name, short description, note that details are confirmed upon inquiry, CTA.
- Same visual style as service cards for consistency, with a travel-themed icon or accent if used.

### FAQ Items
- Contain: question (bold/heading style) and answer (body text), presented as a list or accordion.
- Visual separation between each Q&A pair (e.g., divider line or spacing) for easy scanning.

### Contact Channel Cards
- Contain: channel icon, channel name (e.g., "Messenger"), and a tap/click target covering the full card.
- Uniform sizing across all five channels (phone, Messenger, Viber, WhatsApp, Telegram) so no channel appears more prominent than another.

---

# 8. Layout and Spacing System

- **Page Width:** Max content width of approximately 1200px on desktop, centered, with fluid width on smaller screens.
- **Section Spacing:** Consistent vertical spacing between sections (e.g., 64–80px desktop, 40–48px mobile) to create clear visual separation.
- **Grid Rules:** Service and Tour Package cards use a responsive grid — e.g., 4 columns on desktop, 2 on tablet, 1 on mobile.
- **Mobile Stacking:** All grid layouts collapse into a single vertical column on mobile, consistent with the Wireframes' mobile notes.
- **Container Padding:** Minimum 16–24px horizontal padding on mobile to prevent text and buttons from touching screen edges.

---

# 9. Icon and Image Guidelines

- **Icon Style:** Simple, line-based or minimally filled icons for consistency (e.g., a single icon set used throughout, not mixed styles).
- **Image Usage:** Travel-related imagery (e.g., landmarks, transportation, luggage) used sparingly to support the travel-inspired brand direction without distracting from content.
- **Alt Text Rules:** Every image must include descriptive alt text, per FR-011 and NFR-003.
- **Travel-Related Image Guidance:** Use general, royalty-free travel imagery rather than specific real airline, ferry, or hotel branding, to avoid implying an official partnership that hasn't been confirmed.
- **Avoiding Misleading Images:** Do not use imagery that implies a live booking interface, payment screen, or confirmed reservation, consistent with BR-002, BR-003, and BR-012.

---

# 10. Accessibility Rules

- **Color Contrast:** All text/background combinations must meet comfortable readability standards; avoid light text on light backgrounds or low-contrast color pairings.
- **Focus States:** All interactive elements (links, buttons, menu items) must show a visible focus outline when navigated via keyboard.
- **Button Size:** Minimum comfortable tap target size (approximately 44x44px) for all buttons, especially contact buttons on mobile.
- **Text Readability:** Body text no smaller than 16px; avoid long unbroken paragraphs.
- **Keyboard Navigation Support:** All navigation, buttons, and links must be reachable and operable using the Tab key and Enter/Space, without requiring a mouse.

---

# 11. Component Rules

- **Header:** Contains logo/business name and main navigation; consistent height and background across all pages.
- **Navbar:** Horizontal on desktop, collapsible on mobile; active page indicated visually.
- **Mobile Menu:** Toggles open/closed via a clearly labeled icon (e.g., hamburger icon); full list of main pages visible when open.
- **Hero Section:** Appears only on the Homepage; contains business name, slogan explanation, short intro, and primary/secondary CTAs.
- **Service Card:** Reusable across Homepage (preview) and Services page (full grid); consistent structure per Section 7.
- **CTA Banner:** A visually distinct horizontal section used to prompt inquiries (e.g., before the footer); consistent style across pages that use it.
- **Footer:** Appears identically on every page; contains business name, condensed contact links, and copyright notice.
- **Contact Button Group:** A consistent, reusable set of five contact buttons (phone, Messenger, Viber, WhatsApp, Telegram), used on Homepage, Services, Tour Packages, and Contact pages.

---

# 12. Design Do's and Don'ts

**Do:**
- Keep layouts simple, with clear spacing between sections.
- Use one primary color, one accent color, and neutral backgrounds/text as the dominant palette.
- Make CTAs and contact buttons visually prominent and consistent.
- Keep text sizes readable on both mobile and desktop.

**Don't:**
- Don't overcrowd layouts with too many competing sections or CTAs on one screen.
- Don't use booking-like visuals (e.g., calendar pickers, seat maps, payment forms) since v1 has no booking or payment functionality (BR-002, BR-003).
- Don't use too many colors — stick to the defined palette in Section 4 rather than introducing new colors ad hoc.
- Don't use small, unreadable text — body text must stay at or above 16px.
- Don't use weak or vague CTAs (e.g., "Click Here") — use clear, specific wording like "Inquire Now" or "Message Us on Viber."

---

# 13. Summary

This Design System defines the visual rules for the v1 website: a professional, travel-inspired, trustworthy brand direction; a practical color palette built around a deep blue primary, warm sand secondary, and coral accent; a two-font typography system using free Google Fonts (Poppins and Inter); consistent button, card, and component rules; and clear accessibility and spacing standards. Explicit do's and don'ts prevent overcrowded layouts, misleading booking-style visuals, and weak CTAs. This document is ready to guide consistent HTML and CSS implementation across all pages in the next phase of development.

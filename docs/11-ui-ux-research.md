# Deliverable 11: UI/UX Research
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document identifies UX principles, user needs, and design considerations before wireframing. It draws on the approved use cases, user stories, business rules, and information architecture to establish how the website should feel and behave for visitors, ahead of any wireframe or visual design work.

---

# 2. UI/UX Research Overview

UI/UX research helps decide how the website should feel and work for visitors before designing the actual screens. For v1, this means understanding what different visitors need, what could confuse or frustrate them, and what design principles will support the site's inquiry-focused purpose.

---

# 3. Target User Needs

### Potential Customer
Needs a fast, clear way to understand what the business offers and whether it can be trusted, without prior knowledge of the "8-in-1" slogan.

### Existing Customer
Needs quick access to contact options and service confirmation, without having to re-read the full site each time.

### Mobile Visitor
Needs a layout that works comfortably on a small screen, with easy-to-tap buttons and no awkward zooming or side-scrolling.

### First-Time Visitor
Needs an immediate, plain-language explanation of the business and its services, since they arrive with no prior context.

### Business Owner / Staff
Needs the website to reduce repetitive basic questions by answering them clearly on the site, so incoming inquiries are better-informed and easier to handle.

---

# 4. UX Goals

- **Clear service understanding** — visitors should grasp what each of the 8 services means without needing to ask.
- **Fast contact access** — a contact option should never be more than a click or two away.
- **Mobile-first usability** — the experience should be designed primarily for mobile screens, then adapted upward.
- **Trust-building** — the site should look and feel credible, professional, and honest.
- **Low confusion** — especially around the "8-in-1" slogan, which must never be mistaken for a booking platform.
- **Simple navigation** — visitors should always know where they are and how to get to another page.

---

# 5. Design Considerations

- **Travel-related visual identity** — imagery and color choices that evoke travel and assistance (e.g., subtle travel motifs) without overwhelming the informational content.
- **Service card layout** — presenting each of the 8 services as a distinct, scannable card or block rather than a long unbroken paragraph.
- **Strong CTAs** — inquiry buttons that stand out visually and use consistent, action-oriented wording (e.g., "Inquire Now").
- **Readable typography** — clear, legible fonts at a comfortable size for both mobile and desktop reading.
- **Clear page sections** — each page divided into visually distinct sections (e.g., intro, services, CTA) rather than one continuous block of text.
- **Contact visibility** — contact buttons should be visually prominent, not buried at the bottom of a page.
- **FAQ clarity** — questions and answers formatted for easy scanning (e.g., collapsible or clearly separated Q&A blocks).
- **Mobile-friendly layout** — content and navigation designed to remain usable and attractive on small screens first.

---

# 6. Trust-Building UX

The website can build trust without inventing claims by focusing on how information is presented, not by adding unverified content:
- **Clear business identity** — consistent use of the business name, slogan, and description across every page.
- **Consistent contact details** — the same phone number and messaging links appearing correctly everywhere they're shown.
- **Transparent service descriptions** — describing each service honestly as assistance, per BR-007, without exaggerating capability.
- **No overpromising** — avoiding language that implies guaranteed pricing, availability, or instant confirmation, per BR-010 and BR-012.
- **Professional layout** — clean, uncluttered design signals legitimacy even without additional trust badges or claims.
- **Clear explanation of "8-in-1 Ticketing System"** — visible early (Homepage) and reinforced later (FAQs), preventing the single biggest source of visitor confusion.

---

# 7. Mobile UX Considerations

- **Thumb-friendly buttons** — contact buttons and CTAs sized and spaced for easy tapping with a thumb.
- **Collapsible navigation** — a toggle/hamburger menu that keeps the mobile screen uncluttered, per FR-008.
- **Fast loading** — lightweight pages and optimized images so mobile visitors on slower data connections aren't kept waiting, per NFR-001.
- **Short text sections** — breaking content into short, digestible chunks rather than long paragraphs, suited to smaller screens.
- **Visible contact buttons** — keeping contact options within easy reach as the visitor scrolls, not only at the very top or bottom of a page.
- **Simple page flow** — a single, clear vertical flow of content on mobile, avoiding complex multi-column layouts that are hard to navigate on a small screen.

---

# 8. Accessibility Considerations

- **Color contrast** — sufficient contrast between text and background for readability, per FR-011 and NFR-003.
- **Alt text** — descriptive alternative text for all images.
- **Keyboard navigation** — all interactive elements (menu, buttons, links) reachable without a mouse.
- **Clear labels** — buttons and links labeled in plain language (e.g., "Message Us on Viber" rather than an unlabeled icon alone).
- **Readable font size** — body text large enough to read comfortably without zooming.
- **Logical heading order** — headings structured in a clear hierarchy (e.g., one main heading per page, followed by properly nested subheadings).

---

# 9. Content UX Considerations

- **Short paragraphs** — content broken into small, scannable blocks rather than dense text.
- **Clear headings** — each section labeled so visitors can scan and find what they need quickly.
- **Plain language** — avoiding jargon, especially when explaining the "8-in-1" slogan and each service.
- **Service explanations** — each of the 8 services described in terms of what assistance the customer receives, not technical or internal business language.
- **CTA wording** — consistent, honest phrasing (e.g., "Inquire Now," "Message Us") that never implies a completed booking or payment.
- **Avoiding misleading claims** — no pricing, schedules, or availability presented as fixed or guaranteed unless confirmed by the owner, per BR-010 and BR-011.

---

# 10. UX Risks and Mitigation

| UX Risk | Impact | Mitigation |
|---|---|---|
| Visitors misunderstand "8-in-1" as an automated booking system | Confused or frustrated inquiries; mismatched expectations | Explain the slogan clearly and early, on both Homepage and FAQs (BR-006) |
| Contact options are hard to find | Visitors leave without inquiring, reducing lead generation | Place contact buttons prominently on Homepage, Services, and Tour Packages pages (FR-009) |
| Long, dense text blocks overwhelm mobile visitors | High bounce rate, poor mobile experience | Use short paragraphs, clear headings, and card-style service layout |
| Visitors assume prices/availability shown are guaranteed | Complaints or lost trust when actual details differ | Clearly label all pricing/package info as general, pending inquiry (BR-010) |
| Inconsistent contact details across pages | Visitor confusion, failed contact attempts | Keep a single source of contact data (per Data Dictionary) reused across all pages |
| Poor color contrast or small text reduces readability | Excludes visitors with visual impairments; general readability issues | Apply accessibility considerations from Section 8 consistently |
| Cluttered navigation with too many links | Visitors get lost or overwhelmed | Keep navigation limited to the six approved primary pages (Information Architecture) |

---

# 11. Design Direction Recommendation

The recommended overall design direction for v1 is:
- **Professional** — visually clean and business-appropriate, suitable for services involving money and government documents.
- **Clean** — minimal clutter, clear sections, and generous spacing.
- **Travel-inspired** — subtle visual cues related to travel and assistance, without overwhelming the informational focus.
- **Trustworthy** — consistent branding, honest content, and no exaggerated claims.
- **Mobile-first** — designed primarily for comfortable mobile use, then scaled up for tablet and desktop.
- **Simple and practical** — straightforward layouts that prioritize clarity and ease of use over decorative complexity, fitting a zero-budget, static website.

---

# 12. Summary

This UI/UX Research document identifies the needs of five user types, defines six core UX goals, and outlines design, trust-building, mobile, accessibility, and content considerations for the v1 website. A UX risk table highlights the most likely points of visitor confusion or frustration — particularly around the "8-in-1" slogan and contact visibility — along with practical mitigations already supported by the approved business rules and requirements. The recommended design direction is professional, clean, travel-inspired, trustworthy, mobile-first, and simple, providing a clear foundation for the next stage: wireframing.

# Deliverable 12: Wireframes
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document provides low-fidelity text-based wireframes for the website pages. It translates the approved Information Architecture and UI/UX Research into a section-by-section layout for each page, showing where content and features belong before any visual design or coding begins.

---

# 2. Wireframe Overview

Wireframes are rough page layouts. They show where sections go before we decide final colors and styling. Each wireframe below describes the sections of a page from top to bottom, without specifying fonts, colors, or images — those decisions come later in visual design.

---

# 3. Global Layout Structure

Common layout elements shared across all pages:
- **Header** — business name/logo and main navigation, fixed or visible at the top of every page.
- **Navigation** — links to Home, About, Services, Tour Packages, FAQs, Contact (collapses to a mobile menu on small screens).
- **Main Content Area** — the unique content of each page, organized into clear sections.
- **CTA Sections** — inquiry prompts placed near relevant content (e.g., after a service description).
- **Footer** — business name, condensed contact links, and copyright notice, appearing on every page.
- **Contact Buttons** — phone, Messenger, Viber, WhatsApp, Telegram, appearing on select pages (Homepage, Services, Tour Packages) in addition to the Contact page.

---

# 4. Homepage Wireframe

```
[ HEADER ]
  Logo / Business Name        Navigation: Home | About | Services | Tour Packages | FAQs | Contact

[ HERO SECTION ]
  Business Name
  Slogan: "8-in-1 Ticketing System" + one-line explanation
  Short introductory description
  [ Primary CTA: "View Our Services" ]   [ Secondary CTA: "Contact Us" ]

[ SERVICES PREVIEW ]
  Section Heading: "Our 8 Services"
  Grid or row of 8 short service labels/icons (Airline, Ferry, Bus, Hotel, Tour Packages,
  Visa/Passport, Bills Payment, E-Loading)
  [ CTA: "See All Services" → links to Services page ]

[ WHY CHOOSE US ]
  Section Heading: "Why Choose Us"
  Short trust-building points (e.g., personal assistance, multiple contact channels)
  [Content pending owner confirmation]

[ TOUR PACKAGES PREVIEW ]
  Section Heading: "Tour Packages"
  Short teaser text about available tour package assistance
  [ CTA: "View Tour Packages" → links to Tour Packages page ]

[ FAQ PREVIEW ]
  Section Heading: "Common Questions"
  2–3 sample questions (e.g., "What does 8-in-1 mean?")
  [ CTA: "See All FAQs" → links to FAQs page ]

[ CONTACT CTA ]
  Section Heading: "Get in Touch"
  Short prompt: "Have a question? Reach out anytime."
  Contact buttons: Phone | Messenger | Viber | WhatsApp | Telegram

[ FOOTER ]
  Business Name | Condensed Contact Links | Copyright Notice
```

---

# 5. About Page Wireframe

```
[ HEADER ]

[ PAGE TITLE ]
  "About Homeland Travel and Tours – GBM Prestige Ticketing"

[ BUSINESS INTRODUCTION ]
  Short paragraph on business background
  [Content pending owner confirmation]

[ BUSINESS ROLE / ASSISTANCE PROVIDER EXPLANATION ]
  Explanation that the business assists with travel and everyday transactions,
  rather than owning airlines, hotels, or government processes directly

[ MISSION / VISION PLACEHOLDER ]
  [Placeholder section — to be filled in if owner provides mission/vision statement]

[ TRUST-BUILDING SECTION ]
  Optional credibility points (e.g., years active, service philosophy)
  [Content pending owner confirmation]

[ CONTACT CTA ]
  Short prompt inviting further questions
  Contact buttons or link to Contact page

[ FOOTER ]
```

---

# 6. Services Page Wireframe

```
[ HEADER ]

[ PAGE TITLE ]
  "Our Services — 8-in-1 Ticketing System"

[ 8-IN-1 EXPLANATION ]
  Short paragraph: "8-in-1 Ticketing System" refers to 8 categories of assistance,
  not an automated booking platform

[ SERVICE CARDS GRID ]
  8 cards, one per service, each showing:
    - Service Name
    - One-line description
    - [ "Inquire Now" button ]

[ INDIVIDUAL SERVICE SECTIONS ]
  1. Airline Ticketing Assistance — description + CTA
  2. Ferry Ticketing Assistance — description + CTA
  3. Bus Ticketing Assistance — description + CTA
  4. Hotel Booking Assistance — description + CTA
  5. Tour Packages — description + CTA (+ link to full Tour Packages page)
  6. Visa and Passport Processing Assistance — description + CTA
  7. Bills Payment — description + CTA
  8. E-Loading — description + CTA

[ INQUIRY CTA ]
  Closing section: "Don't see what you need? Message us directly."
  Contact buttons

[ FOOTER ]
```

---

# 7. Tour Packages Page Wireframe

```
[ HEADER ]

[ PAGE TITLE ]
  "Tour Packages"

[ TOUR PACKAGE INTRODUCTION ]
  Short paragraph introducing tour package assistance

[ PACKAGE CATEGORY CARDS OR PLACEHOLDER AREAS ]
  General categories or example placeholders (e.g., "Local Getaways," "International Trips")
  [Content pending owner confirmation]

[ IMPORTANT NOTES ]
  Note clarifying that pricing, schedules, and availability are provided upon inquiry,
  not guaranteed on the site (per BR-010)

[ INQUIRY CTA ]
  "Interested in a tour package? Contact us for details."
  Contact buttons

[ FOOTER ]
```

---

# 8. FAQs Page Wireframe

```
[ HEADER ]

[ PAGE TITLE ]
  "Frequently Asked Questions"

[ FAQ ACCORDION OR Q&A LIST ]
  Q: What does "8-in-1 Ticketing System" mean?
  A: [Explanation — not a software system, but 8 categories of assisted services]

  Q: How do I make an inquiry?
  A: [Explanation of available contact channels]

  Q: Do you process bookings or payments on this website?
  A: [Clarification — no, all transactions are handled manually through contact channels]

  Q: [Additional FAQs — pending owner input]

[ CONTACT CTA ]
  "Still have questions? Reach out directly."
  Contact buttons

[ FOOTER ]
```

---

# 9. Contact Page Wireframe

```
[ HEADER ]

[ PAGE TITLE ]
  "Contact Us"

[ CONTACT INTRODUCTION ]
  Short prompt: "Reach us through any of the channels below."

[ CONTACT BUTTON GRID ]
  Phone | Messenger | Viber | WhatsApp | Telegram
  (each button clearly labeled and tappable)

[ PHONE NUMBERS ]
  Primary business phone number displayed as text and clickable link

[ SOCIAL / MESSAGING LINKS ]
  Facebook Page link
  Messenger / Viber / WhatsApp / Telegram links repeated as direct links

[ OPTIONAL BUSINESS HOURS / ADDRESS PLACEHOLDER ]
  [Content pending owner confirmation — include only if owner wants it public]

[ FOOTER ]
```

---

# 10. Mobile Wireframe Notes

- **Stack sections vertically** — all page sections (Hero, Services Preview, etc.) stack in a single column on mobile, in the same order as desktop.
- **Use full-width buttons** — CTAs and contact buttons expand to the full width of the screen for easier tapping.
- **Collapse navigation** — main navigation condenses into a toggle/hamburger menu, per FR-008.
- **Keep CTAs visible** — inquiry and contact CTAs remain easy to reach as the visitor scrolls, not hidden below excessive content.
- **Keep text short and readable** — paragraphs shortened and broken into smaller chunks to suit smaller screens, consistent with the UI/UX Research content guidance.

---

# 11. Wireframe Rules

- No booking forms.
- No payment sections.
- No login areas.
- No database-backed features.
- Every main page should lead to contact options, either through a contact button, CTA, or footer link.

---

# 12. Summary

This Wireframes document provides text-based, low-fidelity layouts for all six core pages — Homepage, About, Services, Tour Packages, FAQs, and Contact — organized section by section according to the approved Information Architecture and UI/UX Research. Each wireframe places services, CTAs, and contact options consistently, while explicitly excluding booking forms, payment sections, login areas, and any database-backed features. Mobile-specific notes ensure the same structure adapts cleanly to smaller screens. This document is ready to guide visual design and HTML/CSS structuring in the next phase of development.

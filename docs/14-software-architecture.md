# Deliverable 14: Software Architecture
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document defines the technical structure of the website before coding. It translates the approved requirements, information architecture, and design system into a lightweight architecture description, so that development in VS Code follows a clear, consistent technical structure from the start.

---

# 2. Architecture Overview

The website will be made of static files that run in the browser. There is no server-side processing, no database, and no backend logic — HTML, CSS, and JavaScript files are served as-is, and all interactivity (like opening a contact app) happens entirely on the visitor's device.

---

# 3. Architecture Style

- **Static Website Architecture** — all pages are pre-built HTML files with associated CSS and JavaScript; nothing is generated dynamically on a server.
- **Client-Side Only** — any interactivity (e.g., mobile menu toggle, FAQ accordion) runs entirely in the visitor's browser using JavaScript, with no server communication.
- **Multi-Page / Section-Based Website** — the site is organized as six distinct HTML pages (Home, About, Services, Tour Packages, FAQs, Contact), each containing clearly defined sections, consistent with the approved Information Architecture.
- **External Communication Links for Inquiries** — all "contact" actions are simple links that open external apps (Messenger, Viber, WhatsApp, Telegram) or the device's phone dialer; the website itself does not handle the conversation.

---

# 4. System Context

| Entity | Relationship to the Website |
|---|---|
| Website Visitors | Browse static pages, read content, and click contact links/buttons to reach the business. |
| Business Owner/Staff | Do not interact with the website as a system (no admin dashboard exists); they receive and respond to inquiries through their existing apps, which the website links to. |
| Facebook Page | Remains the business's separate, existing social presence; the website may link to it (e.g., in the footer) but does not embed or control it. |
| Messenger | External app opened via a direct link (e.g., m.me/[page]) when a visitor clicks the Messenger contact button. |
| Viber | External app opened via a direct link or number when a visitor clicks the Viber contact button. |
| WhatsApp | External app opened via a direct link (e.g., wa.me/[number]) when a visitor clicks the WhatsApp contact button. |
| Telegram | External app opened via a direct link (e.g., t.me/[username]) when a visitor clicks the Telegram contact button. |
| Phone Calls | Initiated via a standard tel: link that triggers the device's dialer. |
| Free Static Hosting | Hosts the finished HTML/CSS/JS files and serves them to visitors' browsers; no server-side code runs here. |

The website acts purely as an informational hub and a bridge — it presents content and then hands the visitor off to one of these external channels for any real interaction.

---

# 5. Component Architecture

| Component | Role |
|---|---|
| Header | Displays business name/logo; anchors the main navigation at the top of every page. |
| Navigation | Provides links to all six main pages; consistent across the site. |
| Mobile Menu | A collapsible version of the navigation for smaller screens, toggled via JavaScript. |
| Hero Section | Introduces the business and slogan on the Homepage; includes primary CTAs. |
| Service Cards | Reusable component displaying a service name, short description, and CTA; used on Homepage (preview) and Services page (full set). |
| Tour Package Cards | Reusable component displaying general package categories/examples and a CTA. |
| FAQ Section | Displays question-and-answer content, optionally with simple expand/collapse behavior via JavaScript. |
| Contact Buttons | A reusable group of five buttons/links (phone, Messenger, Viber, WhatsApp, Telegram), used on multiple pages. |
| Footer | Displays business name, condensed contact links, and copyright notice on every page. |
| 404 Page/Message | Displays a simple "page not found" message with a link back to the Homepage, per FR-013. |

Each component is built once and reused across pages where applicable, keeping the codebase consistent and easy to maintain.

---

# 6. Page Architecture

| Page | Role |
|---|---|
| Home | Entry point of the site; introduces the business, previews services, and directs visitors toward Services, Tour Packages, FAQs, and Contact. |
| About | Provides business background and trust-building content to support credibility. |
| Services | Presents all 8 services in detail, each with its own inquiry CTA. |
| Tour Packages | Presents general tour package information as a dedicated, more detailed extension of the Tour Packages service. |
| FAQs | Answers common questions, most importantly explaining the "8-in-1 Ticketing System" slogan. |
| Contact | Consolidates all contact channels in one place as the site's primary conversion point. |

---

# 7. Data Flow

The website's data flow is intentionally simple, consistent with the Database Design/ERD Decision (no database in v1):

1. No customer data is collected by the website — there are no forms or storage mechanisms.
2. A visitor reads content and clicks a contact button (e.g., "Message Us on Viber").
3. The visitor's browser or device hands off to an external app or the phone dialer, based on the link type (e.g., `tel:`, `m.me/`, `wa.me/`, `t.me/`).
4. The actual transaction — the conversation, quotation, and confirmation — happens entirely outside the website, within that external app or phone call.

No information ever flows back into the website or is stored by it at any point in this process.

---

# 8. Security and Privacy Architecture

- **No stored customer data** — the site has no database or storage mechanism, so there is nothing to secure or leak.
- **No login credentials** — there are no user accounts, so there is no authentication system to protect.
- **No payment processing** — the site never handles card numbers, e-wallet credentials, or any financial transaction data.
- **No uploaded documents** — visa, passport, or other sensitive files are never submitted through the website.
- **External messaging apps handle communication** — all actual conversations happen within Messenger, Viber, WhatsApp, Telegram, or a phone call, each governed by that platform's own security and privacy protections, not the website's.

This architecture keeps the website's security responsibility minimal: since it holds no sensitive data, there is very little attack surface to defend.

---

# 9. Deployment Architecture

- **Static Files** — the finished website consists of HTML, CSS, and JavaScript files with no build server or backend required at runtime.
- **Free Hosting** — the site can be deployed using a free static hosting service (e.g., GitHub Pages), consistent with the zero-budget constraint.
- **Public or Private Repository** — the source code can be hosted in either a public or private repository depending on the business owner's preference; a public repository (as already used for the related One Mandaluyong project structure) is common for portfolio purposes, but this choice belongs to the owner.
- **Simple Update Workflow** — updating content means editing the relevant static file (HTML/CSS/JS) and redeploying; no database migrations or backend restarts are needed.

---

# 10. Architecture Constraints

- Zero budget — no paid hosting, licensing, or third-party paid tools.
- Static only — no server-side rendering or processing.
- No backend — no application server of any kind.
- No database — no persistent storage layer.
- No third-party paid service — any external tool used (fonts, icons) must be free.
- Maintainable in VS Code — the codebase must remain simple enough to edit directly in a code editor without specialized deployment tooling.

---

# 11. Future Architecture Considerations

**The following are future scope only and are not designed in detail here. None of this applies to v1.**

If the business later expands the website, possible future architecture additions may include:
- Inquiry form (would require basic backend handling)
- Admin dashboard (would require authentication and a management interface)
- Database (would be needed to support the above two items)
- Booking workflow (would require integration with providers and a data layer)
- Payment integration (would require a secure payment gateway and compliance considerations)

These are noted only as future directions to keep in mind while structuring the v1 codebase (e.g., organizing files so they could be extended later) — they are not part of the current build.

---

# 12. Summary

This Software Architecture document defines v1 of the Homeland Travel and Tours – GBM Prestige Ticketing website as a static, client-side-only, multi-page site with no backend, database, or API. It describes how visitors, the business owner, and existing communication channels (Facebook, Messenger, Viber, WhatsApp, Telegram, phone) relate to the system, outlines reusable components and page roles, and confirms that all data flow ends at an external app or phone call rather than within the website itself. Security and privacy responsibilities remain minimal due to the absence of stored data, and deployment relies on free static hosting with a simple, VS Code–friendly update workflow. Future features such as forms, a database, or booking/payment integration are explicitly deferred, keeping v1 lightweight, low-risk, and fully aligned with its approved scope.

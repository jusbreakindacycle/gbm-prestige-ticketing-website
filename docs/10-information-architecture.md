# Deliverable 10: Information Architecture
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document defines the structure, organization, and navigation of the website. It builds on the approved requirements, use cases, user stories, business rules, and data dictionary to describe how pages are organized, how content is placed, and how visitors move through the site during v1.

---

# 2. Information Architecture Overview

Information architecture is the website map. It shows what pages exist, where content belongs, and how visitors move through the website. For v1, this means organizing six core pages so that visitors can quickly understand the business, explore its 8 services, and reach a contact channel without confusion.

---

# 3. Website Structure

**Sitemap:**

```
Home
├── About
├── Services
│   ├── Airline Ticketing Assistance
│   ├── Ferry Ticketing Assistance
│   ├── Bus Ticketing Assistance
│   ├── Hotel Booking Assistance
│   ├── Tour Packages (summary, links to full Tour Packages page)
│   ├── Visa and Passport Processing Assistance
│   ├── Bills Payment
│   └── E-Loading
├── Tour Packages
├── FAQs
└── Contact
```

The 8 services are presented as sections within the Services page rather than as separate pages, keeping navigation simple while still giving each service its own clear space. Tour Packages also has its own dedicated page, since it was identified as a distinct use case (UC-04) and user story (US-05) requiring more detail than a short service entry.

---

# 4. Navigation Structure

**Main Navigation:**
Home | About | Services | Tour Packages | FAQs | Contact
Appears at the top of every page, consistent with FR-007.

**Footer Navigation:**
Condensed links to all main pages, plus contact links and copyright notice, consistent with the Data Dictionary's Footer content elements.

**Mobile Navigation:**
Collapses into a toggle/hamburger menu on smaller screens, per FR-008. All six main pages remain reachable from the expanded menu.

**CTA Navigation:**
Inquiry CTAs ("Inquire Now") appear alongside service descriptions and tour package content, linking directly to the Contact page or triggering a contact button, per FR-010.

**Contact Button Placement:**
Contact buttons (phone, Messenger, Viber, WhatsApp, Telegram) appear on the Homepage, Services page, and Tour Packages page, in addition to being fully listed on the Contact page, per FR-009.

---

# 5. Page Hierarchy

**Primary Pages** (directly accessible from main navigation):
- Home
- About
- Services
- Tour Packages
- FAQs
- Contact

**Supporting Sections** (exist within a primary page, not as separate navigation items):
- The 8 individual service entries, within the Services page
- FAQ question-and-answer entries, within the FAQs page
- Footer content, appearing on every page but not a standalone destination

This keeps the navigation to six clear destinations while still giving each service and topic enough dedicated space to be useful.

---

# 6. Content Placement

### Home
- **Main Content:** Business name, slogan with brief explanation, short introduction.
- **Supporting Content:** Summary preview of the 8 services.
- **CTA Placement:** Primary CTA linking to Services; secondary CTA linking to Contact.
- **Related Links:** Services, Contact.

### About
- **Main Content:** Business background and description.
- **Supporting Content:** Trust-building details (pending owner confirmation).
- **CTA Placement:** Link to Contact for further questions.
- **Related Links:** Services, FAQs.

### Services
- **Main Content:** All 8 service entries with descriptions.
- **Supporting Content:** Brief note explaining the "8-in-1" slogan at the top of the page.
- **CTA Placement:** Inquiry CTA beside each individual service.
- **Related Links:** Tour Packages (from the Tour Packages service entry), Contact.

### Tour Packages
- **Main Content:** General tour package categories or examples.
- **Supporting Content:** Note clarifying that details are provided upon inquiry.
- **CTA Placement:** Inquiry CTA for tour packages.
- **Related Links:** Services, Contact.

### FAQs
- **Main Content:** Explanation of "8-in-1 Ticketing System," how to inquire, and what the site does not handle.
- **Supporting Content:** Additional common questions (pending owner input).
- **CTA Placement:** Link to Contact for unanswered questions.
- **Related Links:** Services, Contact.

### Contact
- **Main Content:** Phone number, Messenger, Viber, WhatsApp, and Telegram links.
- **Supporting Content:** Business hours and address, if confirmed by the owner.
- **CTA Placement:** Contact buttons are the page's core content.
- **Related Links:** Home, Services.

### Footer (appears on every page)
- **Main Content:** Business name and condensed contact links.
- **Supporting Content:** Copyright notice.
- **CTA Placement:** None additional — footer reinforces existing contact options.
- **Related Links:** Quick links to Services and Contact.

---

# 7. User Flow

### New Visitor Learning About the Business
Home → About → Services → FAQs (optional, if "8-in-1" needs clarifying) → Contact

### Visitor Browsing Services
Home or Main Navigation → Services → (optional: Tour Packages, if interested) → Inquiry CTA → Contact channel

### Visitor Contacting the Business
Any page → Contact button or CTA → External app (Messenger, Viber, WhatsApp, Telegram) or phone dialer

### Mobile Visitor Navigating the Site
Any page → Tap mobile menu toggle → Select destination page → Page loads → Repeat as needed

### Search Visitor Landing on a Page
Search engine result → Lands directly on a specific page (often Services or FAQs) → Main Navigation → Explores other pages as needed → Contact

---

# 8. URL Structure

Recommended clean URL paths for v1:
- `/` — Home
- `/about` — About
- `/services` — Services (includes all 8 service entries)
- `/tour-packages` — Tour Packages
- `/faqs` — FAQs
- `/contact` — Contact

These paths are short, descriptive, and consistent with the page names used throughout the approved documents, supporting both usability and SEO (per FR-012, NFR-011).

---

# 9. Information Architecture Rules

- Every page must include access to contact options, either through the main navigation, a contact button, or the footer.
- Every service must have an inquiry CTA, consistent with FR-010 and BR-005.
- Navigation must remain simple, limited to the six primary pages with no additional top-level items.
- No hidden critical information — service descriptions, contact details, and the "8-in-1" explanation must be visible without requiring extra clicks beyond the main navigation.
- The "8-in-1" explanation must be easy to find, appearing on both the Homepage and the FAQs page, consistent with BR-006.

---

# 10. Summary

This Information Architecture document defines a simple, six-page structure — Home, About, Services, Tour Packages, FAQs, and Contact — with the 8 services organized as sections within the Services page. Navigation stays consistent across desktop, mobile, and footer, with contact buttons and inquiry CTAs placed throughout to support easy access to existing communication channels. Clean URL paths, defined content placement per page, and clear user flows ensure the site structure directly supports the approved use cases, user stories, and business rules. This document is ready to guide page layout and navigation coding in VS Code.

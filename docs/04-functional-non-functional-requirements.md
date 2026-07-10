# Deliverable 04: Functional & Non-Functional Requirements
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document expands and organizes the functional and non-functional requirements already defined in the System Requirements Specification (SRS) into a clearer, implementation-ready checklist. It is meant to be used directly by the developer while building the v1 website in VS Code, making it easy to confirm that each required feature and quality standard has been addressed before launch.

---

# 2. Functional Requirements Overview

Functional requirements describe what the website must do. These are the specific features, pages, and actions the website needs to provide so that visitors can learn about the business and reach it for inquiries.

---

# 3. Functional Requirements List

| Requirement ID | Requirement Name | Description | Priority | Related Page/Section | Acceptance Criteria |
|---|---|---|---|---|---|
| FR-001 | Homepage Display | Display the business name, slogan, short introduction, and a summary of services on the main landing page. | High | Homepage | Homepage loads at the site's root; shows business name, "8-in-1 Ticketing System" slogan with brief explanation, and links to Services and Contact. |
| FR-002 | About Page | Present business background, description, and trust-building information. | High | About | Page is reachable from navigation; content matches the approved Research Foundation and Business Analysis documents; no unverified claims are stated as fact. |
| FR-003 | Services Page | List and explain all 8 services offered under the "8-in-1 Ticketing System." | High | Services | All 8 services are listed with a short description each; every service includes an inquiry CTA. |
| FR-004 | Tour Packages Page | Present general tour package categories or examples. | Medium | Tour Packages | Page is reachable from navigation or Services page; content avoids fixed pricing or real-time availability claims; includes an inquiry CTA. |
| FR-005 | FAQs Page | Answer common customer questions, including a clear explanation of the "8-in-1" slogan. | High | FAQs | Page is reachable from navigation; includes at minimum an explanation of "8-in-1," how to inquire, and confirmation that bookings/payments are not handled on the site. |
| FR-006 | Contact Page | Consolidate all communication channels in one place. | High | Contact | Displays phone number and clickable links for Messenger, Viber, WhatsApp, and Telegram; reachable from navigation and CTAs sitewide. |
| FR-007 | Main Navigation | Provide a consistent menu linking to all main pages. | High | Sitewide | Navigation appears on every page with links to Home, About, Services, Tour Packages, FAQs, and Contact. |
| FR-008 | Mobile Navigation | Adapt the navigation menu for smaller screens. | High | Sitewide | On mobile screen widths, navigation collapses into an accessible menu (e.g., toggle/hamburger); all links remain reachable. |
| FR-009 | Contact Buttons | Provide clickable contact buttons on key pages beyond the Contact page. | High | Homepage, Services, Tour Packages | Contact buttons for phone, Messenger, Viber, WhatsApp, and Telegram appear on at least the Homepage, Services, and Tour Packages pages. |
| FR-010 | Inquiry Call-to-Action | Prompt visitors to reach out after reading about a service. | High | Homepage, Services, Tour Packages | Each service description includes at least one CTA (e.g., "Inquire Now") linking to a contact method; wording does not imply booking or payment. |
| FR-011 | Accessibility Support | Support visitors with different needs through basic accessible design. | Medium | Sitewide | Images include alt text; text/background contrast is readable; all interactive elements are reachable by keyboard. |
| FR-012 | SEO Support | Improve discoverability through basic search engine optimization elements. | Medium | Sitewide | Each page has a descriptive title and meta description; content uses clear heading structure; keywords accurately reflect the business. |
| FR-013 | Error Handling | Handle broken links or invalid URLs gracefully. | Medium | Sitewide | A custom "page not found" message displays for invalid URLs, with a link back to the Homepage; contact links are verified working before launch. |

---

# 4. Non-Functional Requirements Overview

Non-functional requirements describe how well the website should work. These cover qualities such as speed, ease of use, security, and compatibility, rather than specific features.

---

# 5. Non-Functional Requirements List

| Requirement ID | Requirement Name | Description | Priority | Measurement or Acceptance Criteria |
|---|---|---|---|---|
| NFR-001 | Performance | The website should load quickly on typical internet connections, including mobile data. | High | Pages load within a few seconds on a standard mobile data connection; images are reasonably sized. |
| NFR-002 | Usability | The website should be easy to use and understand without instructions. | High | A first-time visitor can find service information and a contact method within a few clicks/taps. |
| NFR-003 | Accessibility | The website should follow basic accessible design practices. | Medium | Alt text, sufficient contrast, and keyboard navigability are present, as defined in FR-011. |
| NFR-004 | Security | The website should not collect or expose sensitive customer data. | High | No forms collect personal, payment, or identity information; all contact happens through external messaging apps. |
| NFR-005 | Privacy | The website should not track or store personal visitor data beyond standard, privacy-respecting analytics if used. | Medium | No personal data is captured directly by the site; any analytics tool discloses its purpose. |
| NFR-006 | Reliability | The website should remain accessible without requiring ongoing server maintenance. | High | Site stays available on free static hosting with minimal downtime under normal conditions. |
| NFR-007 | Maintainability | The website should be simple enough to update without specialized tools. | High | Content (text, services, links) can be updated by editing static files directly. |
| NFR-008 | Scalability | The website's structure should allow future features to be added without a full rebuild. | Medium | Pages and code are organized so new sections can be added incrementally in later versions. |
| NFR-009 | Browser Compatibility | The website should work correctly across major modern browsers. | High | Site displays and functions correctly on the latest versions of Chrome, Safari, Firefox, and Edge. |
| NFR-010 | Mobile Responsiveness | The website should adapt its layout to different screen sizes. | High | All pages display and function correctly on common mobile, tablet, and desktop widths. |
| NFR-011 | SEO | The website should be structured to support search engine discoverability. | Medium | Meets the SEO-related criteria defined in FR-012. |

---

# 6. Requirement Priority Guide

- **High:** Essential for v1 launch. The website is not considered complete or usable without this requirement.
- **Medium:** Important for quality and professionalism, but the site can still function at a basic level without it. Should be included if time and effort allow.
- **Low:** Optional improvements that add polish but are not necessary for v1 to meet its core purpose.

---

# 7. Requirement Traceability Summary

| Project Goal | Related Functional Requirements | Related Non-Functional Requirements |
|---|---|---|
| Increase business credibility | FR-001, FR-002, FR-005 | NFR-002, NFR-006 |
| Showcase services clearly | FR-003, FR-004, FR-005 | NFR-002, NFR-011 |
| Improve online visibility | FR-012 | NFR-011 |
| Generate customer inquiries | FR-009, FR-010 | NFR-002 |
| Make it easier to contact the business | FR-006, FR-007, FR-008, FR-009 | NFR-002, NFR-010 |
| Provide a professional, trustworthy experience | FR-002, FR-011, FR-013 | NFR-001, NFR-003, NFR-004, NFR-009, NFR-010 |
| Keep the site maintainable at zero budget | — | NFR-006, NFR-007, NFR-008 |

---

# 8. Out-of-Scope Requirements

The following are explicitly not part of v1 and must not be implemented:
- Booking system
- Payment system
- Database
- Admin dashboard
- Customer portal
- Real-time availability (tickets, hotel rooms, or pricing)
- Online form that collects personal data

---

# 9. Development Constraints

Future development in VS Code must follow these boundaries:
- Build a **static website only** — no dynamic backend processing.
- All customer inquiries are directed to **existing contact channels** (phone, Messenger, Viber, WhatsApp, Telegram), not handled on the site itself.
- **No database** of any kind.
- **No backend** server-side logic.
- **No online payment** functionality.
- **No customer data storage** — the site must not retain any personal visitor information.
- The site **must be responsive**, working correctly on mobile, tablet, and desktop screens.
- The site **must be simple to maintain**, allowing content updates through direct file edits without specialized tools.

---

# 10. Summary

This document expands the approved SRS into an implementation-ready requirements specification.

It defines thirteen functional requirements and eleven non-functional requirements that will guide website development, testing, and future validation while keeping the project within its approved scope.

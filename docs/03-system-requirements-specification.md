# System Requirements Specification (SRS)
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Introduction

## 1.1 Purpose
This document defines the functional and non-functional requirements for v1 of the Homeland Travel and Tours – GBM Prestige Ticketing website. It translates the findings of the Research Foundation and Business Analysis documents into concrete, verifiable requirements that will guide development in VS Code and serve as the basis for testing and acceptance.

## 1.2 Project Overview
The website is a static, informational business website designed to present the business, explain its "8-in-1 Ticketing System" service offering, build customer trust, and direct visitors to existing inquiry channels (phone, Messenger, Viber, WhatsApp, Telegram). It does not perform bookings, process payments, store customer data, or provide real-time ticket availability.

## 1.3 Intended Audience
This document is intended for:
- The website developer(s) implementing v1
- The business owner reviewing and approving requirements
- Future contributors extending the website in later versions

## 1.4 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|---|---|
| 8-in-1 Ticketing System | Marketing slogan representing 8 categories of customer assistance services offered by the business |
| CTA | Call-to-Action — a prompt directing the visitor to take an action, such as contacting the business |
| FAQ | Frequently Asked Questions |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| BR | Business Rule |
| Static Website | A website with fixed content that does not connect to a database or backend system |
| Inquiry Channel | Any existing communication method the business uses to receive customer inquiries (phone, Messenger, Viber, WhatsApp, Telegram) |

## 1.5 Scope of the Document
This SRS covers only v1 of the website: a public, static, informational site. It excludes booking systems, payment systems, databases, admin dashboards, and real-time data features, consistent with the scope already defined in the Research Foundation and Business Analysis documents.

---

# 2. Overall Description

## Product Perspective
The website is a new, standalone product. It does not replace or integrate with the business's existing Facebook Page or messaging channels — it complements them by serving as an independent, centralized information source that funnels visitors toward those same channels for actual transactions.

## Product Goals
- Present the business clearly and professionally to new and returning visitors.
- Explain all 8 services in a way that removes ambiguity around the "8-in-1" slogan.
- Provide clear, working contact options across all relevant pages.
- Increase the volume and quality of customer inquiries received through existing channels.
- Establish a foundation that can support future enhancements without requiring a full rebuild.

## User Classes
- **Potential Customers** — first-time visitors evaluating the business before contacting it.
- **Existing Customers** — repeat visitors looking for quick reference or contact information.
- **Business Owner/Staff** — indirect users who rely on the site to reduce repetitive inquiries and represent the business professionally.

## User Characteristics
- Likely to access the site primarily via mobile devices, consistent with reliance on mobile messaging apps (Messenger, Viber, WhatsApp, Telegram).
- Vary in technical proficiency; the site must be usable without requiring any technical knowledge.
- May not be familiar with the term "8-in-1 Ticketing System" and require plain-language explanation.

## Operating Environment
The website must run as a static site accessible through standard web browsers on both desktop and mobile devices, without requiring any server-side processing, account creation, or app installation.

## Assumptions
- Visitors have access to at least one of the listed messaging apps or a phone to complete an inquiry.
- The business will keep its existing messaging channels active and monitored, as the site depends on them for all actual transactions.
- Content such as service descriptions and contact details will be supplied or confirmed by the business owner.

## Constraints
- Zero development budget: no paid hosting, licensing, or premium tools.
- No backend, database, or server-side processing in v1.
- All actual transactions remain manual and occur outside the website.
- Visa/passport and similar time-sensitive information must be described in general terms to avoid becoming outdated.

---

# 3. Functional Requirements

### FR-001 — Homepage Display
**Description:** The system shall display a homepage introducing the business, its slogan, and a summary of its services.
**Priority:** High
**Acceptance Criteria:**
- Homepage loads by default at the site's root URL.
- Displays business name, a short introductory description, and the "8-in-1 Ticketing System" slogan with a brief explanation.
- Includes a visible link or button to the Services page and to contact options.

### FR-002 — About Page
**Description:** The system shall provide an About page describing the business background, purpose, and trust-building information.
**Priority:** High
**Acceptance Criteria:**
- Page is reachable from the main navigation.
- Contains business description content consistent with the Research Foundation and Business Analysis documents.
- Does not state unverified claims (e.g., specific partner names) unless confirmed by the business owner.

### FR-003 — Services Page
**Description:** The system shall display all 8 services with individual descriptions explaining what assistance each service provides.
**Priority:** High
**Acceptance Criteria:**
- All 8 services (Airline, Ferry, Bus, Hotel, Tour Packages, Visa/Passport, Bills Payment, E-Loading) are listed.
- Each service includes a short, plain-language description of the assistance provided.
- Each service section includes a CTA directing the visitor to an inquiry channel.

### FR-004 — Tour Packages Page
**Description:** The system shall provide a dedicated page or section presenting available tour package categories or examples.
**Priority:** Medium
**Acceptance Criteria:**
- Page is reachable from the main navigation or Services page.
- Displays general tour package information without implying real-time availability or fixed pricing unless confirmed accurate.
- Includes a CTA for inquiries.

### FR-005 — FAQs Page
**Description:** The system shall provide a Frequently Asked Questions page addressing common customer questions, including an explanation of the "8-in-1 Ticketing System" slogan.
**Priority:** High
**Acceptance Criteria:**
- Page is reachable from the main navigation.
- Includes at minimum: what "8-in-1 Ticketing System" means, how to make an inquiry, and what the business does and does not handle (e.g., no online booking/payment).
- Content is presented in a clear question-and-answer format.

### FR-006 — Contact Page
**Description:** The system shall provide a Contact page consolidating all available communication channels.
**Priority:** High
**Acceptance Criteria:**
- Lists phone number and links/buttons for Messenger, Viber, WhatsApp, and Telegram.
- Each contact option is clickable/tappable and directs the visitor to the correct app or dialer where technically supported.
- Page is reachable from the main navigation and from CTAs throughout the site.

### FR-007 — Site Navigation
**Description:** The system shall provide a consistent navigation menu across all pages.
**Priority:** High
**Acceptance Criteria:**
- Navigation menu appears on every page with links to Home, About, Services, Tour Packages, FAQs, and Contact.
- Current page is visually indicated in the navigation, where feasible.

### FR-008 — Contact Buttons
**Description:** The system shall provide contact buttons (phone, Messenger, Viber, WhatsApp, Telegram) accessible from key pages, not only the Contact page.
**Priority:** High
**Acceptance Criteria:**
- Contact buttons appear on the Homepage, Services page, and Tour Packages page at minimum.
- Buttons are visually distinct and clearly labeled with the corresponding channel.

### FR-009 — Inquiry Call-to-Action
**Description:** The system shall present inquiry-oriented CTAs throughout the site to prompt visitors to reach out.
**Priority:** High
**Acceptance Criteria:**
- Each service description includes at least one CTA (e.g., "Inquire Now") linking to a contact method.
- CTA wording avoids implying that inquiries submit a booking or payment.

### FR-010 — Responsive Navigation
**Description:** The system shall adapt its navigation menu for smaller screens (e.g., collapsible mobile menu).
**Priority:** High
**Acceptance Criteria:**
- On mobile-width screens, the navigation collapses into an accessible menu (e.g., a toggle/hamburger menu).
- All navigation links remain reachable and functional at all screen sizes.

### FR-011 — Accessibility Features
**Description:** The system shall include basic accessibility features to support users with different needs.
**Priority:** Medium
**Acceptance Criteria:**
- All images include descriptive alternative text.
- Text and background colors maintain sufficient contrast for readability.
- All interactive elements (menu, buttons, links) are reachable via keyboard navigation.

### FR-012 — SEO Features
**Description:** The system shall include basic search engine optimization elements to improve discoverability.
**Priority:** Medium
**Acceptance Criteria:**
- Each page includes a descriptive page title and meta description.
- Content uses clear heading structures (e.g., one main heading per page).
- Pages include relevant, accurate keywords reflecting the business and its services without misrepresentation.

### FR-013 — Error Handling
**Description:** The system shall handle broken links or missing pages gracefully.
**Priority:** Medium
**Acceptance Criteria:**
- A custom "page not found" message is displayed for invalid URLs, with a link back to the Homepage.
- Any non-functional contact link is identified and corrected prior to launch.

---

# 4. Non-Functional Requirements

### NFR-001 — Performance
**Description:** The website shall load efficiently on standard internet connections, including mobile data.
**Priority:** High
**Acceptance Criteria:** Pages load within a few seconds on a typical mobile data connection; image files are reasonably sized to avoid excessive load times.

### NFR-002 — Usability
**Description:** The website shall be easy to navigate and understand without prior instruction.
**Priority:** High
**Acceptance Criteria:** A first-time visitor can locate service information and a contact method within a few clicks/taps without confusion.

### NFR-003 — Accessibility
**Description:** The website shall follow basic accessibility practices to accommodate users with visual or motor impairments.
**Priority:** Medium
**Acceptance Criteria:** Alt text, sufficient color contrast, and keyboard navigability are present as defined in FR-011.

### NFR-004 — Security
**Description:** The website shall avoid collecting or storing sensitive customer data, since no database exists in v1.
**Priority:** High
**Acceptance Criteria:** No forms collect personal, payment, or identity information; all contact happens through external, already-secured messaging apps.

### NFR-005 — Privacy
**Description:** The website shall not track or store personal visitor data beyond standard, privacy-respecting analytics if used.
**Priority:** Medium
**Acceptance Criteria:** No personal data is captured directly by the website; any analytics tool used discloses its purpose if added.

### NFR-006 — Reliability
**Description:** The website shall remain accessible and functional without requiring ongoing server maintenance.
**Priority:** High
**Acceptance Criteria:** The site remains available via free static hosting with minimal to no downtime under normal conditions.

### NFR-007 — Maintainability
**Description:** The website's structure and content shall be simple enough for future updates without specialized tools.
**Priority:** High
**Acceptance Criteria:** Content (text, services, contact links) can be updated by editing static files directly, without requiring a database or backend.

### NFR-008 — Scalability
**Description:** The website's structure shall allow future addition of features (e.g., booking forms, admin dashboard) without a full rebuild.
**Priority:** Medium
**Acceptance Criteria:** Pages and code are organized in a way that new sections or features can be added incrementally in later versions.

### NFR-009 — Browser Compatibility
**Description:** The website shall function correctly on major modern web browsers.
**Priority:** High
**Acceptance Criteria:** Site displays and functions correctly on the latest versions of Chrome, Safari, Firefox, and Edge.

### NFR-010 — Mobile Responsiveness
**Description:** The website shall adapt its layout to different screen sizes, prioritizing mobile devices.
**Priority:** High
**Acceptance Criteria:** All pages display correctly and remain fully usable on common mobile screen widths as well as tablet and desktop widths.

### NFR-011 — SEO
**Description:** The website shall be structured to support discoverability through search engines.
**Priority:** Medium
**Acceptance Criteria:** Meets the SEO-related acceptance criteria defined in FR-012.

---

# 5. External Interface Requirements

## User Interface Requirements
- The interface shall use a consistent visual style (colors, fonts, spacing) across all pages.
- Navigation shall be consistent in placement and behavior across all pages.
- Contact buttons shall use recognizable icons or labels for each channel (phone, Messenger, Viber, WhatsApp, Telegram).

## Communication Interface Requirements
- Phone contact links shall use a standard dialer-triggering format where supported by the visitor's device.
- Messenger, Viber, WhatsApp, and Telegram links shall direct the visitor to the correct chat interface or app for that platform.
- No direct data submission (e.g., forms posting to a server) is required, since all communication is routed through external messaging platforms.

## Browser Compatibility
- The site shall be tested and function correctly on the latest versions of Chrome, Safari, Firefox, and Edge, per NFR-009.

## Device Compatibility
- The site shall function correctly on smartphones, tablets, and desktop computers, per NFR-010.

---

# 6. Content Requirements

## Homepage
- Business name and slogan ("8-in-1 Ticketing System") with brief explanation
- Short introductory description of the business
- Summary or preview of the 8 services
- Primary CTA(s) linking to Services and Contact

## About
- Business background and description
- Explanation of the business's role as a facilitator/assistance provider
- Trust-building content (e.g., years of operation, service philosophy) — to be confirmed with the business owner before publishing

## Services
- Individual entries for all 8 services, each with a short description of the assistance provided
- CTA per service directing to an inquiry channel

## Tour Packages
- General presentation of tour package categories or examples
- Clear indication that details are provided upon inquiry, not fixed or real-time
- CTA for inquiries

## FAQs
- Explanation of the "8-in-1 Ticketing System" slogan
- How to make an inquiry and through which channels
- Clarification that the site does not process bookings or payments directly
- Other common questions as identified by the business owner

## Contact
- Phone number
- Messenger, Viber, WhatsApp, and Telegram links/buttons
- Optional: business hours or availability notes, if confirmed by the owner

## Footer
- Business name
- Condensed contact links
- Copyright/year notice
- Optional: link back to key pages (Services, Contact)

## Call-to-Action
- Consistent CTA wording (e.g., "Inquire Now," "Message Us") used across Homepage, Services, and Tour Packages pages
- CTA wording shall avoid implying booking, payment, or confirmation capability on the website itself

---

# 7. Business Rules

### BR-001
The website serves as the official business website for Homeland Travel and Tours – GBM Prestige Ticketing.

### BR-002
All customer inquiries generated through the website shall be handled through the business's existing communication channels (phone, Messenger, Viber, WhatsApp, Telegram).

### BR-003
Service descriptions shall accurately describe the assistance provided and shall not overstate the business's role or capabilities.

### BR-004
The website shall not imply ownership of, or authority over, third-party transportation providers, hotels, tour operators, or government agencies.

### BR-005
The website shall clearly explain that "8-in-1 Ticketing System" is a marketing term representing 8 categories of assisted services, not a software or booking system.

### BR-006
The website shall not promise real-time availability, fixed pricing, or instant confirmation for any service.

### BR-007
Visa, passport, and other government-related content shall be described in general terms to avoid misrepresenting requirements that may change over time.

---

# 8. Constraints

- Zero development budget: the site shall be built using free tools and hosted on free static hosting.
- No backend, server-side processing, or database in v1.
- No online booking or payment functionality in v1.
- No admin dashboard or customer portal in v1.
- No real-time ticket, hotel, or pricing data in v1.
- All transaction processing continues manually, outside the website, through existing communication channels.
- Content describing visa/passport and similar services must remain general to avoid becoming outdated.

---

# 9. Acceptance Criteria

The website shall be considered acceptable for v1 launch when:
1. All functional requirements (FR-001 to FR-013) are implemented and verifiable.
2. All non-functional requirements (NFR-001 to NFR-011) are met to a reasonable degree appropriate for a zero-budget static site.
3. All required pages (Homepage, About, Services, Tour Packages, FAQs, Contact) are complete, linked, and free of broken navigation.
4. All contact buttons/links function correctly across major browsers and devices.
5. The "8-in-1 Ticketing System" slogan is clearly explained on at least the Homepage and FAQs page.
6. No content implies booking, payment processing, real-time availability, or ownership of third-party services, consistent with BR-004 and BR-006.
7. The site displays and functions correctly on both mobile and desktop screen sizes.
8. The site contains no forms or mechanisms that collect or store personal customer data.

---

# 10. Summary

This System Requirements Specification defines the functional and non-functional requirements for v1 of the Homeland Travel and Tours – GBM Prestige Ticketing website, translating the business needs identified in the Research Foundation and Business Analysis documents into concrete, testable requirements. The specification covers six core pages (Homepage, About, Services, Tour Packages, FAQs, Contact), supporting navigation and contact features, and quality attributes such as performance, accessibility, and mobile responsiveness — while explicitly excluding booking, payment, database, and administrative functionality reserved for future versions. Together with the business rules and acceptance criteria defined here, this document provides the foundation for the next stage of project documentation and for development work in VS Code.

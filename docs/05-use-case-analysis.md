# Deliverable 05: Use Case Analysis
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document identifies how users interact with the website to achieve their goals. It builds on the approved Research Foundation, Business Analysis, SRS, and Functional & Non-Functional Requirements to describe the specific actions different users take on the site, and how the website supports those actions within the scope of a static, zero-budget, inquiry-focused business website.

---

# 2. Use Case Analysis Overview

A use case shows what a user wants to do on the website and how the website helps them do it. Each use case describes a goal-oriented action — such as browsing services or contacting the business — along with the steps involved and the outcome. Since this is a static site with no accounts, forms, or transactions, all use cases in this document are informational or navigational in nature.

---

# 3. Actors

### Actor: Website Visitor / Potential Customer
- **Description:** A first-time visitor exploring the site to learn about the business before deciding to reach out.
- **Goals:** Understand what the business offers, confirm it is trustworthy, and find a way to make contact.
- **Relationship to the Website:** Primary consumer of homepage, About, Services, Tour Packages, and FAQ content; initiates contact through provided channels.

### Actor: Existing Customer
- **Description:** A previous or repeat customer returning to the site for quick reference or to re-initiate contact.
- **Goals:** Quickly confirm service details or find the fastest way to reach the business again.
- **Relationship to the Website:** Uses the site as a quick-reference tool rather than for first-time discovery; relies heavily on Contact page and contact buttons.

### Actor: Business Owner / Staff
- **Description:** The person(s) representing the business who receive and respond to inquiries generated through the website.
- **Goals:** Receive clear, well-informed inquiries through existing channels; reduce repetitive basic questions.
- **Relationship to the Website:** Indirect actor — does not use the website as an interactive system (no admin dashboard exists in v1), but is the end recipient of all inquiries the site generates.

### Actor: Search Engine Crawler
- **Description:** An automated agent (e.g., Googlebot) that indexes the website's pages for search engine results.
- **Goals:** Read and interpret page content, titles, and structure to determine how the site should appear in search results.
- **Relationship to the Website:** Interacts only with the site's static content and metadata (titles, descriptions, headings); does not interact with contact buttons or navigation the way a human visitor does.

---

# 4. Use Case List

| Use Case ID | Use Case Name | Primary Actor | Goal | Priority | Related Functional Requirement |
|---|---|---|---|---|---|
| UC-01 | View Homepage | Website Visitor / Potential Customer | Get an overview of the business and its services | High | FR-001 |
| UC-02 | Learn About the Business | Website Visitor / Potential Customer | Understand business background and build trust | High | FR-002 |
| UC-03 | Browse Services | Website Visitor / Potential Customer | Understand the 8 services offered | High | FR-003 |
| UC-04 | View Tour Packages | Website Visitor / Potential Customer | See general tour package options | Medium | FR-004 |
| UC-05 | Read FAQs | Website Visitor / Potential Customer | Get quick answers, including what "8-in-1" means | High | FR-005 |
| UC-06 | Contact the Business | Website Visitor / Existing Customer | Reach the business to make an inquiry | High | FR-006, FR-010 |
| UC-07 | Use Contact Buttons | Website Visitor / Existing Customer | Quickly initiate contact via a preferred channel | High | FR-009 |
| UC-08 | Navigate the Website | Website Visitor / Existing Customer | Move between pages easily | High | FR-007 |
| UC-09 | Use Mobile Navigation | Website Visitor / Existing Customer | Access the menu on a small screen | High | FR-008 |
| UC-10 | Access the Website on Mobile | Website Visitor / Existing Customer | View and use the site comfortably on a phone | High | FR-008, NFR-010 |
| UC-11 | Find the Website Through Search Engines | Search Engine Crawler | Index the site so it appears in search results | Medium | FR-012 |
| UC-12 | Handle Invalid Page or Broken Link | Website Visitor / Existing Customer | Recover gracefully from a broken or mistyped link | Medium | FR-013 |

---

# 5. Detailed Use Case Descriptions

### UC-01: View Homepage
- **Primary Actor:** Website Visitor / Potential Customer
- **Supporting Actor:** None
- **Goal:** Get a quick overview of the business, its slogan, and its services.
- **Preconditions:** Visitor has a working internet connection and a browser.
- **Trigger:** Visitor opens the website's root URL.
- **Main Flow:**
  1. Visitor lands on the homepage.
  2. Visitor sees the business name, "8-in-1 Ticketing System" slogan with explanation, and a services summary.
  3. Visitor sees links/CTAs to Services and Contact.
- **Alternative Flow:** If the visitor is unsure what "8-in-1" means, they can proceed to the FAQs page for a fuller explanation (UC-05).
- **Postconditions:** Visitor understands the business's purpose and knows where to go next.
- **Related Requirements:** FR-001, NFR-001, NFR-002.

### UC-02: Learn About the Business
- **Primary Actor:** Website Visitor / Potential Customer
- **Supporting Actor:** None
- **Goal:** Build trust and confirm the business is legitimate before contacting it.
- **Preconditions:** Visitor navigates to the About page.
- **Trigger:** Visitor clicks "About" in the navigation.
- **Main Flow:**
  1. Visitor opens the About page.
  2. Visitor reads business background and description.
  3. Visitor forms an impression of the business's credibility.
- **Alternative Flow:** None identified for a static informational page.
- **Postconditions:** Visitor has a clearer understanding of who the business is.
- **Related Requirements:** FR-002, NFR-002.
- **Note:** Specific trust-building details (e.g., years in operation) depend on future owner confirmation.

### UC-03: Browse Services
- **Primary Actor:** Website Visitor / Potential Customer
- **Supporting Actor:** None
- **Goal:** Understand what each of the 8 services covers.
- **Preconditions:** Visitor navigates to the Services page.
- **Trigger:** Visitor clicks "Services" in the navigation or a CTA from the homepage.
- **Main Flow:**
  1. Visitor opens the Services page.
  2. Visitor reads through all 8 service descriptions.
  3. Visitor identifies the service relevant to their need.
  4. Visitor uses the inquiry CTA next to that service.
- **Alternative Flow:** If the visitor is interested in tour packages specifically, they may proceed to the Tour Packages page (UC-04) for more detail.
- **Postconditions:** Visitor understands available services and has a clear next step.
- **Related Requirements:** FR-003, FR-010, NFR-002.

### UC-04: View Tour Packages
- **Primary Actor:** Website Visitor / Potential Customer
- **Supporting Actor:** None
- **Goal:** See general tour package categories or examples.
- **Preconditions:** Visitor navigates to the Tour Packages page.
- **Trigger:** Visitor clicks "Tour Packages" in the navigation or from the Services page.
- **Main Flow:**
  1. Visitor opens the Tour Packages page.
  2. Visitor reviews general package categories or examples.
  3. Visitor uses the inquiry CTA for more details.
- **Alternative Flow:** None — real-time pricing/availability is explicitly out of scope, so no "check availability" flow exists.
- **Postconditions:** Visitor understands general tour offerings and knows to inquire for specifics.
- **Related Requirements:** FR-004, BR-006.
- **Note:** Actual package names/pricing shown depend on future owner confirmation.

### UC-05: Read FAQs
- **Primary Actor:** Website Visitor / Potential Customer
- **Supporting Actor:** None
- **Goal:** Get quick answers to common questions, especially about the "8-in-1" slogan.
- **Preconditions:** Visitor navigates to the FAQs page.
- **Trigger:** Visitor clicks "FAQs" in the navigation.
- **Main Flow:**
  1. Visitor opens the FAQs page.
  2. Visitor reads the explanation of "8-in-1 Ticketing System."
  3. Visitor reads other common questions (how to inquire, what the site does not handle).
- **Alternative Flow:** If the visitor's question isn't listed, they proceed directly to Contact (UC-06).
- **Postconditions:** Visitor's basic questions are answered without needing to message the business first.
- **Related Requirements:** FR-005, BR-005, BR-006.

### UC-06: Contact the Business
- **Primary Actor:** Website Visitor / Existing Customer
- **Supporting Actor:** Business Owner / Staff (receives the inquiry)
- **Goal:** Reach the business to ask about or request a service.
- **Preconditions:** Visitor has identified a service of interest or has a general question.
- **Trigger:** Visitor clicks a CTA or visits the Contact page.
- **Main Flow:**
  1. Visitor opens the Contact page or clicks a CTA elsewhere on the site.
  2. Visitor selects a preferred contact method (phone, Messenger, Viber, WhatsApp, Telegram).
  3. Visitor is directed to that app or dialer to start the conversation.
  4. Business Owner/Staff receives and responds to the inquiry outside the website.
- **Alternative Flow:** If a visitor's chosen app isn't installed on their device, they can choose a different listed channel instead.
- **Postconditions:** An inquiry is initiated through an existing communication channel; the website's role ends here.
- **Related Requirements:** FR-006, FR-009, FR-010, BR-002.

### UC-07: Use Contact Buttons
- **Primary Actor:** Website Visitor / Existing Customer
- **Supporting Actor:** None
- **Goal:** Quickly initiate contact without navigating to the Contact page first.
- **Preconditions:** Visitor is on a page that includes contact buttons (Homepage, Services, Tour Packages).
- **Trigger:** Visitor clicks a contact button while reading page content.
- **Main Flow:**
  1. Visitor sees a contact button next to relevant content.
  2. Visitor clicks/taps the button.
  3. The corresponding app or dialer opens.
- **Alternative Flow:** None — this is a direct-action use case.
- **Postconditions:** Visitor is connected to their preferred contact channel.
- **Related Requirements:** FR-009.

### UC-08: Navigate the Website
- **Primary Actor:** Website Visitor / Existing Customer
- **Supporting Actor:** None
- **Goal:** Move between pages to find needed information.
- **Preconditions:** Visitor is on any page of the site.
- **Trigger:** Visitor clicks a navigation link.
- **Main Flow:**
  1. Visitor views the navigation menu.
  2. Visitor selects a destination page (Home, About, Services, Tour Packages, FAQs, Contact).
  3. The selected page loads.
- **Alternative Flow:** If the visitor clicks an invalid or broken link, the flow proceeds to UC-12.
- **Postconditions:** Visitor reaches the intended page.
- **Related Requirements:** FR-007.

### UC-09: Use Mobile Navigation
- **Primary Actor:** Website Visitor / Existing Customer
- **Supporting Actor:** None
- **Goal:** Access the navigation menu comfortably on a small screen.
- **Preconditions:** Visitor is using a mobile device or narrow browser window.
- **Trigger:** Visitor taps the mobile menu toggle (e.g., hamburger icon).
- **Main Flow:**
  1. Visitor taps the menu toggle.
  2. The navigation menu expands.
  3. Visitor selects a page link.
  4. The menu collapses and the selected page loads.
- **Alternative Flow:** None identified.
- **Postconditions:** Visitor reaches the intended page via the mobile-friendly menu.
- **Related Requirements:** FR-008.

### UC-10: Access the Website on Mobile
- **Primary Actor:** Website Visitor / Existing Customer
- **Supporting Actor:** None
- **Goal:** View and use the entire site comfortably on a phone.
- **Preconditions:** Visitor opens the site on a mobile browser.
- **Trigger:** Visitor navigates to the site URL on a mobile device.
- **Main Flow:**
  1. Site layout adjusts to the mobile screen width.
  2. Text, images, buttons, and navigation remain readable and usable without zooming or horizontal scrolling.
  3. Visitor completes their intended action (browsing or contacting).
- **Alternative Flow:** None — this use case describes the overall mobile experience across all pages.
- **Postconditions:** Visitor has a fully functional experience on mobile.
- **Related Requirements:** FR-008, NFR-010.

### UC-11: Find the Website Through Search Engines
- **Primary Actor:** Search Engine Crawler
- **Supporting Actor:** Website Visitor / Potential Customer (benefits indirectly)
- **Goal:** Index the site's pages so they can appear in relevant search results.
- **Preconditions:** The website is published and publicly accessible.
- **Trigger:** A search engine crawler visits the site.
- **Main Flow:**
  1. Crawler reads page titles, meta descriptions, and heading structure.
  2. Crawler indexes the content for relevant search terms.
  3. The site becomes discoverable to users searching for related terms.
- **Alternative Flow:** None — this is an automated, non-interactive process.
- **Postconditions:** The site is indexed and discoverable through search engines.
- **Related Requirements:** FR-012, NFR-011.

### UC-12: Handle Invalid Page or Broken Link
- **Primary Actor:** Website Visitor / Existing Customer
- **Supporting Actor:** None
- **Goal:** Recover gracefully after clicking a broken link or mistyping a URL.
- **Preconditions:** Visitor accesses a URL that does not correspond to an existing page.
- **Trigger:** Visitor navigates to an invalid or outdated link.
- **Main Flow:**
  1. The system displays a custom "page not found" message.
  2. The message includes a link back to the homepage.
  3. Visitor clicks the link and returns to a working page.
- **Alternative Flow:** None identified.
- **Postconditions:** Visitor is redirected back into the working site instead of reaching a dead end.
- **Related Requirements:** FR-013.

---

# 6. Use Case Diagram Description

Since no image is created, the relationships between actors and use cases are described below:

- **Website Visitor / Potential Customer** connects to: View Homepage (UC-01), Learn About the Business (UC-02), Browse Services (UC-03), View Tour Packages (UC-04), Read FAQs (UC-05), Contact the Business (UC-06), Use Contact Buttons (UC-07), Navigate the Website (UC-08), Use Mobile Navigation (UC-09), Access the Website on Mobile (UC-10).
- **Existing Customer** connects to: Contact the Business (UC-06), Use Contact Buttons (UC-07), Navigate the Website (UC-08), Use Mobile Navigation (UC-09), Access the Website on Mobile (UC-10), Handle Invalid Page or Broken Link (UC-12).
- **Business Owner / Staff** connects to: Contact the Business (UC-06) as a supporting actor — receiving inquiries generated by the Website Visitor or Existing Customer, but not interacting with the website system directly.
- **Search Engine Crawler** connects to: Find the Website Through Search Engines (UC-11) only.

All use cases ultimately support two connected outcomes: helping a visitor understand the business (UC-01 to UC-05) and helping a visitor successfully make contact (UC-06 to UC-10), with UC-11 and UC-12 supporting discoverability and reliability around the edges of that experience.

---

# 7. Scope Boundaries

The use cases in this document deliberately exclude the following, consistent with the approved SRS and Functional & Non-Functional Requirements:
- User registration
- Login
- Booking confirmation
- Online payment
- Inquiry form submission
- Database storage
- Admin management

No use case in this document depends on any of the above. All contact-related use cases (UC-06, UC-07) end at the point where the visitor is handed off to an external messaging app or phone call — the website itself does not process, store, or confirm anything beyond that handoff.

---

# 8. Use Case Traceability Matrix

| Use Case ID | Related Functional Requirement | Related Non-Functional Requirement | Supported Project Goal |
|---|---|---|---|
| UC-01 | FR-001 | NFR-001, NFR-002 | Increase business credibility |
| UC-02 | FR-002 | NFR-002 | Increase business credibility |
| UC-03 | FR-003, FR-010 | NFR-002 | Showcase services clearly |
| UC-04 | FR-004 | NFR-002 | Showcase services clearly |
| UC-05 | FR-005 | NFR-002 | Showcase services clearly |
| UC-06 | FR-006, FR-009, FR-010 | NFR-002 | Generate customer inquiries |
| UC-07 | FR-009 | NFR-002 | Make it easier to contact the business |
| UC-08 | FR-007 | NFR-002 | Make it easier to contact the business |
| UC-09 | FR-008 | NFR-010 | Make it easier to contact the business |
| UC-10 | FR-008 | NFR-010 | Make it easier to contact the business |
| UC-11 | FR-012 | NFR-011 | Improve online visibility |
| UC-12 | FR-013 | NFR-006 | Provide a professional, trustworthy experience |

---

# 9. Implementation Notes for Future VS Code Development

- Pages must support the identified visitor actions — each page built in VS Code should map directly to one or more use cases above (e.g., the Services page must support UC-03).
- CTAs must match the use cases — CTA wording and placement should reflect the specific goal of the use case they support (e.g., "Inquire Now" for UC-06/UC-07, not booking or payment language).
- Navigation must support both desktop and mobile users, satisfying UC-08, UC-09, and UC-10 together.
- Contact buttons must work across devices where possible, so that UC-07 functions consistently whether the visitor is on mobile or desktop.
- No feature should be added unless it supports one of the approved use cases above — this keeps development aligned with the static, zero-budget, inquiry-focused scope and prevents scope creep into booking, payment, or account-based features.

---

# 10. Summary

This Use Case Analysis identifies four actors — Website Visitor/Potential Customer, Existing Customer, Business Owner/Staff, and Search Engine Crawler — and defines 12 use cases covering how each interacts with the v1 website. All use cases center on two outcomes: helping visitors understand the business and its services, and helping them successfully reach the business through existing communication channels. The document confirms that no use case depends on registration, login, bookings, payments, forms, or database storage, keeping the analysis fully aligned with the approved Research Foundation, Business Analysis, SRS, and Functional & Non-Functional Requirements documents. This analysis is now ready to guide page design, CTA placement, and navigation behavior in future VS Code development.

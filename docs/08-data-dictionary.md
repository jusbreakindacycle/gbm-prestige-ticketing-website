# Deliverable 08: Data Dictionary
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document defines the data/content elements used across the website. It lists the pieces of information — business identity details, service descriptions, contact details, page content, and SEO metadata — that must be defined consistently before and during development, so that naming and meaning stay the same across every page.

---

# 2. Data Dictionary Overview

A data dictionary is a list of important information items used in the website, so naming and meaning stay consistent. In this document, each item is a piece of static content (text, links, or labels) that appears on the site — not a database field, since v1 has no database.

---

# 3. Data Scope

- v1 has no database.
- v1 does not store customer data.
- v1 only uses static content data — text, links, and labels written directly into the website's pages.
- Future versions may require a database (e.g., to support inquiry tracking or an admin dashboard), but that is outside the scope of v1 and is not defined in this document.

---

# 4. Website Identity Data Elements

| Data Element | Description | Example / Placeholder | Source / Confirmation Needed | Used In |
|---|---|---|---|---|
| Business Name | Full legal/operating name of the business | Homeland Travel and Tours – GBM Prestige Ticketing | Confirmed (Research Foundation) | Homepage, About, Footer, page titles |
| Business Short Name | Shortened version for tight spaces (e.g., mobile header) | Homeland Travel and Tours | Owner confirmation needed | Header, Footer, mobile navigation |
| Business Description | Short paragraph explaining what the business does | "We assist customers with travel and everyday transaction needs, including ticketing, bookings, visa/passport processing, bills payment, and e-loading." | Owner confirmation needed for final wording | Homepage, About |
| Slogan | Marketing slogan used by the business | 8-in-1 Ticketing System | Confirmed (Research Foundation) | Homepage, FAQs, About |
| Logo | Business logo image | [Placeholder – logo file not provided] | Owner confirmation/upload needed | Header, Footer |
| Brand Tagline | Optional short phrase supporting the slogan | [Placeholder – e.g., "Your One-Stop Travel and Transaction Assistant"] | Owner confirmation needed | Homepage, meta description |

---

# 5. Service Data Elements

| Service ID | Service Name | Service Category | Service Description | Important Notes | CTA Label | Used In |
|---|---|---|---|---|---|---|
| SV-01 | Airline Ticketing Assistance | Travel | Assistance with processing airline ticket requests. | Describe as assistance, not direct airline ownership (BR-007, BR-008). | Inquire Now | Homepage, Services |
| SV-02 | Ferry Ticketing Assistance | Travel | Assistance with processing ferry ticket requests. | Same as above; no real-time schedule/availability implied (BR-010, BR-012). | Inquire Now | Homepage, Services |
| SV-03 | Bus Ticketing Assistance | Travel | Assistance with processing bus ticket requests. | Same as above. | Inquire Now | Homepage, Services |
| SV-04 | Hotel Booking Assistance | Travel | Assistance with arranging hotel bookings. | No guaranteed pricing/availability (BR-010). | Inquire Now | Homepage, Services |
| SV-05 | Tour Packages | Travel | Assistance with arranging tour packages for local or international travel. | General categories/examples only; specifics require owner confirmation. | Inquire Now | Homepage, Services, Tour Packages |
| SV-06 | Visa and Passport Processing Assistance | Travel/Government | Assistance with preparing and processing visa and passport requirements. | Content must remain general per BR-009; no specific country requirements unless confirmed. | Inquire Now | Homepage, Services, FAQs |
| SV-07 | Bills Payment | Everyday Errand | Assistance with paying bills through the business. | Describe as assistance/facilitation, not a payment platform owned by the business (BR-003, BR-007). | Inquire Now | Homepage, Services |
| SV-08 | E-Loading | Everyday Errand | Assistance with mobile load top-ups. | Same as above. | Inquire Now | Homepage, Services |

---

# 6. Contact Data Elements

| Contact Element | Description | Format | Confirmation Needed | Used In |
|---|---|---|---|---|
| Phone Number | Primary business phone number | Standard phone number format (e.g., +63 9XX XXX XXXX) | Owner confirmation needed | Contact, Homepage, Services, Tour Packages, Footer |
| Messenger Link | Direct link to the business's Messenger chat | Facebook Messenger URL (e.g., m.me/[pagehandle]) | Owner confirmation needed (exact page handle) | Contact, Homepage, Services, Tour Packages |
| Viber Link | Direct link or number for Viber contact | Viber chat URL or phone number | Owner confirmation needed | Contact, Homepage, Services, Tour Packages |
| WhatsApp Link | Direct link for WhatsApp contact | WhatsApp chat URL (e.g., wa.me/[number]) | Owner confirmation needed | Contact, Homepage, Services, Tour Packages |
| Telegram Link | Direct link for Telegram contact | Telegram URL (e.g., t.me/[username]) | Owner confirmation needed | Contact, Homepage, Services, Tour Packages |
| Facebook Page Link | URL of the business's existing Facebook Page | Facebook Page URL | Owner confirmation needed | Footer, About, Contact |
| Business Hours | Days/times the business is available to respond | e.g., "Monday–Saturday, 9:00 AM–6:00 PM" | Owner confirmation needed | Contact, Footer |
| Business Address | Physical address, if the business has a public office | [Placeholder – address not provided] | Owner confirmation needed (include only if the owner wants it public) | Contact, About, Footer |

---

# 7. Page Content Data Elements

| Page | Content Element | Description | Required or Optional | Confirmation Needed |
|---|---|---|---|---|
| Homepage | Business Name, Slogan, Short Description | Introduces the business at a glance | Required | Business Description wording |
| Homepage | Services Summary | Brief preview of the 8 services | Required | — |
| Homepage | Primary CTA | Links to Services and Contact | Required | — |
| About | Business Background | Fuller description of the business's history and purpose | Required | Owner confirmation needed |
| About | Trust-Building Content | Optional credibility details (e.g., years of experience) | Optional | Owner confirmation needed |
| Services | 8 Service Entries | Full list with descriptions, per Section 5 | Required | Per-service notes above |
| Tour Packages | Package Categories/Examples | General tour package information | Required | Owner confirmation needed |
| FAQs | Question and Answer Pairs | Including "8-in-1" explanation and inquiry process | Required | Additional FAQs owner may want to add |
| Contact | Contact Details | All items from Section 6 | Required | Per contact element above |
| Footer | Business Name, Condensed Contact Links, Copyright Notice | Repeated identity and contact info sitewide | Required | Copyright year |

---

# 8. SEO Data Elements

| Page | Title Tag | Meta Description | Keywords / Topic Focus | Confirmation Needed |
|---|---|---|---|---|
| Homepage | Homeland Travel and Tours – GBM Prestige Ticketing \| 8-in-1 Ticketing Assistance | Short summary of the business and its 8 assisted services, with a call to inquire. | travel ticketing assistance, 8-in-1 ticketing, Homeland Travel and Tours | Owner confirmation on final wording |
| About | About Us \| Homeland Travel and Tours – GBM Prestige Ticketing | Brief description of the business's background and mission. | about Homeland Travel and Tours, travel assistance business | Owner confirmation on background details |
| Services | Our Services \| Homeland Travel and Tours – GBM Prestige Ticketing | Overview of all 8 assisted services offered. | airline ticketing assistance, ferry ticketing, bus ticketing, hotel booking, visa passport assistance | — |
| Tour Packages | Tour Packages \| Homeland Travel and Tours – GBM Prestige Ticketing | General overview of tour package assistance offered. | tour packages assistance, travel packages | Owner confirmation on package examples |
| FAQs | FAQs \| Homeland Travel and Tours – GBM Prestige Ticketing | Answers to common questions, including what "8-in-1 Ticketing System" means. | 8-in-1 ticketing meaning, ticketing assistance FAQ | — |
| Contact | Contact Us \| Homeland Travel and Tours – GBM Prestige Ticketing | Ways to reach the business via phone, Messenger, Viber, WhatsApp, or Telegram. | contact Homeland Travel and Tours, ticketing assistance contact | Owner confirmation on business hours/address |

---

# 9. Placeholder and Owner-Confirmation Items

The following content must be confirmed by the business owner before final website copy is published:
- Business Short Name (exact preferred short form)
- Final wording of the Business Description
- Logo file (upload needed)
- Brand Tagline (if the owner wants one beyond the slogan)
- About page background/history details
- Trust-building content for the About page (e.g., years of operation)
- Tour Package category names/examples
- Phone number (confirmed active line)
- Messenger, Viber, WhatsApp, and Telegram exact links/handles
- Facebook Page link
- Business Hours
- Business Address (and whether it should be made public)
- Any additional FAQs the owner wants included
- Final SEO title/meta description wording, if the owner wants adjustments

---

# 10. Excluded Data Elements

The following data is not collected or stored in v1, consistent with the approved scope:
- Customer name
- Email
- Passenger details
- Payment information
- Government ID details
- Uploaded documents
- Booking records
- Account credentials

None of these items appear anywhere in this Data Dictionary, since v1 has no forms, database, or storage mechanism to hold them.

---

# 11. Summary

This Data Dictionary defines the static content data elements used across the v1 website: business identity details, all 8 services, contact information, page-level content, and SEO metadata. It confirms that v1 uses no database and stores no customer data, listing only the content that must be written into the site's static pages. A consolidated list of owner-confirmation items (Section 9) and explicitly excluded data (Section 10) ensures development in VS Code proceeds with clear, consistent content while keeping the project fully aligned with its static, zero-budget, inquiry-focused scope.

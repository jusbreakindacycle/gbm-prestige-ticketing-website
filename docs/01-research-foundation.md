# Research Foundation Document
## Homeland Travel and Tours – GBM Prestige Ticketing Website 

> **Note on sourcing:** This document is based on the business screenshots reviewed in ChatGPT and the project details provided by the user. Any information not directly visible from the screenshots or stated by the user is labeled as [Assumption].

---

## 1. Project Title

**Homeland Travel and Tours – GBM Prestige Ticketing: Official Business Website**

*Subtitle for internal use:* A static, zero-budget informational website built to support the business's existing "8-in-1 Ticketing System" service offering.

---

## 2. Business Background

- The business currently operates as **Homeland Travel and Tours – GBM Prestige Ticketing**. *(From your description.)*
- It presently runs its public-facing operations through a **Facebook Page** and **direct messaging channels** (no website exists yet). *(From your description.)*
- The business markets itself using the slogan **"8-in-1 Ticketing System."** *(From your description — noted as taken from business screenshots you reviewed, not attached here.)*
- This slogan is **not** an actual software or booking platform — it is a marketing label describing eight (8) categories of assistance the business provides to customers. *(From your description — this is an important clarification you gave, and it should carry through into the website copy so visitors are not misled into expecting an online booking system.)*
- **[Assumption]** The business likely operates as a local travel and ticketing agency serving walk-in and online inquiry customers, common to small-to-medium ticketing agencies in the Philippines that partner with airlines, ferry lines, bus companies, and government processing services rather than owning their own booking infrastructure. *(This should be verified with the business owner, not treated as fact.)*

---

## 3. Business Description

Homeland Travel and Tours – GBM Prestige Ticketing is a **ticketing and travel assistance business** that helps customers process transactions they could otherwise struggle to book directly — such as flights, ferries, buses, hotels, tour packages, visa/passport paperwork, bill payments, and e-loading — by acting as a **facilitator/assistant**, not as the airline, ferry line, or government agency itself. *(This description is inferred directly from the 8 listed services you provided, not from an outside source.)*

**[Assumption]** The business likely earns through service/convenience fees on top of the ticket or transaction cost, which is a common model for ticketing agencies of this type. This should be confirmed with the owner before it is stated anywhere on the website.

---

## 4. Current Digital Presence

| Channel | Status | Source |
|---|---|---|
| Facebook Page | Active — primary public presence | From your description |
| Messenger | Active — inquiry channel | From your description |
| Viber | Active — inquiry channel | From your description |
| WhatsApp | Active — inquiry channel | From your description |
| Telegram | Active — inquiry channel | From your description |
| Website | **None currently exists** — this project creates the first one | From your description |
| Phone/Call | Active — inquiry channel | From your description |

**Implication for v1:** Because all current business transactions happen through chat and calls, the website's core job is to **feed these same channels**, not replace them.

---

## 5. Services Offered ("8-in-1 Ticketing System")

1. **Airline Ticketing Assistance**
2. **Ferry Ticketing Assistance**
3. **Bus Ticketing Assistance**
4. **Hotel Booking Assistance**
5. **Tour Packages**
6. **Visa and Passport Processing Assistance**
7. **Bills Payment**
8. **E-Loading**

*(All eight services are as provided by you, sourced from the business's own marketing material.)*

**[Assumption]** Each of these is likely presented on the website as a short description + "Inquire Now" call-to-action, rather than a live booking form, since v1 excludes booking systems.

---

## 6. Target Customers

Based only on the nature of the services listed, likely customer segments include: *(all items below are [Assumption], to be validated with the business owner)*

- **[Assumption]** Overseas Filipino Workers (OFWs) and their families needing flight/ferry tickets and visa/passport processing.
- **[Assumption]** Local travelers and tourists booking domestic trips, tour packages, or hotel stays.
- **[Assumption]** Walk-in customers who use the bills payment and e-loading services for everyday convenience (these two services suggest the business also serves a non-travel, everyday-errands customer base).
- **[Assumption]** Customers who are not comfortable navigating airline/ferry booking websites directly and prefer a human assistant.

This section should be revisited once actual customer data or the owner's input is available — it is currently a planning hypothesis, not a confirmed profile.

---

## 7. Problem Statement

Homeland Travel and Tours – GBM Prestige Ticketing currently has **no independent website**. *(From your description.)* This creates the following planning-level problems: *(reasoned from the facts above, not independently verified)*

- Customers must rely entirely on Facebook and direct messaging to learn what the business offers, which limits discoverability (e.g., the business does not appear in general web searches).
- New or first-time customers have no single, organized place to see all 8 services, business credibility signals, or contact options — they must scroll through Facebook posts or ask directly.
- The "8-in-1 Ticketing System" slogan, without explanation, risks being misunderstood as an actual online booking platform, when it is really a description of assisted services.
- There is no neutral, always-available reference point that works even when the page admin is offline or Facebook is inaccessible.

---

## 8. Project Rationale

A simple, informational business website addresses the problems above without overengineering the solution:

- It gives the business a **permanent, professional home online** that is independent of any single social media platform.
- It **clarifies the "8-in-1" concept** clearly so customers understand it means 8 categories of human-assisted service, not automated booking.
- It **centralizes trust-building content** (business description, services, contact options) in one place.
- It is **zero-cost and low-maintenance**, matching the business's current stage — no hosting fees, no database, no backend required for v1.
- It **directs all real transactions back to existing, working channels** (phone, Messenger, Viber, WhatsApp, Telegram), so no new operational risk is introduced.

---

## 9. Project Objectives

### General Objective
To design and develop a static, zero-budget public business website for Homeland Travel and Tours – GBM Prestige Ticketing using HTML, CSS, and JavaScript in VS Code, that presents the business, explains its 8 services, builds customer trust, and directs visitors to existing inquiry channels.

### Specific Objectives
1. To present clear business background and identity information (name, description, and legitimacy signals) to first-time visitors.
2. To explain each of the 8 services in simple, non-technical language so customers understand what assistance they can request.
3. To clarify that "8-in-1 Ticketing System" is a service label, not a software platform, avoiding customer confusion.
4. To provide clickable/tappable contact options for phone, Messenger, Viber, WhatsApp, and Telegram on every relevant page.
5. To build a mobile-responsive layout, since most inquiry traffic likely comes from phones. **[Assumption — reasonable given Messenger/Viber/WhatsApp reliance, but not confirmed with analytics]**
6. To keep the codebase simple (plain HTML/CSS/JS, no framework, no backend) so it can run on free static hosting.
7. To structure the code and folders in a way that allows v2 features (booking system, database, admin dashboard) to be added later without a full rebuild.

---

## 10. Scope of the Website (v1)

**Included:**
- Home / Landing page introducing the business
- About page (business background, mission/trust content)
- Services page explaining all 8 services individually
- Contact page / contact section with phone, Messenger, Viber, WhatsApp, Telegram links
- Simple navigation menu, footer, and responsive design
- Static content only — no live data, no user accounts

**Technology:**
- HTML, CSS, JavaScript
- Built and edited in VS Code
- No backend framework, no server-side code, no paid hosting required for v1

---

## 11. Limitations of v1

Explicitly **excluded** from this version, per your instructions:

- ❌ Booking system (no ability to reserve tickets/hotels on the site itself)
- ❌ Payment system (no online payment collection)
- ❌ Database (no storage of customer or transaction data)
- ❌ Admin dashboard (no backend management panel)
- ❌ Real-time ticket availability (no live seat/slot/price data)

All actual transactions remain manual, continuing through phone, Messenger, Viber, WhatsApp, or Telegram — the website's role is informational and referral-based only.

---

## 12. Expected Benefits

- **Credibility:** A dedicated website signals legitimacy beyond a Facebook Page alone. *(Reasoned expectation, not a measured outcome — no analytics exist yet to confirm impact.)*
- **Clarity:** Customers get a clear explanation of all 8 services and what "8-in-1" actually means, reducing repetitive basic questions sent to the page admin.
- **Accessibility:** The business becomes visible to people who search generally online, not just existing Facebook followers.
- **Low risk, low cost:** Zero hosting budget needed; no new technical liability (no database or payment system to secure or maintain).
- **Portfolio value:** As a real, client-usable static site, this also serves as a demonstrable project for professional/freelance presentation purposes.
- **Future-ready foundation:** Clean, simple code structure makes it easier to extend into v2 later.

---

## 13. Assumptions

Consolidated list of all assumptions used in this document (none are treated as fact and all should be validated with the business owner and the actual Facebook Page content before final copywriting):

1. The business earns via service/convenience fees on top of transaction costs (Section 3).
2. Primary customers likely include OFWs, local travelers, and walk-in errands customers (Section 6).
3. Most website traffic will be mobile (Section 9, Objective 5).
4. No existing website analytics or customer data currently exist to validate reach or behavior (implied throughout).
5. The business currently has no logo/brand guideline confirmed in this conversation — **[Assumption]** one may need to be requested from the owner or extracted from the Facebook Page.

---

## 14. Future Enhancements (Beyond v1)

Potential v2+ features, **not being built now**, but worth keeping in mind for folder/code structure decisions:

- Online booking request form (still human-processed, not automated)
- Admin dashboard for managing inquiries or content updates
- Database-backed customer inquiry tracking (e.g., simple CRM)
- Real-time or semi-real-time ticket/fare information (if a data source becomes available)
- Online payment integration (e.g., GCash, PayMaya, or bank transfer confirmation flow)
- Multi-language support (English/Filipino toggle)
- Customer testimonials or review system
- Blog/updates section for travel advisories, promos, or news

---

*Document prepared for planning purposes only. Sections 6, 9 (Objective 5), and 13 in particular should be reviewed against the actual Facebook Page and the business owner's confirmation before being used as final website copy.*

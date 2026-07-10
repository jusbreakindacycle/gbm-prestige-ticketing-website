# Deliverable 07: Business Rules
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document defines the business rules that control how the website should present information and guide customer expectations. These rules ensure the site accurately represents the business, stays within its approved scope, and does not create false expectations about bookings, payments, or third-party services.

---

# 2. Business Rules Overview

Business rules are rules the website must follow so it does not mislead customers or go beyond the business scope. They apply to content, wording, and presentation across every page, and act as guardrails that keep v1 focused on being an informational, inquiry-driven site rather than a transactional system.

---

# 3. Business Rule Categories

- Website Purpose Rules
- Service Description Rules
- Inquiry and Contact Rules
- Booking and Payment Rules
- Third-Party Service Rules
- Visa and Passport Assistance Rules
- Content Accuracy Rules
- Privacy and Data Rules
- Future Expansion Rules

---

# 4. Business Rules List

| Rule ID | Rule Name | Rule Statement | Priority | Reason | Related Requirement |
|---|---|---|---|---|---|
| BR-001 | Informational Purpose | The website is informational and inquiry-focused; it does not process transactions. | High | Sets correct visitor expectations from the start. | FR-001, BR-001 (SRS) |
| BR-002 | No Booking Processing | The website must not process bookings of any kind. | High | Prevents customers from expecting confirmed reservations from the site. | FR-004, Out-of-Scope (SRS) |
| BR-003 | No Payment Processing | The website must not process payments of any kind. | High | Avoids handling sensitive financial data with no backend to secure it. | NFR-004 |
| BR-004 | No Personal Data Collection | The website must not collect personal data through forms. | High | Protects visitor privacy and avoids the need for a database. | NFR-004, NFR-005 |
| BR-005 | Route Inquiries to Existing Channels | The website must route all inquiries to existing contact channels (phone, Messenger, Viber, WhatsApp, Telegram). | High | Keeps all actual transaction handling within the business's proven, working process. | FR-006, FR-009, BR-002 (SRS) |
| BR-006 | Explain the "8-in-1" Slogan | The website must clearly explain that "8-in-1 Ticketing System" is a marketing slogan representing 8 assisted services, not a software system. | High | Prevents visitors from mistaking the slogan for an automated booking platform. | FR-005, BR-005 (SRS) |
| BR-007 | Describe Services as Assistance | All service descriptions must describe the business's role as providing assistance, not direct issuance or ownership of the underlying service. | High | Accurately reflects the business's facilitator role. | FR-003, BR-003 (SRS) |
| BR-008 | No Implied Ownership of Third Parties | The website must not imply ownership of airlines, ferry operators, bus companies, hotels, tour operators, or government agencies. | High | Avoids misrepresenting the business's relationship with external providers. | BR-004 (SRS) |
| BR-009 | General Visa/Passport Content | Visa and passport content must remain general unless specific details are confirmed by the business owner. | High | Prevents publishing outdated or inaccurate government requirements. | BR-007 (SRS) |
| BR-010 | No Guaranteed Prices, Schedules, or Availability | Prices, schedules, availability, and package details must not be presented as guaranteed unless confirmed by the owner. | High | Prevents overpromising outcomes the business cannot control. | BR-006 (SRS) |
| BR-011 | Exclude Unverified Claims | All unverified claims must remain excluded from public website copy. | High | Maintains factual accuracy and protects business credibility. | Section 9, Business Analysis |
| BR-012 | No Real-Time Data Presentation | The website must not display or imply real-time ticket, hotel, or pricing availability. | High | Consistent with the static, non-database nature of v1. | Out-of-Scope (SRS) |
| BR-013 | Consistent Contact Information | Contact details displayed on the website must match the business's actual active channels at all times. | Medium | Prevents visitor frustration from outdated or incorrect contact information. | FR-006 |
| BR-014 | Scope-Limited Future Additions | Any future feature (e.g., booking, payment, admin dashboard) must be introduced only in a later version, not v1. | Medium | Preserves the zero-budget, static nature of the current release. | Out-of-Scope (SRS) |

---

# 5. Rule Explanations

### Website Purpose Rules
These rules (BR-001) establish the fundamental nature of the site: it exists to inform and generate inquiries, not to process transactions. This matters because it sets the tone and expectations for every other rule in this document — if visitors understand this from the start, later rules about bookings, payments, and data simply reinforce a boundary they already expect.

### Service Description Rules
These rules (BR-007) ensure that all 8 services are described accurately as assistance rather than as services the business owns or directly controls. This protects the business from claims of misrepresentation and keeps customer expectations aligned with what actually happens after they make an inquiry.

### Inquiry and Contact Rules
These rules (BR-005, BR-013) keep the website's role limited to directing visitors toward the business's existing, proven communication channels. Since v1 has no backend, all actual conversations and transactions must happen exactly as they do today — the rules ensure the website supports, rather than disrupts, this existing process.

### Booking and Payment Rules
These rules (BR-002, BR-003) protect both the business and its customers by ensuring no transaction-like expectation is created. Without a database or secure backend, attempting to process bookings or payments through the site would introduce real risk; these rules keep that risk out of scope entirely.

### Third-Party Service Rules
This rule (BR-008) protects the business from being seen as claiming authority it doesn't have over airlines, hotels, ferry operators, bus companies, tour operators, or government agencies. It also protects those third parties from being misrepresented.

### Visa and Passport Assistance Rules
This rule (BR-009) exists because visa and passport requirements change over time and vary by destination. Publishing specific, time-sensitive requirements risks becoming inaccurate; general language keeps the content both safe and accurate long-term.

### Content Accuracy Rules
These rules (BR-010, BR-011, BR-012) ensure the website only publishes what can be confirmed, and never states or implies guarantees the business cannot control (pricing, schedules, real-time availability). This protects credibility and avoids disputes from unmet expectations.

### Privacy and Data Rules
This rule (BR-004) keeps the site free of any mechanism that collects, stores, or transmits personal visitor data, which is consistent with the absence of a database or backend in v1 and avoids privacy or security obligations the project isn't equipped to handle.

### Future Expansion Rules
This rule (BR-014) keeps any discussion of future features (booking systems, payment processing, admin dashboards) clearly separated from v1 scope, so development stays focused and does not quietly expand beyond what was approved.

---

# 6. Business Rule Traceability Matrix

| Rule ID | Related Functional Requirement | Related Non-Functional Requirement | Related Risk Prevented |
|---|---|---|---|
| BR-001 | FR-001 | NFR-002 | Visitor confusion about the site's purpose |
| BR-002 | FR-004 | — | False expectation of confirmed bookings |
| BR-003 | — | NFR-004 | Handling of sensitive payment data without security infrastructure |
| BR-004 | — | NFR-004, NFR-005 | Privacy exposure from stored personal data |
| BR-005 | FR-006, FR-009 | NFR-002 | Inquiries getting lost without a clear channel |
| BR-006 | FR-005 | NFR-002 | Misunderstanding "8-in-1" as an automated system |
| BR-007 | FR-003 | — | Misrepresentation of the business's role |
| BR-008 | — | — | Misrepresentation of third-party relationships |
| BR-009 | FR-005 | — | Publishing outdated visa/passport requirements |
| BR-010 | FR-004 | — | Overpromising pricing, schedules, or availability |
| BR-011 | FR-002 | — | Loss of credibility from unverifiable claims |
| BR-012 | — | NFR-006 | False impression of real-time data capability |
| BR-013 | FR-006 | NFR-006 | Visitor frustration from outdated contact details |
| BR-014 | — | NFR-008 | Uncontrolled scope creep beyond v1 |

---

# 7. Out-of-Scope Rules

The following are not part of v1 and have no corresponding business rules in this document beyond their exclusion:
- No account creation
- No login
- No booking confirmation
- No online payment
- No database storage
- No admin management

Any business rule that would only make sense in the presence of these features (e.g., rules about account security or payment confirmation messaging) is intentionally absent, since these features do not exist in v1.

---

# 8. Implementation Notes for Future VS Code Development

- Every page's copy should be checked against the relevant business rules before being finalized in code — particularly BR-006 (explaining "8-in-1"), BR-007 (assistance language), and BR-010/BR-012 (no guarantees or real-time claims).
- CTA and button wording (e.g., "Inquire Now") must be reviewed to ensure it never implies booking confirmation or payment processing, per BR-002 and BR-003.
- No form elements should be added to any page that would collect personal data, per BR-004 — contact must always route through external apps/phone, per BR-005.
- Visa/passport and tour package content should be written in general terms during development, with a placeholder or comment noting where owner-confirmed specifics can be added later, per BR-009 and BR-010.
- Contact information hardcoded into the site (phone number, Messenger/Viber/WhatsApp/Telegram links) must be double-checked for accuracy before launch and kept easy to update, per BR-013.
- Any feature request that falls under the Out-of-Scope Rules (Section 7) should be deferred to a future version rather than implemented in v1, per BR-014.

---

# 9. Summary

This Business Rules document defines 14 rules across nine categories, covering the website's purpose, service descriptions, inquiry handling, booking/payment boundaries, third-party representation, visa/passport content, content accuracy, privacy, and future expansion. Each rule is traced to its related functional or non-functional requirement and the specific risk it prevents. Together, these rules ensure that v1 remains a static, zero-budget, inquiry-focused website that accurately represents Homeland Travel and Tours – GBM Prestige Ticketing without overstating its capabilities or creating false customer expectations. This document is ready to guide content writing and development decisions in VS Code.

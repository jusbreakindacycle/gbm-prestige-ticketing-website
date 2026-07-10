# Deliverable 15: API Design
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document evaluates whether an API is required for the approved v1 website. It confirms the correct architectural decision for v1 based on the already-approved scope, so that development in VS Code is not delayed by unnecessary backend or API design.

---

# 2. API Scope Decision

**No internal API is required for v1.**

This is based on the following, all consistent with the approved documents:
- The website is static — there is no server-side application to expose an API from.
- It does not collect customer data — there is nothing to send to or retrieve from a backend.
- It does not submit forms — no data submission process exists that would need an API.
- It does not process bookings — booking activity remains fully manual, outside the website.
- It does not process payments — no payment feature exists that would require a payment API.
- It does not require admin management — there is no admin dashboard or backend to authenticate against.

---

# 3. External Link-Based Communication

Instead of APIs, v1 uses simple external contact links to connect visitors with the business:
- **Phone dialer link** (`tel:`) — opens the device's dialer with the business's phone number.
- **Messenger link** (`m.me/`) — opens a chat with the business's Facebook Page in Messenger.
- **Viber link** — opens a Viber chat or call with the business.
- **WhatsApp link** (`wa.me/`) — opens a WhatsApp chat with the business's number.
- **Telegram link** (`t.me/`) — opens a Telegram chat with the business's account.
- **Facebook Page link**, if applicable — opens the business's existing Facebook Page.

These are plain hyperlinks, not API calls. Clicking one simply hands the visitor off to an external app or service that the business already uses — the website performs no processing of its own.

---

# 4. API Requirements Excluded from v1

The following API-related features are explicitly excluded from v1:
- Inquiry submission API
- Booking API
- Payment API
- Customer account API
- Admin login API
- Content management API
- File upload API

None of these are needed because v1 has no backend, no forms, and no admin system to support them.

---

# 5. Security and Privacy Implications

Not using APIs in v1 significantly reduces risk:
- **No customer data submission** — there is no data flowing from the visitor's browser to any server, so nothing can be intercepted or mishandled.
- **No authentication handling** — with no login system, there are no credentials to protect or attack.
- **No payment processing** — the website never touches financial data, removing a major security and compliance burden.
- **No server-side attack surface** — without a backend or API, there is no server-side code for an attacker to target.
- **Lower maintenance burden** — a static, API-free site requires no ongoing security patching, server monitoring, or API versioning.

---

# 6. Future API Considerations

**This section describes future scope only. None of the following applies to v1 and none of it should be implemented now.**

If the business later expands into inquiry management, admin tools, or online transactions, possible future API categories may include, at a high level only (no endpoint design):
- **Inquiry Submission API** — to accept and store inquiry details submitted through a future form.
- **Admin Authentication API** — to allow authorized staff to log into a future admin dashboard.
- **Tour Package Management API** — to let staff update tour package information dynamically.
- **Customer Inquiry Tracking API** — to track the status of inquiries over time.
- **Payment Confirmation API** — to confirm and record payments, if online payment is introduced.

These are conceptual placeholders only, meant to inform long-term planning — they are not part of v1 and must not be built now.

---

# 7. Recommendation

It is recommended that v1 remain fully API-free. External contact links are sufficient to meet all approved goals — connecting visitors to the business through its existing communication channels — without introducing the cost, complexity, and security responsibility of building and maintaining a backend API.

---

# 8. Summary

This document confirms that v1 of the Homeland Travel and Tours – GBM Prestige Ticketing website does not require an internal API. All visitor-to-business communication is handled through simple external contact links (phone, Messenger, Viber, WhatsApp, Telegram, Facebook), not through API calls. API-related features such as inquiry submission, booking, payment, admin login, and content management are explicitly excluded from v1, though conceptual API categories are noted for possible future versions. Keeping v1 API-free minimizes security risk, avoids unnecessary complexity, and matches the site's confirmed purpose as a static, inquiry-focused business website.

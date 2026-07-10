# Deliverable 09: Database Design / ERD
## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

---

# 1. Document Purpose

This document evaluates whether a database is required for the approved v1 scope. It reviews the approved requirements and confirms the correct database decision for v1, so that development in VS Code is not delayed or complicated by unnecessary backend design.

---

# 2. Database Scope Decision

**No database is required for v1.**

This is based on the following, all consistent with the approved documents:
- The website is static — all content is fixed text, links, and labels, not dynamically retrieved from a data source.
- It does not collect customer data — no forms exist that capture visitor information.
- It does not process bookings — all booking activity happens manually, outside the website.
- It does not process payments — no payment feature exists on the site.
- It does not provide admin management — there is no admin dashboard or backend to manage.
- All inquiries are handled through existing external communication channels (phone, Messenger, Viber, WhatsApp, Telegram), not through the website itself.

---

# 3. v1 Data Handling

v1 handles information entirely as static content, without any storage or retrieval system:
- **Static website content** — text describing the business, services, and FAQs, written directly into the site's pages.
- **Contact links** — phone number and Messenger/Viber/WhatsApp/Telegram links, hardcoded into the pages as defined in the Data Dictionary.
- **Service descriptions** — fixed descriptions for all 8 services, also defined in the Data Dictionary.
- **No stored customer records** — the website does not create, save, or manage any record of who visits the site or who makes an inquiry.

---

# 4. Database Requirements Excluded from v1

The following database-related features are explicitly excluded from v1:
- Customer table
- Inquiry table
- Booking table
- Payment table
- Admin user table
- Service transaction table
- Uploaded documents storage

None of these are needed because v1 has no mechanism to create, store, or retrieve this kind of data.

---

# 5. ERD Decision

No Entity-Relationship Diagram (ERD) is required for v1, because there are no database entities to define or relate. An ERD only becomes relevant once the project introduces data that must be stored and managed, which is outside the current approved scope.

---

# 6. Future Database Considerations

**This section describes future scope only. None of the following applies to v1 and none of it should be implemented now.**

If the business later expands into inquiry management or an admin dashboard in a future version, possible future entities may include, at a high level only (no schema design):
- **Customer** — basic contact information for people who submit inquiries.
- **Inquiry** — details of a specific customer request or question.
- **Service** — structured records of the 8 (or more) services, if they need to be managed dynamically.
- **Tour Package** — structured records of individual tour packages, if offered dynamically.
- **Admin User** — accounts for staff managing the site or inquiries.
- **Message Log** — a record of communications tied to an inquiry.
- **Payment Record** — details of a payment, if online payment is introduced in the future.

These are conceptual placeholders only, meant to inform long-term planning — they are not part of v1 and must not be built now.

---

# 7. Data Privacy Considerations

Keeping v1 free of a database directly reduces privacy and security risk:
- **No stored personal data** — there is nothing to protect, leak, or misuse, since nothing is collected.
- **No passenger information storage** — travel-related personal details stay entirely within the business's existing manual process.
- **No payment data storage** — the site never touches sensitive financial information.
- **No uploaded document storage** — no visa, passport, or ID documents are ever received or held by the website.

This significantly lowers the project's security burden and matches the zero-budget, static nature of v1.

---

# 8. Recommendation

It is recommended that v1 remain fully database-free. A static website is sufficient to meet all approved goals — presenting the business, explaining services, and generating inquiries through existing channels — without introducing the cost, complexity, and risk of building and securing a database.

---

# 9. Summary

This document confirms that v1 of the Homeland Travel and Tours – GBM Prestige Ticketing website does not require a database or an ERD. All content is static, no customer data is collected or stored, and all inquiries are routed to existing external communication channels. Database-related features such as customer, inquiry, booking, payment, and admin tables are explicitly excluded from v1, though conceptual entities are noted for possible future versions. Keeping v1 database-free minimizes risk, keeps costs at zero, and matches the site's confirmed purpose as a static, inquiry-focused business website.

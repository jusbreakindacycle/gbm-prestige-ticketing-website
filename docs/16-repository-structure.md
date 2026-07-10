# Deliverable 16: Repository Structure

## Homeland Travel and Tours – GBM Prestige Ticketing Website (v1)

This document defines the approved repository structure for the static website implementation phase.

## 1. Project Scope

- Static business website
- Plain HTML, CSS, and JavaScript only
- GitHub Pages deployment
- No backend, database, API, booking system, payment system, or admin app in v1

## 2. Approved Repository Structure

```text
gbm-prestige-ticketing-website/
├── .cursor/
│   └── rules/
│       └── project-rules.md
├── docs/
│   ├── 01-research-foundation.md
│   ├── 02-business-analysis.md
│   ├── 03-system-requirements-specification.md
│   ├── 04-functional-non-functional-requirements.md
│   ├── 05-use-case-analysis.md
│   ├── 06-user-stories.md
│   ├── 07-business-rules.md
│   ├── 08-data-dictionary.md
│   ├── 09-database-design-erd-decision.md
│   ├── 10-information-architecture.md
│   ├── 11-ui-ux-research.md
│   ├── 12-wireframes.md
│   ├── 13-design-system.md
│   ├── 14-software-architecture.md
│   ├── 15-api-design.md
│   └── 16-repository-structure.md
├── prompts/
│   └── cursor-implementation-rules.md
├── public/
│   ├── images/
│   ├── icons/
│   └── favicon/
├── src/
│   ├── css/
│   │   ├── reset.css
│   │   ├── variables.css
│   │   ├── base.css
│   │   ├── layout.css
│   │   ├── components.css
│   │   └── responsive.css
│   ├── js/
│   │   └── main.js
│   └── pages/
│       ├── about.html
│       ├── services.html
│       ├── tour-packages.html
│       ├── faqs.html
│       └── contact.html
├── .cursorrules
├── .gitignore
├── 404.html
├── index.html
├── LICENSE
└── README.md
```

## 3. Folder Responsibilities

- .cursor/ and .cursorrules: project rules for Cursor and AI-assisted editing.
- docs/: planning and reference documents for the approved website scope.
- prompts/: reusable implementation guidance for the repository.
- public/: static assets such as images, icons, and favicon files.
- src/css/: stylesheet files split by responsibility.
- src/js/: lightweight JavaScript for progressive enhancement only.
- src/pages/: secondary HTML pages for the informational website.

## 4. Implementation Notes

- The homepage and 404 page remain at the repository root.
- The website is informational only, so no backend, database, or API folders are part of v1.
- The database decision document is stored as docs/09-database-design-erd-decision.md for clarity and consistency.

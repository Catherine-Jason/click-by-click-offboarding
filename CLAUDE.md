# Click by Click Offboarding

Single file app (`index.html`). This is the Cyber Ready Clinic capstone. Click by Click Access, in `C:\Users\User\click-by-click-access`, grew out of it.

## Mirroring rule

These stay the same in both repos:

- Offboarding steps (titles, "why" text, when each step applies, urgent flags)
- "Why this matters" text
- Framework tags and their links
- Device fields (types, OS, encryption, More details fields)
- CSV import and export (column matching, template, export columns)
- Learn mode, glossary and sources
- Records for HR and audits (Access v2.8, Offboarding v1.8): the optional Organization name near the top of the intake (null means it follows the last name typed), the record number (OFF or ON, the date and a 4 character code, kept with the person), Prepared for and the record number at the top of the record, the sign off lines, page numbers, credit and disclaimer when printing, and the same lines at the end of the text file and copied record. Each app uses its own name and address in the credit.

Any change to those goes into both repos in the same session, as a separate commit in each repo.

Expected differences, which do not need mirroring:

- Titles, taglines, footers and version numbers
- localStorage keys: Offboarding uses `cbc-offboarding-v1`, Access uses `cbc-access-v1`. Offboarding is live at https://catherine-jason.github.io/click-by-click-offboarding/ and Access at https://access.catherinejason.com, so they no longer share browser storage. Keep the keys different anyway, in case they ever end up on the same address again. These must never match.
- Access says "your organization" where Offboarding says "nonprofit"
- Features only in Access: the Onboarding tab, the Inventory tab, backup and restore, and the links between them. Do not add these here.

## Working rules

- Test every change, show the diff (and any README change) before committing, and wait for "commit".
- README text is plain words with no dashes.
- The `capstone-v1.0` tag marks the version presented for the capstone. Never move or delete it.

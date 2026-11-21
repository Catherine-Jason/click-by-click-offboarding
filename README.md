# Click by Click Offboarding

This is my capstone project for the Cyber Ready Clinic internship.

When someone leaves a small nonprofit, their accounts usually stay open. Their email still works, shared passwords never get changed, and nobody really knows everything that person had access to. Most small nonprofits don't have an IT team, so this falls on whoever handles IT on the side.

I built this app to make that process simple. You answer a few questions about who is leaving and what they had access to, and it builds a checklist with only the steps that apply to them. If someone leaves unexpectedly or is let go, the urgent steps move to the top so access gets cut first. You can also list every device they have, like laptops, tablets and phones, with the serial number or asset tag, then check each one back in as returned, wiped or missing. Each device also has an operating system and an encryption field, like BitLocker for Windows or FileVault for a Mac, and the checklist adds the right wipe and sign-out steps for that system. If you already keep your inventory in Excel, you can import a CSV of their devices and download the results as a CSV to put back in your spreadsheet. When you're done, it gives you a dated record to keep for audits or cyber insurance, with the device list included.

Everything runs in the browser. Nothing gets saved to a server.

**Built with:** HTML, CSS, JavaScript

**Frameworks used:** CIS Controls 5 and 6, NIST CSF 2.0 PR.AA

**Try it:** https://catherine-jason.github.io/click-by-click-offboarding/

**Slides:** [Capstone presentation (PDF)](capstone-slides.pdf)

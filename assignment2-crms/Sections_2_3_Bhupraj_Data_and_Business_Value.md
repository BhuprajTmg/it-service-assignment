# Customer Relationship Management System (CRMS) for Top End Explorer Travels
## Group Report — Author's Draft: Sections 2 & 3

**Author of this draft:** Bhupraj Tamang (Data & Business Value Analyst)
**Case organisation:** Top End Explorer Travels — an independently owned boutique travel agency, Smith Street, Darwin CBD, specialising in tailored Top End/Kakadu domestic itineraries and international (Southeast Asia, Europe) bookings for retail and corporate clients.

> *Note for the group: structured this around the exact categories from our outline — Structured/Semi-Structured/Unstructured for Section 2, and Administrative Efficiency/Customer Intimacy/Supplier Coordination for Section 3 — but filled in a few extra points under each one, since just the original one-liners probably won't carry enough depth for full marks on their own. Happy to trim anything that feels like it's overreaching.*

---

## 2. Data Sources and Data Types

Top End Explorer Travels already collects a huge amount of information about its clients — it just isn't captured anywhere useful. A phone call, a web form, a passport scan, a throwaway comment about someone's anniversary: none of it is "one kind" of data, and each kind behaves differently once you try to actually put it into a system. Laudon and Laudon (2022) describe a CRM system as the piece of infrastructure that pulls an organisation's front-office functions — sales, marketing, service — around a single customer record, but that only works if the agency is honest about where its data really comes from. For this report we've grouped it the standard way: structured, semi-structured, and unstructured.

### Structured Data

Structured data is information that fits into fixed fields with a defined type — exactly what a relational database is designed for (Laudon & Laudon, 2022). For Top End Explorer Travels, this is the layer that runs the business day to day, and it covers more ground than it might first seem:

- **Client contact profiles** — name, date of birth, phone, email, postal address, and (because the agency also handles corporate clients) company name and billing contact for business accounts.
- **Booking dates** — travel start/end dates, number of travellers, and whether the booking is a domestic Kakadu/Litchfield-style itinerary or an international package.
- **Payment transaction logs** — amounts, currency, payment method, deposit versus balance, and reconciliation status.
- **Passport numbers** — along with expiry dates and nationality, which matter for both domestic identity checks and international visa/travel requirements.
- **Flight/accommodation pricing tiers** — supplier rates, seasonal pricing, and commission percentages that feed into quote generation.
- A smaller but still structured field worth adding: **loyalty/repeat-client status**, essentially a count or flag derived from booking history, which later feeds directly into the customer-retention argument in Section 3.

The reason this layer needs care isn't just about convenience, it's about risk. Passport numbers and payment details are sensitive personal information, and in the current paper/spreadsheet setup there's nothing stopping anyone in the office from opening a file and reading them. In the CRMS, those specific fields need column-level encryption and role-based access, so a junior agent isn't automatically seeing what the owner sees when processing a refund. Get this layer right, and a search like "who's travelling to Kakadu in July" or "who still owes a balance after 30 days" becomes a five-second query instead of flicking between spreadsheet tabs.

### Semi-Structured Data

Semi-structured data has some shape to it — tags, key–value pairs, usually XML or JSON — but it doesn't sit neatly in a column the way a date of birth does (Laudon & Laudon, 2022). This is mostly the data arriving from outside the business itself:

- **Inquiry web forms**, submitted from the agency's website as a JSON payload and ingested automatically through an API/webhook connector, rather than someone re-typing it after seeing an email notification.
- **Automated booking confirmation emails** from airlines, hotels, and tour operators, which can be parsed with a simple rule set (sender domain, subject-line pattern) so booking status updates itself instead of relying on someone reading every email.
- **Supplier rate sheets** — XML feeds from airlines and JSON feeds from hotel aggregators such as HotelBeds or Expedia TAAP — that need to update pricing and availability close to daily, not whenever someone happens to check an inbox.
- Worth adding here: **inquiry messages from social media and messaging channels** (Facebook/Instagram DMs, WhatsApp), which arrive with some platform-level structure (sender ID, timestamp, message thread) but still need a human or a bot to tag the actual intent.

The practical way to handle all of this is to not force it straight into final tables. Land it first in a staging layer — most relational databases now support a JSON column type for exactly this — and only pull the operationally important fields (confirmed price, confirmed dates, supplier reference) into the core Booking and Pricing Tier tables. That way, if a supplier changes their feed format next year, it breaks a staging import that can be fixed, not the whole database.

### Unstructured Data

And then there's the data with no shape at all, which — a little ironically for a personal-service business — is probably the most valuable of the three:

- **Agent–client phone call logs**, currently either not recorded at all or summarised inconsistently depending on which agent took the call.
- **Consultation notes regarding traveller health/dietary needs**, which right now live on paper and depend entirely on whoever wrote them remembering to mention it to the next person handling that booking.
- **Special-occasion markers** (anniversaries, honeymoons, milestone birthdays), typically noted informally and only "remembered" if the same agent happens to handle the client again.
- **Post-trip feedback and review text**, whether collected through a survey, an email reply, or said out loud at the counter.
- Also worth including: **scanned passport/visa image attachments** and **online reviews or social media mentions** (Google, TripAdvisor) referencing the agency, both of which are unstructured but still need to be linked back to a specific client or booking for them to be useful.

None of this can just be dumped into a spreadsheet cell and stay usable. In the CRMS it should sit in a Notes/Interaction record tied to the client ID, tagged with a handful of simple labels at the point of entry — dietary, mobility, special occasion, complaint — so that even free text becomes something you can filter and report on later, without losing the actual detail someone wrote down. That's the real difference this layer makes: between losing an inquiry, and the system still remembering the honeymoon booking even after the agent who took it has gone on leave.

None of these three layers works in isolation, though. The point of separating them this way — rather than treating "customer data" as one undifferentiated notes field, which is essentially what a spreadsheet already does — is that it's what turns the CRMS from a slightly nicer filing cabinet into a platform that can absorb every channel a client uses to reach the agency.

---

## 3. Why Customer Information is Important

It's worth asking *why* any of this is worth building, rather than just assuming "more data equals a better business," which is honestly where a lot of weaker reports on this topic stop. For Top End Explorer Travels, the value breaks down into three groups, matching who actually uses the data day to day.

### Administrative Efficiency

Reduces administrative overhead by automating client record lookup and invoice tracking. In practice this means a lookup that currently involves checking a spreadsheet, then a filing tray, then maybe a sticky note on someone's desk, becomes a single search on a name or booking reference. Linking the payment log to the booking record means overdue balances get flagged automatically instead of someone manually cross-checking a ledger at the end of the month, and because every change to a record is tied to a staff login, there's an actual audit trail — something that simply doesn't exist when the "system" is a shared spreadsheet anyone can edit. It's worth adding that this also reduces duplicate data entry: right now a single booking might be typed into a spreadsheet, copied into an email confirmation, and written again on a paper file, and each copy is a chance for an error to creep in.

### Customer Intimacy

Empowers agents to recall past preferences (e.g., preferred seat types, hotel styles) to deliver hyper-personalised itineraries, boosting customer retention. This is arguably the strongest commercial argument in the whole report, because a boutique agency competing against large online travel platforms can't win on price — it has to win on actually knowing the client. Once that knowledge sits in a searchable system instead of one agent's memory, any staff member can pick up a client's file and sound like they've known them for years, including things like the fact that a client mentioned wanting to try Kakadu after years of booking only international trips. It also supports basic segmentation — looking at how often and how recently a client books — to identify which repeat clients deserve loyalty treatment and which have quietly gone cold and are worth a re-engagement call. Cross-selling and upselling stop depending on one agent happening to remember a detail, and become something the system can actually prompt at the right moment.

### Supplier Coordination

Aligns travel bookings seamlessly with external tour operators, hotels, and airlines in Darwin and abroad, preventing over-booking and missed coordination. Because supplier data already arrives as the semi-structured feeds described in Section 2, keeping it in the same system as client bookings means availability can be checked against confirmed bookings close to real time — which matters when the alternative is double-booking a tour vehicle out to Kakadu, or a hotel room that's already sold out through a different channel. It also gives the agency aggregate visibility into how much business it's actually sending a given supplier over a season, which is a far stronger position to negotiate commission from than scattered figures across old spreadsheets. And because the client-facing booking and the supplier's confirmation live in one place rather than separate email threads, the kind of mismatch where a flight gets rebooked but the hotel dates don't follow becomes much less likely.

Put simply: admin gets efficiency and accountability, agents get personalisation and the retention/revenue that comes with it, and suppliers get coordination and negotiating leverage. None of that happens just from "having more data" sitting in a system — it happens because the data architecture described in Section 2 gives each of these three groups a specific, deliberate way of using the same underlying customer record.

---

### References (to be merged with the group's consolidated reference list)

Buttle, F., & Maklan, S. (2019). *Customer relationship management: Concepts and technologies* (4th ed.). Routledge.

Laudon, K. C., & Laudon, J. P. (2022). *Management information systems: Managing the digital firm* (17th ed.). Pearson.

---

*Draft word count (Sections 2 & 3 body text only, excluding headings/table/references): ~1,500 words.*

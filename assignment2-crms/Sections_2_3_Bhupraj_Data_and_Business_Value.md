# Customer Relationship Management System (CRMS) for Top End Explorer Travels
## Group Report — Author's Draft: Sections 2 & 3

**Author of this draft:** Bhupraj Tamang (Data & Business Value Analyst)
**Case organisation:** Top End Explorer Travels — an independently owned boutique travel agency, Smith Street, Darwin CBD, specialising in tailored Top End/Kakadu domestic itineraries and international (Southeast Asia, Europe) bookings for retail and corporate clients.

---

## 2. Data Sources and Data Types

Top End Explorer Travels already collects a lot of information about its clients, it just isn't captured anywhere useful. A phone call, a web form, a passport scan, a comment about someone's anniversary — none of this is "one kind" of data, and each behaves differently once you try to put it into a system. Laudon and Laudon (2022) describe a CRM as the infrastructure that pulls an organisation's sales, marketing, and service functions around a single customer record, but that only works if the agency is clear on what kind of data it's actually dealing with. We've grouped it the standard way: structured, semi-structured, and unstructured.

**Structured Data** covers client contact profiles, booking dates, payment transaction logs, passport numbers, and flight/accommodation pricing tiers. This is the data that already fits a fixed format, so it slots naturally into relational database tables (Laudon & Laudon, 2022) — a Client table, a Booking table, a Payment log, and a Pricing Tier table pulling from supplier rates. Passport numbers and payment details need extra care here, since they're sensitive personal information currently sitting in an unlocked spreadsheet; in the CRMS they should be encrypted and only visible through role-based access, so a junior agent isn't seeing what the owner sees when processing a refund.

**Semi-Structured Data** includes inquiry web forms, automated booking confirmation emails, and supplier rate sheets arriving as XML/JSON feeds from airlines and hotel aggregators. These have some shape (tags, key-value pairs) but don't sit neatly in a column, so instead of someone re-typing a web form after it lands in an inbox, it should come in through an API connector, and confirmation emails should be parsed automatically off sender/subject patterns to update booking status. Supplier feeds (XML from airlines, JSON from aggregators like HotelBeds) need to refresh pricing and availability close to daily rather than whenever someone checks an inbox.

**Unstructured Data** is agent-client phone call logs, consultation notes on traveller health/dietary needs, special-occasion markers like anniversaries, and post-trip feedback reviews. This is probably the most valuable of the three for a personal-service business, and right now it mostly lives on paper or in one agent's memory. In the CRMS it should sit as a Notes/Interaction record tied to the client ID, with simple tags (dietary, mobility, occasion, complaint) applied as it's entered, so free text stays searchable without losing the detail someone actually wrote down.

None of the three layers works on its own — treating them separately, instead of lumping "customer data" into one notes field the way a spreadsheet does, is what turns the CRMS into something that can actually absorb every channel a client uses to reach the agency.

---

## 3. Why Customer Information is Important

**Administrative Efficiency** reduces administrative overhead by automating client record lookup and invoice tracking. A lookup that currently means checking a spreadsheet, then a filing tray, then maybe a sticky note, becomes one search. Linking payments to bookings flags overdue balances automatically instead of someone cross-checking a ledger by hand, and because every change is tied to a staff login, there's an audit trail that simply doesn't exist when the "system" is a shared spreadsheet.

**Customer Intimacy** empowers agents to recall past preferences, like preferred seat types or hotel styles, to deliver hyper-personalised itineraries and boost customer retention. A boutique agency can't compete with large online platforms on price, so it has to win on actually knowing the client. Once that knowledge sits in a system instead of one agent's head, any staff member can pick up a file and sound like they've known the client for years, and basic patterns in booking history make it easier to spot which repeat clients are worth loyalty treatment and which have gone quiet.

**Supplier Coordination** aligns travel bookings seamlessly with external tour operators, hotels, and airlines in Darwin and abroad, preventing over-booking and missed coordination. Because supplier data already arrives as the feeds described in Section 2, keeping it in the same system as client bookings means availability can be checked against confirmed bookings in close to real time, which matters when the alternative is double-booking a Kakadu tour vehicle or a room that's already sold out elsewhere.

Put simply: admin gains efficiency and accountability, agents gain personalisation and retention, and suppliers gain coordination — and none of that comes from just "having more data," it comes from the architecture in Section 2 giving each group a deliberate way of using the same underlying customer record.

---

### References (to be merged with the group's consolidated reference list)

Laudon, K. C., & Laudon, J. P. (2022). *Management information systems: Managing the digital firm* (17th ed.). Pearson.

---

*Draft word count (Sections 2 & 3 body text only, excluding headings/references): ~750 words.*

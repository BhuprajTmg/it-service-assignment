# Customer Relationship Management System (CRMS) for Top End Explorer Travels
## Group Report — Author's Draft: Sections 2 & 3

**Author of this draft:** Bhupraj Tamang (Data & Business Value Analyst)
**Case organisation:** Top End Explorer Travels — an independently owned boutique travel agency, Smith Street, Darwin CBD, specialising in tailored Top End/Kakadu domestic itineraries and international (Southeast Asia, Europe) bookings for retail and corporate clients.

> *Note for the group: I've written this to sit straight after Prabin's Section 1, so it keeps referring back to the same problem he sets up — the spreadsheets, the paper notes, the inboxes. Feel free to tighten the wording so it sounds like you two as well; I didn't want it reading like three separate essays stapled together. Also worth checking the Laudon & Laudon edition we used in Assignment 1 and lining the citation up with that.*

---

## 2. Data Sources and Data Types

Once you actually sit down and think about everything Top End Explorer Travels collects from a client — a phone call, a web form, a passport scan, an offhand comment about someone's anniversary — it becomes obvious that "customer data" is not one thing. It is at least three different kinds of thing, and each one behaves differently once you try to put it into a system. Laudon and Laudon (2022) frame a CRM system as the piece of infrastructure that unifies an organisation's front-office functions (sales, marketing, service) around a single customer record, but getting to that single record only works if the agency is honest about where its data actually comes from and how messy some of it is. For this report we've grouped it the standard way: structured, semi-structured, and unstructured.

### 2.1 Structured Data

This is the easy part, in the sense that it is the data that already behaves itself. Structured data fits into fixed fields with defined types, which is exactly what a relational database wants (Laudon & Laudon, 2022). For Top End Explorer Travels, this is the layer that would actually run the business day to day: a **Client** table (client ID, name, date of birth, passport number and expiry, nationality, contact details, emergency contact), a **Booking** table (booking ID, linked client, destination, whether it's a domestic Kakadu/Litchfield safari or an international package, travel dates, traveller count, status), a **Payment/Transaction Log** (amounts, currency, payment method, deposit versus balance, reconciliation status), and a **Pricing Tier** table holding supplier rates, seasonal pricing, and commission percentages.

A couple of things matter here that a lot of first-pass designs skip. Passport numbers and payment details are not just "fields" — they're sensitive personal information, and in the current paper-and-spreadsheet setup there is nothing stopping anyone in the office from opening a client file and reading them. In the CRMS, those fields need column-level encryption and should only be visible through role-based access control, so a junior agent doesn't have the same visibility as the owner handling refunds. The payoff of getting this layer right is that a search like "which clients are travelling to Kakadu in July" or "who still owes a balance after 30 days" becomes a five-second query instead of someone flicking between spreadsheet tabs.

### 2.2 Semi-Structured Data

Semi-structured data has some shape to it — tags, key–value pairs, usually XML or JSON — but it won't sit neatly in a column the way a date of birth will (Laudon & Laudon, 2022). For this agency, that's basically everything coming in from outside the business itself: the inquiry form on the website, which arrives as a JSON payload and should be picked up by the CRMS automatically through an API connector rather than someone re-typing it from an email notification; the booking confirmation emails that airlines, hotels, and tour operators send out, which can be parsed with a simple rule set matching sender and subject line so the booking status updates itself; and the rate and availability feeds that come from suppliers — XML from airlines, JSON from hotel aggregators like HotelBeds or Expedia TAAP — which need to flow into pricing and availability on something close to a daily basis, not whenever someone remembers to check an inbox.

The practical way to handle this is to not force it into the final tables straight away. Land it first in a staging layer — most relational databases now support a JSON column type for exactly this — and only pull out the fields that actually matter operationally (confirmed price, confirmed dates, supplier reference) into the Booking and Pricing Tier tables. That way, if an airline changes the format of its feed next year, it doesn't break the whole database, it just breaks a staging import that can be fixed without touching anything client-facing.

### 2.3 Unstructured Data

And then there's the data that has no shape at all, which, somewhat ironically for a personal-service business, is probably the most valuable of the three. Phone call notes, consultation records about dietary needs or mobility issues, the fact that a client mentioned it's their 20th wedding anniversary, a paragraph of feedback written after a trip — none of this fits a column, and right now at Top End Explorer Travels it lives on paper, in someone's memory, or nowhere at all once the agent who took the call goes on leave.

The fix isn't to try and force this into a rigid structure either, because then it stops being useful. Instead it should sit in a Notes/Interaction record tied to the client ID, with a handful of simple tags applied as it's entered — dietary, mobility, special occasion, complaint — so that even free text becomes something you can filter and report on later, without losing the actual detail a human agent wrote down. That's really the whole point of this layer: it's the difference between "we lose inquiries and forget to follow up" and "the system remembers the honeymoon booking even if the agent who took it is on leave."

### 2.4 Pulling it together

| Data category | Examples at Top End Explorer Travels | How it gets in | Where it lives |
|---|---|---|---|
| Structured | Client profiles, bookings, payments, pricing tiers | CRMS forms, payment gateway | Normalised relational tables, encrypted sensitive fields, RBAC |
| Semi-structured | Web inquiry forms, confirmation emails, supplier feeds | API/webhook integration, scheduled sync | JSON staging layer, then normalised into core tables |
| Unstructured | Call notes, dietary/health notes, occasion markers, feedback | Agent entry at point of contact, post-trip survey | Tagged Notes/Interaction record linked to client ID |

None of this works, though, if the three layers are treated as separate systems. The whole point of designing them this way — rather than just dumping everything into one big "notes" field, which is essentially what a spreadsheet already does — is that it turns the CRMS from a slightly nicer filing cabinet into a platform that can actually absorb every channel a client might use to reach the agency.

---

## 3. Why Customer Information is Important

It's worth asking *why* any of this is worth building, rather than just assuming "more data equals better business," which is honestly where a lot of weaker reports on this topic stop. The useful way to answer it is through the distinction CRM literature draws between operational, analytical, and collaborative CRM (Buttle & Maklan, 2019; Laudon & Laudon, 2022) — and conveniently, those three layers map almost exactly onto the three groups this report needs to cover: admin staff, the sales/agent side of the business, and the external suppliers.

### 3.1 Administrative Efficiency (Operational CRM)

This is the least glamorous benefit but probably the one that pays for the system fastest. Operational CRM is just the automation of the routine stuff admin staff currently do by hand — and right now that hand-work is genuinely slow at Top End Explorer Travels. A client lookup that means checking a spreadsheet, then a filing tray, then maybe a sticky note on someone's desk, becomes one search on a name or booking reference. Linking the payment log to the booking record means overdue balances get flagged automatically instead of someone manually cross-referencing a ledger at the end of the month. And because every change to a record is tied to a staff login, there's an actual audit trail — something that simply doesn't exist when the "system" is a shared spreadsheet anyone can edit.

The time saved here isn't abstract either: less time locating a file, less duplicate data entry, fewer inquiries that quietly die in someone's inbox because nobody logged them against a client in the first place.

### 3.2 Customer Intimacy and Revenue (Analytical CRM)

This is where the real commercial argument sits, and it's the part that connects back to Section 2.3. A boutique agency competing against big online travel platforms can't win on price, so it has to win on knowing the client — remembering that someone prefers an aisle seat, or a particular style of hotel, or that they mentioned wanting to try Kakadu next after years of booking only overseas trips. Once that information is sitting in a searchable system rather than in one agent's head, any staff member can pick up a client's file and sound like they've known them for years, which is exactly the kind of service a boutique agency is supposed to be selling.

It also opens up some fairly basic but genuinely useful analysis — looking at recency, frequency, and spend to work out which repeat clients deserve loyalty treatment, and which ones have quietly gone cold and might be worth a phone call. Cross-selling stops being a matter of luck (an agent happening to remember a client's anniversary) and becomes something the system can actually surface at the right moment. The underlying point, which is really the direct answer to the old "surface-level" feedback, is that the business value isn't the data itself, it's turning one agent's personal memory into something the whole business can act on.

### 3.3 Supplier Coordination (Collaborative CRM)

The third layer looks outward, to the airlines, hotels, and Top End tour operators the agency actually books through. Because supplier data already flows in as the semi-structured feeds described in Section 2.2, keeping it in the same system as client bookings means availability can be checked against confirmed bookings in close to real time — which matters a lot when the alternative is double-booking a tour vehicle or a hotel room that's already sold out somewhere else. It also means the agency can see, in aggregate, how much business it's actually sending a given supplier, which is a far stronger position to negotiate commission from than scattered figures across old spreadsheets. And because both the client-facing booking and the supplier's confirmation live in one place, the kind of mismatch where a flight gets rebooked but the hotel dates don't follow — currently a real risk with information split across emails — becomes much less likely.

Put simply: admin gets efficiency and accountability, agents get personalisation and the revenue that comes with it, and suppliers get coordination and leverage. None of that happens from "having more data" on its own — it happens because the architecture in Section 2 gives each of those groups a different, deliberate way of using the same underlying customer record.

---

### References (to be merged with the group's consolidated reference list)

Buttle, F., & Maklan, S. (2019). *Customer relationship management: Concepts and technologies* (4th ed.). Routledge.

Laudon, K. C., & Laudon, J. P. (2022). *Management information systems: Managing the digital firm* (17th ed.). Pearson.

---

*Draft word count (Sections 2 & 3 body text only, excluding headings/table/references): ~1,500 words.*

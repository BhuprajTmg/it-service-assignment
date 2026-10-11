# Assignment 3 — Continual Improvement through ITIL 4 Practices
## Author's Draft: Section 5 (Parts 5.1 and 5.2) + Shared Summary Table

**Author of this draft:** Bhupraj Tamang (Student ID: S398423)
**Case organisation:** Australia Post — MyPost / PostApp Digital Parcel Management System
**Team:** Danala Group 11

> Note to team: This draft assumes Section 4 (Prabin) has already established the three core problems —
> (1) high volumes of repeat tracking inquiries, (2) inflated MTTR during peak-season surges, and
> (3) siloed diagnostic logs across support teams. Each sub-section below opens with a one-line link
> back to those problems before moving into the ITIL 4 practice detail, so the narrative flows
> Section 4 → Section 5 without repeating Prabin's analysis.

---

## 5. ITIL 4 Practices for Continual Improvement

### 5.1 Incident Management

The incidents raised against PostApp and the MyPost tracking portal are rarely diagnosed once — they are diagnosed repeatedly, by whichever team happens to pick up the ticket, because the diagnostic logs described in Section 4 sit in separate systems for the network team, the app-support team and the fulfilment-centre scanning team. This is the direct cause of the inflated Mean Time to Resolve (MTTR) seen during peak-season surges: by the time an incident is correlated across all three log sources, the parcel volume has already moved on to the next surge day. ITIL 4 defines the objective of Incident Management as minimising the negative impact of incidents by restoring normal service operation as quickly as possible, in a way that maintains the quality and continuity of the service (Axelos, 2019). For Australia Post, "normal operation" during a surge period needs to be redefined as a faster, correlated response rather than the current sequential hand-off between teams.

**Practice Success Factor 1: Early detection and effective diagnosis of incidents**
Key Metrics:
- Mean Time to Detect (MTTD) for Priority 1/2 incidents affecting parcel tracking or scanning
- Percentage of incidents identified through proactive monitoring and alerting rather than customer complaints
- Weekly volume of duplicate or repeat tracking-related tickets logged against an already-open incident

**Practice Success Factor 2: Minimising the business and customer impact of incidents by restoring service as quickly as possible**
Key Metrics:
- Mean Time to Resolution (MTTR), benchmarked separately for peak-season and business-as-usual periods
- SLA compliance rate — percentage of incidents resolved within the agreed SLA window
- First-Contact Resolution (FCR) rate at the service desk
- Incident re-open rate, as a check on the quality (not just the speed) of each resolution

The revised practice replaces the current sequential escalation model with a swarming approach: a single correlated incident dashboard that pulls PostApp application logs, MyPost tracking-backend logs and warehouse scanning-system logs into one timeline, so diagnosis happens once, by a cross-functional group, instead of three times by three separate teams. A tiered priority matrix would also flag surge-related incidents automatically once ticket volume crosses a defined threshold, triggering the swarm before the queue backs up rather than after customers have already noticed the delay. Tracking MTTR and SLA compliance separately for peak and non-peak periods matters here, because a single blended average currently hides exactly how much worse the service gets during the surge windows that cause the most customer complaints — the metric itself needs to change before the practice can be judged as improved.

### 5.2 Knowledge Management

The repeat tracking inquiries identified in Section 4 are, in large part, a knowledge problem rather than a volume problem: the same handful of tracking issues (parcel "stuck" at a depot scan, delivery-date mismatches, failed proof-of-delivery photos) are being re-explained to customers and re-diagnosed by agents because there is no shared, trusted place to store the answer the first time it is found. ITIL 4 describes the objective of Knowledge Management as maintaining and improving the effective, efficient use of information and knowledge across the organisation, so that people and systems can make better decisions with less effort (Axelos, 2019). At Australia Post this means closing the gap between what support agents already know after resolving an incident and what both future agents and customers can access without raising a new ticket.

**Practice Success Factor 1: Effectively using information to enable decision-making, for both support staff and customers**
Key Metrics:
- Self-service deflection rate — the percentage of tracking inquiries resolved through PostApp's help centre or chatbot content without escalating to a live agent
- Knowledge-base (KB) adoption rate among service-desk staff — the percentage of incident resolutions that reference an existing KB or Known Error Database (KEDB) article rather than starting diagnosis from zero
- Reduction in repeat/duplicate tracking inquiries, measured against the Section 4 baseline

**Practice Success Factor 2: Maintaining knowledge content that is current, accurate and genuinely useful**
Key Metrics:
- Article freshness index — the percentage of KB articles reviewed or updated within the governance cycle (proposed quarterly review)
- Users' satisfaction with knowledge-management tools, captured through a short post-article feedback prompt ("Did this solve your issue?")
- Compliance of knowledge articles with the formally agreed KEDB template, verified through periodic audit

The revised practice makes knowledge capture a mandatory, non-optional step in incident closure: every Priority 1/2 incident must generate or update a KEDB article before the ticket can be closed, and the highest-frequency customer-facing issues are converted into plain-language self-service content on PostApp, directly targeting the repeat-inquiry volume raised in Section 4. This also strengthens Incident Management in Section 5.1, since a mature KEDB is what allows the swarming team to recognise a recurring fault pattern immediately instead of re-diagnosing it from scratch, which is why the two practices are presented together rather than in isolation. Measuring deflection rate and KB adoption together is deliberate: a high deflection rate with low staff adoption would suggest the self-service content is working for customers but agents are still bypassing it, which is the opposite failure mode to the one Australia Post currently has.

---

## Shared Summary Table — PSFs Aligned to Key Metrics (for team formatting)

| ITIL 4 Practice | Practice Success Factor | Key Metric(s) | Problem from Section 4 Addressed |
|---|---|---|---|
| Incident Management | Early detection and effective diagnosis | MTTD; % incidents caught proactively; repeat-ticket volume | Siloed diagnostic logs |
| Incident Management | Minimising business/customer impact via fast restoration | MTTR (peak vs BAU); SLA compliance rate; First-Contact Resolution; re-open rate | Inflated MTTR during peak-season surges |
| Knowledge Management | Effective use of information for decision-making | Self-service deflection rate; KB adoption rate; reduction in repeat inquiries | High volumes of repeat tracking inquiries |
| Knowledge Management | Maintaining current, accurate knowledge content | Article freshness index; user satisfaction; KEDB template compliance | Siloed diagnostic logs / tribal knowledge |

*(Suggested to team: add a column for the matching PSF/metric from Section 5.1 contributed by other members if your assigned practice differs, so the final table in the report covers every practice discussed across Section 5.)*

---

### Reference used in this draft (to be merged into the group's consolidated reference list)

Axelos. (2019). *ITIL 4: Create, deliver and support*. TSO (The Stationery Office).

---

*Draft word count (Section 5.1 + 5.2 body text, PSFs and key metrics, excluding the shared table and this note): ~840 words — in line with the ~400 words allocated to each sub-section in the team task division plan.*

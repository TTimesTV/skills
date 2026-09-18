# Palantir Ontology — official-video research pack

Use when a TTimes speech beat explains Palantir Ontology as modeling an organization's objects, relationships, state, rules, permissions, and actions. This is a source/timestamp bank, not a rights-clearance record.

## Editorial concept map

Translate the spoken beat before searching:

- `물건·고객·시설·사람` → objects / nouns
- `객체 사이 연결` → links / relationships
- `현재 주문·배송·경보 상태` → properties / current state
- `환불·취소·배정·경로 변경` → actions / verbs
- `누가 무엇을 할 수 있나` → permissions / guardrails
- `승인·validation·상태 전이` → rules / compliant state change
- `커머스 외 조직` → defense, healthcare, industrial operations; use only as an extension example, not as proof of a specific commercial workflow

## Ranked official sources

### 1. Palantir Ontology Overview

- Source: Palantir official
- URL: https://www.youtube.com/watch?v=YDAxITCNcko
- Best use: clean concept animation; primary source for an abstract Ontology explanation
- `00:07–00:28`: “nouns and verbs”; plants, warehouses, products, customers and interconnected relationships. The right-side white board visibly fills with object icons and links.
- `00:39–00:59`: decision-centric system = data, logic, actions; data represents current business state and actions affect the real world.
- `02:34–02:49`: data + logic + actions form a digital twin of actual operations.
- Visual note: presenter and graphic are split-screen. Crop or enlarge the right graphic if text is unreadable. Best conceptual insert; weaker for granular permissions.

### 2. Building with Palantir AIP: Customer Service Engine

- Source: Palantir Developers official
- URL: https://www.youtube.com/watch?v=X2XJ_g6BUiU
- Best use: actual customer/order/shipment/case objects and operational state
- `02:02–02:22`: Case Ontology graph connects customer alert, customer, order, product/shipment and AI-suggested response.
- `02:26–03:12`: customer requests delivery postponement; AIP suggests Modify Delivery Date; execution writes the new state back to the Ontology and can write to source systems.
- `04:19–04:34`: explicit access is limited to allowed objects and even allowed properties.
- Claim boundary: no refund action is shown. Use as customer/order/state modeling or delivery-date-change evidence, not as a literal refund demo.

### 3. Foundry 2022 Operating System Demo

- Source: Palantir official
- URL: https://www.youtube.com/watch?v=uF-GSj-Exms
- Best use: strongest technical evidence for actions, validations, permissions, approval and compliant state change
- `35:55–36:18`: Ontology Manager visibly lists Object Types, Link Types and Action Types; narration says actions modify ontology state compliantly.
- `36:20–37:17`: opens `Cancel Customer Order`; UI shows modified objects/properties, parameters, rules and validation.
- `37:32–37:54`: identity-aware permission example; a junior employee's cancellation can require manager approval, then write back to ERP/MES.
- Visual note: small UI text. Enlarge `Cancel Customer Order`, `RULES`, `PARAMETERS`, and `VALIDATION`; suppress spoken captions while the UI is the primary reading object.
- Claim boundary: order cancellation is the nearest official proxy found for refund; do not relabel it as refund.

### 4. Foundry Reference Project | Ontology

- Source: Palantir Developers official
- URL: https://www.youtube.com/watch?v=GONnAl2wwvw
- `03:07–03:42`: Actions are edit rules; state-machine edits change status and assignee through an alert lifecycle; Link Types connect alert to route.
- `08:03–08:19`: operational object view shows an alert in context plus actions that move it through its lifecycle.
- Best use: short technical support for state machine / object lifecycle without a commerce-heavy framing.

### 5. Introducing Palantir AIP | Capabilities and Product Demo

- Source: Palantir official
- URL: https://www.youtube.com/watch?v=Xt_RLNx1eBM
- `00:28–00:49`: real-time representation of concepts/actions/decisions; rules define what AI can see and do.
- `02:19–02:29`: AI cannot access employee-level PII despite its presence in the data foundation.
- `05:01–05:19`: AIP Control Panel sets per-model guardrails—visible objects, recommendable/executable actions, trusted workflows and authorized users.
- Best use: permission/AI guardrail layer, not core Ontology object modeling.

### 6. Palantir Gotham for Defense Decision Making

- Source: Palantir official
- URL: https://www.youtube.com/watch?v=rxKghrZU5w8
- `03:46–04:32`: commander compares courses of action, selects an option, submits a task order, and a ship changes course.
- Best use: 2–4 second proof that the object/state/rule/action paradigm extends beyond commerce.
- Claim boundary: this demonstrates an operational outcome, not the Ontology schema or permissions UI itself.

## Recommended 3-cut sequence

For a beat like “there are products, customers, returns, and beyond commerce the organization has permissions, rules and states that can all be modeled”:

1. `Ontology Overview 00:09–00:25` — objects and relationships build up.
2. `Customer Service Engine 02:02–02:18` — customer/order/shipment/case graph in actual UI.
3. `Foundry OS Demo 36:42–36:54` or `37:32–37:50` — validation or manager-approval rule.

Optional 4th cut: `Gotham 03:46–04:05` for non-commerce extension.

## Exact-video research workflow learned

When the user explicitly asks to find footage rather than merely specify source families:

1. Convert the speech into viewer functions and product terms before searching.
2. Search official company and developer channels first.
3. Fetch timed transcripts and search for concept terms and adjacent synonyms.
4. Separate four roles: clean concept overview, actual operational example, technical proof UI, and non-domain extension example.
5. Download only candidate time ranges with `yt-dlp --download-sections` and inspect contact sheets. A transcript match is not enough; verify the visible action and legibility.
6. Report exact timestamp links, observable screen content, use function, crop/legibility note, and claim boundary.
7. Never upgrade a nearby action into the requested one: order cancellation is not refund; delivery-date modification is not refund; a military outcome is not proof of ontology configuration.
8. Keep source identity, factual support, and broadcast rights as separate states. Official upload does not equal cleared use.

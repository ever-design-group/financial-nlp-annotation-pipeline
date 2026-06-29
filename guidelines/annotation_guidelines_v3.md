# Annotation Guidelines v3.0

## NexusBank AI Lab – Customer Sentiment Monitoring System

**Version:** 3.0  
**Date:** 2026-06-22

---

## 1. Core Principles

1. **Holistic Reading** – Read full communication before scoring
2. **Context Over Keywords** – "Great" in "Great, I was charged twice" = Frustration 4
3. **Cultural Sensitivity** – Indian politeness ("Respected Sir") is NOT sentiment
4. **Multi-label Valid** – Multiple Intents and Topics per communication
5. **Confidence Scoring** – Flag uncertain labels: High/Medium/Low

---

## 2. Sentiment Guidelines (1-5 Likert)

### 2.1 Satisfaction

| Score | Definition | Example Signal |
|-------|------------|----------------|
| 1 | Not Present | No positive evaluation |
| 2 | Minimal | "At least the app worked" |
| 3 | Moderate | "Agent was helpful but process slow" |
| 4 | High | "Very pleased, minor reservations" |
| 5 | Exceptional | "Outstanding service, resolved perfectly" |

### 2.2 Urgency

| Score | Definition | Example Signal |
|-------|------------|----------------|
| 1 | Not Present | "Just wondering when you have time" |
| 2 | Low | "Could you look sometime this week?" |
| 3 | Moderate | "Need resolved before end of month" |
| 4 | High | "This is my 4th email, payment due in 2 days" |
| 5 | Critical | "Account frozen, cannot pay hospital bill" |

### 2.3 Frustration

| Score | Definition | Example Signal |
|-------|------------|----------------|
| 1 | Not Present | "What are your interest rates?" |
| 2 | Mild | "A bit annoying to visit branch" |
| 3 | Moderate | "Frustrated this took 3 weeks" |
| 4 | High | "Absolutely unacceptable, third time" |
| 5 | Extreme | "Closing all accounts, lost a 20-year customer" |

### 2.4 Confusion

| Score | Definition | Example Signal |
|-------|------------|----------------|
| 1 | Not Present | "Please reverse duplicate charge" |
| 2 | Mild | "Is FD auto-renewed?" |
| 3 | Moderate | "I don't understand the charges" |
| 4 | High | "But I thought my account was KYC compliant?" |
| 5 | Extreme | "Why can't I withdraw from my mutual fund?" |

---

## 3. Intent Guidelines (Multi-label)

| Intent | Definition | Decision Rule |
|--------|------------|---------------|
| **Complaint** | Expressing dissatisfaction about past event | Past-tense negative; blame |
| **Query** | Seeking information | Question marks; "What/Why/How" |
| **Request** | Asking for specific action | Imperative; "Please + action" |
| **Feedback** | Providing input (no action expected) | "I think", "Just wanted to say" |
| **Escalation** | Demanding higher intervention | "Ombudsman", "RBI", "Manager", threats |

### Intent Priority (when ambiguous):
1. Escalation > Request > Complaint > Query > Feedback

---

## 4. Topic Guidelines (Multi-label)

| Topic | Definition | Signal Checklist |
|-------|------------|------------------|
| **Billing** | Charges, fees, payments | "Charge", "fee", "payment", "statement" |
| **Fraud** | Unauthorized transactions | "Unauthorized", "fraud", "skimming" |
| **Account Access** | Login, password, locks | "Login", "password", "locked", "blocked" |
| **Product Inquiry** | Questions about products | "FD", "loan", "credit card", "interest rate" |
| **Regulatory Complaint** | Invoking regulatory rights | "Ombudsman", "RBI", "SEBI", "consumer court" |

---

## 5. Sarcasm Detection Protocol

### Step 1: Trigger Check
Does it contain potential sarcasm indicators?
- Exaggerated praise in negative context
- Rhetorical questions implying failure
- Thanking for negative experiences
- Structural irony (listing dates, "fifth attempt")

### Step 2: Context Consistency Test
- Positive context + Positive language = GENUINE → Stop
- Negative context + Positive language = SUSPECT → Step 3

### Step 3: Sarcasm Confirmation (Requires 2+ indicators)
- ✅ Praise + negative experience
- ✅ Rhetorical question implying failure
- ✅ Thanking for negative event
- ✅ Exaggerated superlative in complaint
- ✅ Structural irony

**Decision:** 2+ confirmed → SARCASTIC → Invert sentiment scores

---

## 6. Calibration Examples

### Example 1: Sarcasm
**Text:** "Oh wonderful, another month of mystery charges."
**Sat:** 1, **Urg:** 3, **Frus:** 4, **Conf:** 2
**Intent:** Complaint, **Topic:** Billing
**Note:** Sarcastic - "wonderful" means opposite

### Example 2: Multi-Intent
**Text:** "My account is locked. Also what are your FD rates?"
**Sat:** 2, **Urg:** 4, **Frus:** 3, **Conf:** 3
**Intent:** Query + Request, **Topic:** Account Access + Product Inquiry

### Example 3: Cultural Context
**Text:** "Kindly look into this matter as early as possible."
**Sat:** 2, **Urg:** 3, **Frus:** 2, **Conf:** 1
**Note:** "Kindly" in Indian English = polite but implies urgency

### Example 4: Regulatory Threat
**Text:** "If not resolved by tomorrow, I am writing to RBI."
**Sat:** 1, **Urg:** 5, **Frus:** 5, **Conf:** 1
**Intent:** Escalation, **Topic:** Regulatory Complaint

### Example 5: Genuine Positive
**Text:** "Your team resolved my issue in 10 minutes. Excellent service!"
**Sat:** 5, **Urg:** 1, **Frus:** 1, **Conf:** 1
**Intent:** Feedback, **Topic:** Billing

### Example 6: Code-Switched (Hinglish)
**Text:** "Mera account locked hai. Three times password try kiya."
**Sat:** 2, **Urg:** 4, **Frus:** 4, **Conf:** 3
**Note:** Hindi emotional expression = Frustration +1

### Example 7: Passive Aggressive
**Text:** "As per my previous 5 emails, I'm still waiting."
**Sat:** 2, **Urg:** 4, **Frus:** 5, **Conf:** 1
**Note:** Structural sarcasm - listing 5 emails

---

## 7. Quick Reference Card

### Sentiment Scores (1-5)
- **1:** Not present / Very low
- **2:** Minimal / Low
- **3:** Moderate
- **4:** High / Strong
- **5:** Exceptional / Critical / Extreme

### Intent Priority
1. Escalation
2. Request
3. Complaint
4. Query
5. Feedback

### Topic Priority
1. Regulatory Complaint
2. Fraud
3. Billing
4. Account Access
5. Product Inquiry

---

## 8. Common Mistakes to Avoid

1. ❌ Treating Indian politeness ("Respected Sir") as positive sentiment
2. ❌ Missing sarcasm when literal text is positive
3. ❌ Assigning only one intent when there are multiple
4. ❌ Ignoring numerical context (₹50,000 vs ₹500)
5. ❌ Under-rating urgency in formal language
6. ❌ Missing escalation signals (Ombudsman, RBI, deadline)

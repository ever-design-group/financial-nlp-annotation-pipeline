# Calibration Exercises – 10 Exercises (50 Items)

## Exercise 1: Basic Sentiment Detection

### Item 1.1
**Text:** "What are your current savings account interest rates?"
**Correct:** Sat:1, Urg:1, Frus:1, Conf:1, Intent:Query, Topic:Product Inquiry

### Item 1.2
**Text:** "I'm very happy with your service today."
**Correct:** Sat:5, Urg:1, Frus:1, Conf:1, Intent:Feedback

### Item 1.3
**Text:** "I need my money back now!"
**Correct:** Sat:1, Urg:5, Frus:5, Conf:1, Intent:Request

### Item 1.4
**Text:** "Can you explain these charges? I don't understand them."
**Correct:** Sat:2, Urg:2, Frus:2, Conf:4, Intent:Query

### Item 1.5
**Text:** "Your app is okay, I guess. It works sometimes."
**Correct:** Sat:3, Urg:1, Frus:2, Conf:1, Intent:Feedback

---

## Exercise 2: Intent Classification

### Item 2.1
**Text:** "I will close my account if this isn't fixed."
**Correct:** Sat:1, Urg:4, Frus:4, Conf:1, Intent:Escalation

### Item 2.2
**Text:** "Please refund the ₹5000 fee you charged."
**Correct:** Sat:1, Urg:3, Frus:3, Conf:1, Intent:Request

### Item 2.3
**Text:** "I'm writing to complain about your customer service."
**Correct:** Sat:1, Urg:2, Frus:3, Conf:1, Intent:Complaint

### Item 2.4
**Text:** "What is the interest rate on fixed deposits?"
**Correct:** Sat:1, Urg:1, Frus:1, Conf:1, Intent:Query

### Item 2.5
**Text:** "Just wanted to say I love your new app design."
**Correct:** Sat:5, Urg:1, Frus:1, Conf:1, Intent:Feedback

---

## Exercise 3: Topic Identification

### Item 3.1
**Text:** "I see a charge I don't recognize on my credit card."
**Correct:** Sat:2, Urg:3, Frus:3, Conf:3, Topic:Billing + Fraud

### Item 3.2
**Text:** "I can't log in to my net banking."
**Correct:** Sat:2, Urg:4, Frus:3, Conf:2, Topic:Account Access

### Item 3.3
**Text:** "What are the rates for your home loans?"
**Correct:** Sat:1, Urg:1, Frus:1, Conf:1, Topic:Product Inquiry

### Item 3.4
**Text:** "I will complain to RBI about this."
**Correct:** Sat:1, Urg:4, Frus:5, Conf:1, Topic:Regulatory Complaint

### Item 3.5
**Text:** "My UPI transaction failed but money was deducted."
**Correct:** Sat:1, Urg:4, Frus:4, Conf:3, Topic:Billing + Fraud

---

## Exercise 4: Multi-Label Detection

### Item 4.1
**Text:** "My account is locked. Also, what are your FD rates?"
**Correct:** Intent:Query + Request, Topic:Account Access + Product Inquiry

### Item 4.2
**Text:** "Fix this or I'll complain to your manager."
**Correct:** Intent:Request + Escalation

### Item 4.3
**Text:** "I'm frustrated with the charges. Can you reverse them?"
**Correct:** Intent:Complaint + Request, Topic:Billing

### Item 4.4
**Text:** "Why was I charged? Also, your app is good."
**Correct:** Intent:Query + Feedback, Topic:Billing + Account Access

### Item 4.5
**Text:** "I will contact the ombudsman and close my accounts."
**Correct:** Intent:Escalation + Complaint, Topic:Regulatory Complaint

---

## Exercise 5: Sarcasm Detection

### Item 5.1
**Text:** "Oh great, another fee. Wonderful."
**Correct:** Sat:1, Urg:2, Frus:4, Conf:1, Sarcasm:True

### Item 5.2
**Text:** "I cannot believe how quickly you resolved this. Amazing!"
**Correct:** Sat:5, Urg:1, Frus:1, Conf:1, Sarcasm:False

### Item 5.3
**Text:** "Thank you for charging me twice. Excellent service."
**Correct:** Sat:1, Urg:3, Frus:4, Conf:1, Sarcasm:True

### Item 5.4
**Text:** "Your system is working perfectly, as always."
**Correct:** Sat:2, Urg:2, Frus:4, Conf:1, Sarcasm:True

### Item 5.5
**Text:** "The agent was polite. My issue is still unresolved though."
**Correct:** Sat:2, Urg:3, Frus:3, Conf:1, Sarcasm:False

---

## Exercise 6: Code-Switched (Hinglish)

### Item 6.1
**Text:** "Mera account locked hai. Please check."
**Correct:** Sat:2, Urg:4, Frus:4, Conf:2

### Item 6.2
**Text:** "Yeh kya ho raha hai? My money is gone."
**Correct:** Sat:1, Urg:5, Frus:5, Conf:4

### Item 6.3
**Text:** "Kya aap FD rates bata sakte hain?"
**Correct:** Sat:1, Urg:1, Frus:1, Conf:1

### Item 6.4
**Text:** "Mujhe paisa chahiye urgently."
**Correct:** Sat:1, Urg:5, Frus:4, Conf:1

### Item 6.5
**Text:** "Bohot achha service hai! Thanks."
**Correct:** Sat:5, Urg:1, Frus:1, Conf:1

---

## Exercise 7: Regulatory Language

### Item 7.1
**Text:** "I am filing a formal complaint under RBI's Ombudsman scheme."
**Correct:** Sat:1, Urg:4, Frus:4, Conf:1, Intent:Escalation, Topic:Regulatory Complaint

### Item 7.2
**Text:** "This violates my consumer rights."
**Correct:** Sat:1, Urg:3, Frus:3, Conf:1, Intent:Escalation

### Item 7.3
**Text:** "I demand this be escalated under your complaints procedure."
**Correct:** Sat:1, Urg:4, Frus:3, Conf:1, Intent:Escalation

### Item 7.4
**Text:** "The bank has failed its duty of care."
**Correct:** Sat:1, Urg:2, Frus:2, Conf:1, Intent:Complaint

### Item 7.5
**Text:** "I will take legal action if this isn't resolved."
**Correct:** Sat:1, Urg:4, Frus:5, Conf:1, Intent:Escalation

---

## Exercise 8: Numerical Context

### Item 8.1
**Text:** "I was charged ₹500 extra."
**Correct:** Sat:2, Urg:2, Frus:3, Conf:1

### Item 8.2
**Text:** "I was charged ₹50,000 extra."
**Correct:** Sat:1, Urg:4, Frus:4, Conf:1

### Item 8.3
**Text:** "My pension of ₹35,000 didn't arrive."
**Correct:** Sat:1, Urg:5, Frus:4, Conf:1

### Item 8.4
**Text:** "I need ₹2,500 for medicine. Please check."
**Correct:** Sat:2, Urg:4, Frus:3, Conf:1

### Item 8.5
**Text:** "My daughter's college fees of ₹4,50,000 is due tomorrow."
**Correct:** Sat:1, Urg:5, Frus:5, Conf:1

---

## Exercise 9: Implicit Sentiment

### Item 9.1
**Text:** "My account has been locked for 3 days."
**Correct:** Sat:2, Urg:4, Frus:3, Conf:2

### Item 9.2
**Text:** "I'm still waiting for my refund."
**Correct:** Sat:2, Urg:3, Frus:3, Conf:1

### Item 9.3
**Text:** "Your agent said 24 hours. That was 3 days ago."
**Correct:** Sat:1, Urg:3, Frus:4, Conf:1

### Item 9.4
**Text:** "Third email. Same issue."
**Correct:** Sat:1, Urg:3, Frus:4, Conf:1

### Item 9.5
**Text:** "It's been 2 weeks. Still nothing."
**Correct:** Sat:1, Urg:3, Frus:4, Conf:1

---

## Exercise 10: Passive Aggression

### Item 10.1
**Text:** "As per my previous 5 emails, I'm still waiting."
**Correct:** Sat:1, Urg:3, Frus:5, Conf:1

### Item 10.2
**Text:** "I trust your team is well and not overburdened."
**Correct:** Sat:2, Urg:2, Frus:4, Conf:1

### Item 10.3
**Text:** "I remain hopeful this fifth attempt will merit a response."
**Correct:** Sat:2, Urg:3, Frus:4, Conf:1

### Item 10.4
**Text:** "I'm sure you're doing your best."
**Correct:** Sat:2, Urg:2, Frus:3, Conf:1

### Item 10.5
**Text:** "No rush. I've only been waiting 3 weeks."
**Correct:** Sat:1, Urg:3, Frus:5, Conf:1

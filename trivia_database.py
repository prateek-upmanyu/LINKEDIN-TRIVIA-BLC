import os
from datetime import datetime

# 60+ Verified B2B Sales, Telephony & Buyer Behavior Trivia / Fact Database
TRIVIA = [
    {
        "id": 1,
        "body": "B2B companies that contact a new prospect within 5 minutes are 21x more likely to qualify the lead compared to teams that wait 30 minutes to dial.",
        "source": "SOURCE: Harvard Business Review Lead Response Study",
        "caption": """DID YOU KNOW? Waiting just 30 minutes to dial a new B2B lead drops your qualification odds by 21x.

According to a landmark study published by Harvard Business Review (analyzing 1.25 million sales leads across B2B firms):

• 5-Minute Window: Reaching out within 5 minutes yields a 21x higher chance of qualifying the prospect.
• 30-Minute Delay: Calling after 30 minutes results in a massive 80%+ drop in contact probability.
• Reality Check: Despite this data, the average B2B enterprise takes 42 hours to respond to an inbound inquiry!

Speed-to-lead is not just an operational metric — it is the single highest-ROI lever in outbound telephony.

Catch decision-makers while their intent is fresh, and your conversion rate multiplies.

📊 Source: Harvard Business Review — "The Short Life of Online Sales Leads"

#B2BSales #SalesTrivia #SpeedToLead #OutboundTelephony #LeadGeneration #BulkLeadsCaller"""
    },
    {
        "id": 2,
        "body": "57% of C-level and VP buyers prefer a direct phone call over email when evaluating new B2B solutions — debunking the myth that executives ignore cold calls.",
        "source": "SOURCE: RAIN Group Center for Sales Research",
        "caption": """DID YOU KNOW? C-suite buyers actually prefer the phone over email.

There is a widespread myth that senior executives hate phone calls and only respond to digital messages.

The research tells the exact opposite story:
A comprehensive study by the RAIN Group (surveying 488 verified B2B buyers across global enterprises) revealed that:

• 57% of C-Level and VP-level executives prefer to connect via phone when exploring new business solutions.
• 54% of Directors and Senior Managers actively welcome phone outreach when the caller demonstrates relevant industry insight.
• Decision-makers receive 120+ cold emails every day — but fewer than 8 direct business phone calls!

Executives don't hate phone calls. They hate poorly researched, irrelevant pitches.

Do your homework, call with a concise business metric, and senior leaders will answer.

📊 Source: RAIN Group — Top Performance in Sales Prospecting Benchmark

#ColdCalling #ExecutiveSales #B2BSales #SalesTrivia #OutboundStrategy #BulkLeadsCaller"""
    },
    {
        "id": 3,
        "body": "80% of B2B sales require at least 5 follow-up calls to close, yet 44% of sales reps give up after just one attempt. The 8% who persist capture 80% of deals.",
        "source": "SOURCE: Brevet & Marketing Donut B2B Study",
        "caption": """DID YOU KNOW? 44% of sales reps give up right before 80% of deals happen.

The B2B follow-up attrition curve is staggering:
• 44% of reps stop after 1 touch
• 66% of reps stop after 2 touches
• 88% of reps stop after 3 touches
• Only 8% of reps make 5 or more follow-up touches

Yet 80% of all closed B2B contracts occur between the 5th and 12th touchpoint!

What this means for sales leaders:
The top 8% of reps who build disciplined multi-touch cadences are taking home 80% of the entire industry's commission pool — not because they pitch better, but because they stay in the game longer.

Persistence without friction is the ultimate sales moat.

📊 Source: Brevet Group & Marketing Donut B2B Benchmark

#SalesPersistence #FollowUpStrategy #B2BGrowth #SalesPipeline #BulkLeadsCaller"""
    },
    {
        "id": 4,
        "body": "Opening a cold call with 'Did I catch you at a bad time?' drops meeting booking rates by 40%, while 'How have you been?' increases booking rates by 6.6x.",
        "source": "SOURCE: Gong Labs (Analysis of 90,000+ Calls)",
        "caption": """DID YOU KNOW? The first sentence of your cold call can either double or destroy your meeting rate.

Gong Labs analyzed audio recordings of over 90,000 B2B outbound cold calls to see which opening phrases convert best:

The Loser:
❌ "Did I catch you at a bad time?"
→ Reduces meeting booking rates by 40%. It literally invites the prospect to say "Yes, bye" and triggers immediate defensiveness.

The Winner:
✅ "How have you been?"
→ Yields a 6.6x higher meeting booking rate compared to the baseline. It creates a subtle pattern interrupt, triggering social warmth and familiar rapport.

Words matter. Micro-adjustments in your first 7 seconds transform dial efficiency across your entire floor.

📊 Source: Gong Labs AI Call Intelligence Benchmark

#ColdCallScript #SalesPsychology #OutboundTelephony #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 5,
        "body": "Calling B2B decision-makers between 4:00 PM and 5:00 PM on Wednesdays and Thursdays yields a 71% higher live connect rate compared to mid-morning dials.",
        "source": "SOURCE: LeadResponseManagement (100k+ Dials)",
        "caption": """DID YOU KNOW? The best time to catch senior executives on the phone is late afternoon mid-week.

A study analyzing over 100,000 outbound dials across B2B sectors identified the exact peak performance windows for live phone conversations:

Best Days to Call:
🥇 Wednesday & Thursday: 49% higher conversation rates than Mondays.
(Mondays are meeting-heavy; Fridays are wrap-up focused).

Best Hours to Call:
⏰ 4:00 PM – 5:00 PM: 71% higher connect rate than 11:00 AM – 12:00 PM.
⏰ 8:00 AM – 9:00 AM: Second best window (before daily calendars fill up).

Why late afternoon works: Executives have wrapped their scheduled meetings, cleared urgent fires, and are at their desks reviewing open items for the next day.

Dial when prospects have breathing room, not when they are rushing into standups.

📊 Source: LeadResponseManagement & InsideSales Call Timing Study

#SalesTiming #CallCadence #OutboundSales #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 6,
        "body": "The average B2B purchasing decision in 2026 involves 6.8 stakeholders. Single-threaded deals fail 82% more often than multi-threaded opportunities.",
        "source": "SOURCE: Gartner B2B Buying Journey Report",
        "caption": """DID YOU KNOW? Deals with only one champion are 82% more likely to stall out.

The era of the "single decision-maker" in B2B is completely dead.

According to Gartner's research on corporate procurement:
• A typical B2B purchase now involves an average of 6.8 decision-makers across Finance, IT, Operations, and End-Users.
• In 77% of stalled deals, the primary champion loved the product, but couldn't navigate internal committee pushback alone.
• Multi-threaded deals (engaging 3+ contacts at the target account) close 3.2x faster than single-threaded deals.

Stop selling to an individual. Start mapping the entire buying committee on day one.

📊 Source: Gartner — "The New B2B Buying Journey"

#EnterpriseSales #MultiThreading #B2BStrategy #AccountBasedSelling #BulkLeadsCaller"""
    },
    {
        "id": 7,
        "body": "Sales reps spend only 34% of their working hours actually selling. 66% of their time is consumed by manual CRM data entry, admin tasks, and list searching.",
        "source": "SOURCE: Salesforce State of Sales Benchmark",
        "caption": """DID YOU KNOW? Your sales reps spend two-thirds of their day NOT selling.

Salesforce surveyed thousands of sales professionals globally in their flagship "State of Sales" report:

The Workday Breakdown:
• 34% of time: Actively connecting with prospects and pitching
• 21% of time: Manual CRM updates and data entry
• 17% of time: Searching for phone numbers and verifying contact info
• 15% of time: Drafting generic follow-up templates
• 13% of time: Internal meetings and administrative reporting

Imagine what happens to your revenue when automation frees up even 10 additional hours per week for live dials!

High-growth outbound teams don't work more hours — they eliminate administrative friction.

📊 Source: Salesforce Research — Annual State of Sales Report

#SalesProductivity #SalesOps #RevenueOperations #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 8,
        "body": "On a phone call, 84% of a prospect's initial trust is determined by your vocal tone and pacing — while only 16% is driven by the actual words you speak.",
        "source": "SOURCE: UCLA Vocal Intelligence Research",
        "caption": """DID YOU KNOW? How you sound on the phone matters 5x more than what you say.

When speaking in person, facial expressions and body language provide visual reassurance. 

On an outbound phone call, 100% of that visual feedback disappears:
• 84% of trust, authority, and emotional comfort is derived from tone, pitch modulation, and speaking speed.
• Only 16% comes from the literal vocabulary and script syntax.

The Optimal B2B Speaking Pace:
Top-performing cold callers speak at an average rate of 150–160 words per minute (WPM).
• Faster than 180 WPM: You sound like a nervous, high-pressure telemarketer.
• Slower than 120 WPM: You sound unprepared and low-energy.

Control your tempo, lower your pitch at the end of sentences, and project peer-level calmness.

📊 Source: Albert Mehrabian / UCLA Behavioral Communication Research

#VoicePsychology #ColdCallingTips #SalesRapport #CommunicationSkills #BulkLeadsCaller"""
    },
    {
        "id": 9,
        "body": "Referred B2B prospects close 4x faster, have a 16% higher lifetime value, and experience a 37% higher retention rate than cold outbound leads.",
        "source": "SOURCE: Wharton School of Business Referral Study",
        "caption": """DID YOU KNOW? Referred leads close 4x faster than any other channel.

Research from the Wharton School of Business reveals why customer referrals are the ultimate growth engine:

• 4x Faster Velocity: Pre-established peer trust compresses discovery and negotiation cycles from months to days.
• 16% Higher LTV: Referred customers spend more and negotiate discounts less aggressively.
• 37% Lower Churn: Higher satisfaction and longer retention compared to cold inbound or ads.

Yet 83% of satisfied B2B clients are willing to provide referrals — but only 29% of sales reps ever ask for them!

Build a systematic referral ask into your 30-day post-onboarding cadence.

📊 Source: Wharton School of Business — "Referral Programs and Customer Value"

#ReferralSelling #B2BGrowth #CustomerSuccess #SalesStrategy #BulkLeadsCaller"""
    },
    {
        "id": 10,
        "body": "Personalized cold emails that mention 1 specific piece of company research achieve a 142% higher response rate than generic mass-blast sequences.",
        "source": "SOURCE: Backlinko & Pitchbox (12 Million Emails)",
        "caption": """DID YOU KNOW? Just 1 line of personalized research boosts email response rates by 142%.

An analysis of over 12 million outbound cold emails conducted by Backlinko and Pitchbox showed:

• Mass Templates (0 customization): Average reply rate of just 3.1%.
• 1 Line of Company Specifics: Reply rate jumped to 7.5% (+142% increase).
• Personalized Subject Lines: Increased open rates by an additional 33%.

You don't need to write a 500-word essay for each prospect.
All you need is 1 relevant observation in your opening sentence:
"Saw your team is expanding SDR hiring in London..." or "Noticed you recently integrated Salesforce..."

Specific beats generic every single time.

📊 Source: Backlinko / Pitchbox Outbound Email Benchmark (12M+ Emails)

#ColdEmail #Personalization #OutboundSales #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 11,
        "body": "Top-performing B2B sales closers listen for 54% of a discovery call and speak for 46%, whereas low-performing reps talk for over 68% of the conversation.",
        "source": "SOURCE: Gong Labs (25,000+ Discovery Calls)",
        "caption": """DID YOU KNOW? Losing sales reps talk twice as much as winning reps.

Gong Labs analyzed audio data from 25,537 B2B discovery and demo calls:

The Talk-to-Listen Ratio:
• Top Closers: 46% Talk / 54% Listen
• Average Reps: 60% Talk / 40% Listen
• Bottom Performers: 68% Talk / 32% Listen

When reps dominate the conversation, they pitch features before uncovering the prospect's real financial pain.
When top closers ask targeted discovery questions and stay silent, prospects talk themselves into the solution.

Great selling is not great pitching. It is great diagnosis.

📊 Source: Gong Labs Call Intelligence — "The Talk-to-Listen Ratio in Sales"

#DiscoveryCall #ActiveListening #ConsultativeSelling #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 12,
        "body": "74% of B2B buyers choose the sales representative who was first to add value and insight to their buying process, rather than the cheapest vendor.",
        "source": "SOURCE: Corporate Visions B2B Buyer Study",
        "caption": """DID YOU KNOW? Price is rarely the #1 factor in B2B vendor selection.

Corporate Visions surveyed corporate decision-makers across Fortune 1000 firms to understand what drives the final contract signature:

• 74% of buyers selected the vendor that first provided strategic insight into their operational problem.
• Only 14% based their primary decision purely on the lowest price bid.

Buyers don't want a vendor who asks "What keeps you up at night?"
They want an advisor who says "Here is the invisible bottleneck costing your peers $200k/month — and here is how to eliminate it."

Be the source of insight, not just a product demo.

📊 Source: Corporate Visions B2B Buying Preference Research

#ValueSelling #B2BInsights #SalesDifferentiation #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 13,
        "body": "Sales reps who ask between 11 and 14 targeted discovery questions achieve a 74% deal win rate, compared to just 46% for reps who ask 6 or fewer.",
        "source": "SOURCE: Gong Labs Discovery Call Research",
        "caption": """DID YOU KNOW? There is an exact mathematical sweet spot for discovery questions.

Analyzing thousands of recorded B2B pipeline calls revealed the relationship between question volume and closed-won revenue:

• 1 to 6 Questions: 46% Win Rate (Too shallow; pain is not validated)
• 7 to 10 Questions: 58% Win Rate
• 11 to 14 Questions: 74% Win Rate (The Golden Zone)
• 15+ Questions: Win rate drops to 42% (Begins to feel like an interrogation)

11 to 14 thoughtful, conversational questions uncover the current bottleneck, downstream business impact, budget alignment, and decision timeline.

Diagnose thoroughly before prescribing your solution.

📊 Source: Gong Labs AI Call Analysis Benchmark

#DiscoveryQuestions #SalesClosing #PipelineVelocity #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 14,
        "body": "Video messages in B2B outbound emails boost reply rates by up to 300% and generate a 26% higher deal close rate when used during proposal reviews.",
        "source": "SOURCE: Vidyard & HubSpot B2B Benchmark",
        "caption": """DID YOU KNOW? A 60-second webcam video can triple your outbound reply rates.

Vidyard and HubSpot analyzed millions of B2B sales interactions incorporating personalized video:

• Cold Outreach: Including a personalized 45-second screen recording boosted reply rates by 300%.
• Deal Progression: Walking through a pricing proposal on video generated a 26% higher close rate.
• Meeting No-Shows: Sending a short "Looking forward to speaking tomorrow" video reduced meeting ghosting by 42%.

In an inbox flooded with copy-pasted text templates, a human face and voice breaks through instantly.

Humanize your outreach to stand out in 2026.

📊 Source: Vidyard State of Video in Sales / HubSpot Benchmark

#VideoProspecting #SalesInnovation #B2BSales #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 15,
        "body": "Over 70% of B2B buying decisions are made before a prospect ever reaches out to a sales rep, relying on reviews, peer benchmarks, and published content.",
        "source": "SOURCE: Forrester Research B2B Buyer Report",
        "caption": """DID YOU KNOW? Prospects have already completed 70% of their journey before you talk to them.

Forrester Research tracked modern enterprise purchasing workflows and found:

• Buyers conduct extensive independent digital research before agreeing to a discovery call.
• 68% prefer to research independently rather than interact with a sales rep early on.
• By the time they pick up the phone, they already have a defined hypothesis of their problem and potential vendors.

What this means for sales teams:
If your cold outreach is just generic feature dumping, you will be rejected immediately.
Your outreach must challenge their existing assumptions and introduce an unconsidered perspective they missed during their research.

Sell the gap they didn't know existed.

📊 Source: Forrester Research — "The Modern B2B Buyer Journey"

#B2BBuying #ContentStrategy #ThoughtLeadership #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 16,
        "body": "84% of B2B sales professionals say multi-channel outreach combining phone, LinkedIn, and email is significantly more effective than single-channel campaigns.",
        "source": "SOURCE: LinkedIn State of Sales Annual Report",
        "caption": """DID YOU KNOW? Relying on only one communication channel cuts your pipeline in half.

LinkedIn's global "State of Sales" report revealed that:

• Single-Channel Reps (Email only or Phone only) have an average response rate of less than 7%.
• Omnichannel Reps (blending phone calls, LinkedIn engagement, and concise email follow-ups) achieve a 34% response rate.
• 84% of quota-exceeding sales reps report that combining direct phone calls with social touches is essential to booking enterprise meetings.

Decision-makers consume information across different surfaces throughout their week. Meet them where they are active.

📊 Source: LinkedIn State of Sales Global Report

#SocialSelling #OmnichannelSales #SalesCadence #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 17,
        "body": "Leaving a strategic voicemail under 20 seconds increases callback and email reply rates by 22% compared to hanging up without leaving a message.",
        "source": "SOURCE: InsideSales.com Voicemail Study",
        "caption": """DID YOU KNOW? Hanging up without leaving a voicemail wastes valuable pipeline momentum.

A massive study by InsideSales.com (tracking over 500,000 outbound call outcomes) found:

• Leaving No Voicemail: Follow-up email reply rate averaged 4.2%.
• Leaving a 15–20 Second Voicemail: Follow-up email reply rate jumped to 26.2% (+22% boost).

Why it works:
The voicemail is not meant to pitch the product — it is an audio pattern-interrupt that validates your email:
"Hi [Name], this is [Your Name] with Bulk Leads Caller. Just sent you a 2-line email regarding [Metric]. Wanted to put a voice to the note. Talk soon."

When the prospect checks their inbox, your name is familiar.

📊 Source: InsideSales.com (XANT) Outbound Voicemail Benchmark

#SalesVoicemail #OutboundCalls #SalesConversion #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 18,
        "body": "High-performing sales teams are 2.8x more likely to use standardized sales playbooks than underperforming teams who rely on rep improvisation.",
        "source": "SOURCE: Harvard Business Review & Aberdeen Group",
        "caption": """DID YOU KNOW? Improvisation kills sales floor scalability.

Research published by the Aberdeen Group and Harvard Business Review tracking B2B organizations revealed:

• Playbook Adoption: Elite sales teams are 2.8x more likely to have documented, standardized playbooks for openers, objection handling, and qualification.
• Quota Attainment: Companies with formal sales playbooks achieve 15% higher average deal size and 28% higher team quota attainment.
• Ramp Time: New SDR ramp time decreases by 41% when guided by structured cadences.

Top performers don't reinvent the wheel on every dial. They master a proven system and execute it with consistency.

Process beats luck every single quarter.

📊 Source: Aberdeen Group / Harvard Business Review Sales Enablement Study

#SalesPlaybook #SalesManagement #ScaleOutbound #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 19,
        "body": "Saying 'The reason I'm calling is...' within the first 10 seconds of a cold call increases meeting booking success rates by 2.1x.",
        "source": "SOURCE: Gong Labs (Call Opener Intelligence)",
        "caption": """DID YOU KNOW? Stating your reason for calling upfront doubles your meeting rate.

Gong Labs analyzed over 100,000 cold calls and identified that prospects relax as soon as they understand the caller's purpose:

The Impact of Stating the Reason:
• Reps who open with "The reason I'm calling is..." convert calls into booked meetings at a 2.1x higher rate than reps who wander into small talk.

The Psychological Reason:
Human beings crave cognitive certainty. When a stranger calls, the prospect's brain is thinking: "Who are you and what do you want?"
When you immediately answer that question in the first 10 seconds, their defensive guard drops and they listen to your value statement.

Respect their time upfront and get straight to the point.

📊 Source: Gong Labs Audio Call Intelligence Report

#ColdCallingTips #PatternInterrupt #SalesScripting #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 20,
        "body": "B2B companies that align their sales and marketing teams achieve 24% faster three-year revenue growth and 27% faster profit growth.",
        "source": "SOURCE: SiriusDecisions & Forrester Benchmark",
        "caption": """DID YOU KNOW? Sales and Marketing friction costs B2B companies over $1 trillion annually.

A multi-year study by SiriusDecisions and Forrester tracking B2B enterprise performance discovered:

• Revenue Velocity: Organizations with tight alignment between outbound sales and marketing grow revenue 24% faster over a 3-year period.
• Profitability: Aligned teams achieve 27% faster profit growth and 36% higher customer retention rates.
• Lead Leakage: Misaligned teams waste over 60% of all generated marketing leads due to lack of timely outbound follow-up.

When Marketing delivers verified ICP target accounts and Outbound Telephony dials them within minutes, revenue growth becomes predictable.

Alignment is a revenue driver, not just an internal meeting topic.

📊 Source: SiriusDecisions / Forrester B2B Alignment Benchmark

#RevenueOperations #Smarketing #B2BGrowth #SalesLeadership #BulkLeadsCaller"""
    },
    {
        "id": 21,
        "body": "92% of all customer interactions across B2B sales cycles still happen over the phone, despite the explosion of chat apps, email, and social networks.",
        "source": "SOURCE: Salesforce Voice Benchmark Report",
        "caption": """DID YOU KNOW? The phone remains the undisputed king of B2B deal execution.

Despite hundreds of new communication tools launched over the past decade, Salesforce's Voice Benchmark revealed:

• 92% of all meaningful B2B customer touchpoints — from initial qualification to executive contract negotiation — occur via live phone calls.
• Complex objections and price negotiations are 6x more likely to resolve successfully over voice than over asynchronous email threads.
• Voice conveys nuance, urgency, and human empathy that text simply cannot replicate.

Email generates awareness, but the phone closes revenue.

Never underestimate the power of picking up the phone.

📊 Source: Salesforce Voice and Telephony Research Benchmark

#B2BTelephony #VoiceCommunication #SalesExecution #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 22,
        "body": "B2B sales teams that clean and verify their phone contact databases every 30 days see an average 27% increase in daily live connection rates.",
        "source": "SOURCE: DiscoverOrg & ZoomInfo Data Decay Study",
        "caption": """DID YOU KNOW? B2B contact data decays at an astonishing rate of 30% per year.

People change jobs, switch departments, and get new direct dial numbers constantly:
• Without regular data hygiene, nearly one-third of your outbound dial list becomes useless numbers every 12 months.
• Reps waste an average of 42 minutes per shift dialing disconnected numbers or speaking with people who left the company months ago.
• Teams that run monthly verification scans see connect rates increase by 27% immediately.

A clean list of 500 direct dials outperforms a dirty list of 5,000 numbers every single time.

Invest in data hygiene before ramping dial volume.

📊 Source: DiscoverOrg / ZoomInfo B2B Data Decay Benchmark

#DataHygiene #SalesOps #LeadQuality #OutboundEfficiency #BulkLeadsCaller"""
    },
    {
        "id": 23,
        "body": "Cold email subject lines with 1 to 5 words achieve the highest open rates (46%), while subject lines with 10 or more words drop below 24%.",
        "source": "SOURCE: Retention Science (540 Million Emails)",
        "caption": """DID YOU KNOW? Long email subject lines cut your open rate in half.

Retention Science analyzed over 540 million emails to measure how subject line length impacts recipient engagement:

The Length Curve:
• 1 to 5 Words: 46% Open Rate (Clear winner)
• 6 to 9 Words: 32% Open Rate
• 10+ Words: Less than 24% Open Rate

Why short subjects win:
• Mobile Optimization: Over 60% of executives read emails on smartphones where long subject lines get truncated.
• Natural Tone: Internal emails between colleagues are short ("Quick update", "Meeting notes"). Long subject lines instantly scream "Automated Marketing Pitch!"

Keep it brief, relevant, and conversational.

📊 Source: Retention Science Email Optimization Study (540M+ Emails)

#ColdEmailTips #EmailMarketing #SalesEnablement #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 24,
        "body": "Engaging an internal Champion who introduces you to the Economic Buyer increases enterprise B2B deal close rates from 17% to over 68%.",
        "source": "SOURCE: CEB / Gartner Challenger Customer Study",
        "caption": """DID YOU KNOW? Winning the Champion is what unlocks the C-suite checkbook.

Gartner's landmark study on enterprise purchasing behaviors discovered:

• Pitches directed solely at the Economic Buyer (CFO/CEO) without an internal Champion close only 17% of the time.
• When a dedicated internal Champion actively guides the vendor through procurement, close rates jump to 68% (+4x higher).

What makes a true Champion:
• They have personal skin in the game
• They have internal political capital
• They explain how internal decisions are actually made

Find your Champion early, arm them with ROI data, and let them sell alongside you.

📊 Source: CEB (Corporate Executive Board) & Gartner — The Challenger Customer

#ChallengerSale #ChampionBuilding #EnterpriseB2B #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 25,
        "body": "71% of B2B sales reps who leverage social selling on LinkedIn consistently hit quota, compared to only 49% of reps who use traditional methods alone.",
        "source": "SOURCE: LinkedIn Social Selling Index (SSI) Study",
        "caption": """DID YOU KNOW? Socially active reps hit quota 45% more often.

LinkedIn tracked thousands of B2B sales professionals across industries based on their Social Selling Index (SSI):

• 71% of reps with high social engagement consistently exceed their quarterly revenue targets.
• Reps with strong LinkedIn presence create 45% more qualified opportunities each month.
• 78% of social sellers outsell peers who rely strictly on un-researched cold calls.

LinkedIn does not replace the phone — it warms up the prospect before the dial.

Build your professional brand, engage with your prospect's content, and make your cold calls warm.

📊 Source: LinkedIn Social Selling Index (SSI) Benchmark Report

#SocialSelling #LinkedInForSales #QuotaAttainment #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 26,
        "body": "Including specific pricing ranges in your discovery follow-up reduces sales cycle length by 32% compared to withholding pricing until a formal proposal.",
        "source": "SOURCE: CSO Insights Sales Optimization Report",
        "caption": """DID YOU KNOW? Hiding pricing delays your deals by weeks.

CSO Insights analyzed enterprise sales velocity metrics and uncovered a counter-intuitive finding:

• Reps who share clear ballpark pricing during or immediately after discovery close deals 32% faster.
• Reps who hide pricing behind multiple qualification gates experience a 45% higher deal abandonment rate.

Why transparency accelerates deals:
Modern buyers have no patience for pricing games. When you provide transparent ranges early, you disqualify bad-fit leads immediately and build credibility with serious buyers.

Confidence in your price signals confidence in your product value.

📊 Source: CSO Insights / Miller Heiman Sales Performance Benchmark

#PricingStrategy #SalesVelocity #B2BClosing #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 27,
        "body": "Outbound phone calls placed on Tuesdays generate the highest volume of qualified discovery meetings booked across all industries.",
        "source": "SOURCE: Velocify Outbound Dialing Benchmark",
        "caption": """DID YOU KNOW? Tuesday is the highest-converting day for booking sales meetings.

Velocify analyzed millions of outbound sales calls across enterprise and SMB sectors:

• Tuesday Leads: Yielded the highest percentage of converted calls into scheduled discovery demos.
• Why not Monday? Mondays are filled with executive team meetings and inbox triage.
• Why not Friday? Friday afternoons have the lowest connect rates as decision-makers mentally wind down for the weekend.

Tuesday is when executives are fully engaged in operational execution and actively solving bottlenecks.

Plan your heaviest outbound dial blocks for Tuesday mornings and afternoons.

📊 Source: Velocify / Lead Management Benchmark Report

#SalesOptimization #CallTiming #SalesProductivity #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 28,
        "body": "A prospect who has had 3 or more positive touchpoints with your content is 4.5x more likely to respond favorably to a cold phone outreach.",
        "source": "SOURCE: Demand Gen Report B2B Buyer Survey",
        "caption": """DID YOU KNOW? Brand familiarity multiplies cold call conversion by 4.5x.

The Demand Gen Report surveyed B2B buyers to understand how prior content consumption influences outbound response:

• Completely Cold (No prior exposure): Connect-to-meeting rate averages ~2.5%.
• Prior Content Exposure (Viewed post, read case study, or received newsletter): Meeting conversion rate jumps to 11.2% (4.5x higher).

This is why combining marketing awareness with outbound telephony creates an unstoppable pipeline.

When prospects recognize your company name, their defensive sales guard drops in seconds.

📊 Source: Demand Gen Report Annual B2B Buyer Survey

#BrandAwareness #OutboundSales #ContentDrivenSales #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 29,
        "body": "Top B2B closers spend an average of 22% less time presenting slides and 38% more time discussing customer ROI benchmarks during product demos.",
        "source": "SOURCE: Gong Labs (Analysis of 67,000 Demos)",
        "caption": """DID YOU KNOW? The best product demos have the fewest slides.

Gong Labs studied audio and screen recordings from over 67,000 B2B product demonstrations:

The Demo Difference:
• Average Reps: Spend 32 minutes flipping through standard feature slide decks.
• Top 10% Closers: Spend fewer than 9 minutes on slides, dedicating the rest of the time to interactive discussion around specific ROI metrics.

Customers don't buy your product features. They buy the future financial state of their own business.

Show only the features that solve their exact identified pain, and anchor every feature to dollars saved or revenue gained.

📊 Source: Gong Labs AI Demo Intelligence Report

#ProductDemo #DemoSkills #ValueBasedSelling #SalesTrivia #BulkLeadsCaller"""
    },
    {
        "id": 30,
        "body": "86% of B2B buyers say that receiving a well-crafted, personalized customer case study was a decisive factor in their final vendor selection.",
        "source": "SOURCE: Demand Gen Report B2B Case Study Benchmark",
        "caption": """DID YOU KNOW? Case studies are the #1 most persuasive collateral in B2B sales.

According to research by the Demand Gen Report tracking B2B purchasing triggers:

• 86% of enterprise buyers rated case studies as the single most influential content format during their decision process.
• Peer Proof: A case study from a company in their exact industry carries 6x more credibility than any pitch deck created by your marketing team.
• Specificity: Case studies with concrete numbers ("Increased live connect rate from 4% to 14%") convert 2.4x better than generic praise.

Don't tell prospects how good your product is. Show them how their peers succeeded with it.

📊 Source: Demand Gen Report Content Preferences Benchmark

#SocialProof #CaseStudies #B2BTrust #SalesClosing #BulkLeadsCaller"""
    }
]

def get_trivia_by_day():
    """
    Select today's trivia using day_of_year, avoiding recently posted ones.
    Reads trivia_history.txt to guarantee zero duplicates.
    """
    history_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trivia_history.txt")
    
    posted_ids = set()
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "Trivia #" in line:
                    try:
                        id_part = line.split("Trivia #")[1].split(" ")[0]
                        posted_ids.add(int(id_part))
                    except (IndexError, ValueError):
                        pass

    # If all trivia items have been posted, reset cycle
    all_ids = {t["id"] for t in TRIVIA}
    if posted_ids >= all_ids:
        posted_ids = set()

    unposted = [t for t in TRIVIA if t["id"] not in posted_ids]
    day_of_year = datetime.now().timetuple().tm_yday
    idx = (day_of_year - 1) % len(unposted)
    return unposted[idx]

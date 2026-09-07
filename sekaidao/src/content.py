"""Page content for the Sekaidao site.

Copy is transcribed from the source mockups. Each page is an ordered list of
(component_name, kwargs) pairs rendered by `build.py`.

Mockup -> page mapping:
    image55  ->  /index.html
    image44  ->  /services/managed-it-support.html
    image0   ->  /services/microsoft-365.html
    image6   ->  /services/cybersecurity-compliance.html
    image3   ->  /services/cloud-migration-backup.html
    image4   ->  /services/it-consulting-vcio.html
    image1   ->  /about.html

Pages with no mockup (network setup, services index, blog, contact, FAQs) are
composed from the same components so they stay on-system.
"""

from components import CITY, EMAIL, PHONE, PHONE_HREF, SERVICES

# --------------------------------------------------------------------------
# Reusable fragments
# --------------------------------------------------------------------------
CTA_DEFAULT = dict(
    heading="Get expert IT help before small issues become big problems.",
    lede="Reliable support. Stronger security. A more productive business.",
)

TRUST_STANDARD = [
    ("mark:securityplus", "Security+ Certified", "CompTIA Security+ certified"),
    ("mark:aws", "AWS Solutions Architect Associate (In Progress)",
     "Continuing our commitment to cloud expertise"),
    ("headset", "Responsive Support", "Fast, friendly, and reliable help when you need it"),
    ("users", "Business-Focused IT", "Solutions designed for small business growth"),
]

# --------------------------------------------------------------------------
# Home  (mockup: image55)
# --------------------------------------------------------------------------
HOME = [
    ("hero", dict(
        image="hero-home.jpg",
        eyebrow="Managed IT Services for Small Businesses",
        h1="Reliable IT Support That Keeps Your Business Running.",
        lede="Proactive IT support, stronger security, and seamless technology so you "
             "can focus on what matters most — growing your business.",
    )),
    ("trustbar", dict(items=TRUST_STANDARD)),
    ("cards", dict(
        eyebrow="Our Services",
        heading="IT Solutions for a Stronger, More Productive Business",
        lede="Practical, reliable IT services designed to solve real business challenges.",
        cols=6, variant="service",
        items=[
            dict(icon="gear", question="Tired of recurring tech issues?",
                 title="Managed IT Support", link="/services/managed-it-support.html"),
            dict(icon="mark:microsoft", question="Need a smoother cloud workspace?",
                 title="Microsoft 365 Setup & Administration", link="/services/microsoft-365.html"),
            dict(icon="shield-check", question="Worried about cyber threats?",
                 title="Cybersecurity & Compliance", link="/services/cybersecurity-compliance.html"),
            dict(icon="cloud", question="Afraid of data loss or downtime?",
                 title="Cloud Migration & Backup", link="/services/cloud-migration-backup.html"),
            dict(icon="wifi", question="Slow or unreliable connectivity?",
                 title="Network Setup & Troubleshooting",
                 link="/services/network-setup-troubleshooting.html"),
            dict(icon="chart", question="Need strategic IT direction?",
                 title="IT Consulting / vCIO Services", link="/services/it-consulting-vcio.html"),
        ],
    )),
    ("cards", dict(
        bg="blue", cols=3, variant="row",
        eyebrow="Common Challenges, Real Solutions",
        heading="We Help You Overcome Today's IT Challenges",
        items=[
            dict(icon="clock", title="Downtime Disrupts Your Business", chip=True,
                 text="Minimize disruptions with proactive monitoring and fast response times."),
            dict(icon="dollar", title="Rising IT Costs", chip=True,
                 text="Get predictable, cost-effective solutions that deliver real value."),
            dict(icon="lock", title="Security Concerns", chip=True,
                 text="Protect your business with enterprise-grade security and expert guidance."),
        ],
    )),
    ("split", dict(
        image="founder.jpg",
        eyebrow="About Sekaidao",
        body_heading="Built on Service. Focused on Your Success.",
        body_paragraphs=[
            "Sekaidao was founded by an active duty IT systems administrator with U.S. Navy "
            "experience, bringing real-world expertise in access control, incident response, "
            "systems monitoring, and enterprise identity management to help small businesses "
            "operate more securely and efficiently.",
        ],
        cta=("Learn More About Us", "/about.html"),
        aside=[
            dict(icon="anchor", title="U.S. Navy Experience"),
            dict(icon="gear", title="Real-World Expertise"),
            dict(icon="users", title="Small Business Focus"),
            dict(icon="shield-check", title="A More Secure Tomorrow"),
        ],
    )),
    ("reviews", dict(
        eyebrow="What Our Clients Say",
        heading="Real Businesses. Real Results.",
        note="Can integrate reviews from Clutch or Google later.",
        items=[
            dict(title=f"Review Slot {n}",
                 quote="This is a placeholder for a future client review. "
                       "Your real reviews will go here.",
                 author="Business Owner, City, ST")
            for n in (1, 2, 3)
        ],
    )),
    ("posts", dict(
        eyebrow="Latest Insights",
        heading="From Our Blog",
        items=[
            dict(image=f"blog{n}.jpg", title=f"Blog Post Title Placeholder {n}",
                 text="A short description of the blog post will go here. "
                      "This is placeholder text for your latest article.")
            for n in (1, 2, 3)
        ],
    )),
    ("faqs", dict(
        heading="Quick Answers to Common Questions",
        cols=2, view_all=False, expanded=True,
        items=[
            ("How does Sekaidao operate?",
             "We take a proactive, partnership-based approach, monitoring your systems, "
             "preventing issues, and providing fast support when you need it."),
            ("What are your typical response times?",
             "We strive to respond to all support requests within 1 hour, with many issues "
             "resolved much faster."),
            ("What are your general policies?",
             "We operate with clear, transparent policies covering support, billing, and "
             "service delivery. Full details are provided during onboarding."),
            ("Do you offer refunds or guarantees?",
             "Yes. We stand behind our work with a satisfaction guarantee. If you're not "
             "happy, we'll make it right."),
        ],
    )),
    ("ctaband", dict(**CTA_DEFAULT)),
]

# --------------------------------------------------------------------------
# Managed IT Support  (mockup: image44)
# --------------------------------------------------------------------------
MANAGED = [
    ("hero", dict(
        image="hero-managed.jpg",
        crumbs=[("Home", "/index.html"), ("Services", "/services/index.html"),
                ("Managed IT Support", None)],
        h1="Managed IT Support",
        subhead="Proactive IT support that keeps your business running.",
        lede="Reduce downtime, prevent problems, and keep your team productive with reliable, "
             "proactive managed IT support from Sekaidao. We monitor, maintain, and support "
             "your systems so you can focus on what matters most — growing your business.",
        pills=[
            ("clock", "Proactive Monitoring", None),
            ("shield-check", "Faster Response Times", None),
            ("users", "People", "Stronger Businesses"),
        ],
    )),
    ("cards", dict(
        plain=True, cols=4,
        eyebrow="Common Challenges",
        heading="IT Issues Slow You Down. We Help You Move Forward.",
        lede="Many small businesses face the same frustrating IT challenges. "
             "We solve them with proactive support and expert care.",
        items=[
            dict(icon="warning", accent="orange", title="Recurring IT Issues",
                 text="The same problems keep happening, costing time and productivity."),
            dict(icon="clock", title="Unpredictable Downtime",
                 text="System outages disrupt your business and frustrate your team."),
            dict(icon="users", title="No Internal IT Team",
                 text="You don't have dedicated IT staff to handle day-to-day support "
                      "and strategic needs."),
            dict(icon="coins", title="Rising Support Costs",
                 text="Unexpected repair costs and break-fix support get expensive fast."),
        ],
    )),
    ("cards", dict(
        bg="soft", cols=6, variant="slim",
        eyebrow="What's Included",
        heading="Comprehensive IT Support for Your Business",
        lede="Our managed IT support includes everything you need to keep your systems "
             "secure, stable, and running smoothly.",
        items=[
            dict(icon="headset", title="Help Desk Support",
                 text="Fast, friendly support for your team via phone, email, or remote access."),
            dict(icon="laptop", title="Device Management",
                 text="Setup, configuration, and ongoing management of your computers, "
                      "servers, and devices."),
            dict(icon="users", title="User Support",
                 text="Help for your team with everyday IT issues, software, and account access."),
            dict(icon="monitor-chart", title="Monitoring & Maintenance",
                 text="24/7 system monitoring to detect and resolve issues before they "
                      "cause downtime."),
            dict(icon="gear", title="Patch Management",
                 text="Keep your systems, software, and devices up to date and protected "
                      "from vulnerabilities."),
            dict(icon="shield", title="Basic Security Oversight",
                 text="Ongoing security monitoring, threat detection, and best practice "
                      "enforcement."),
        ],
    )),
    ("process", dict(
        bg="blue", boxed=False, arrows=False,
        eyebrow="How It Works",
        heading="A Simple, Proactive Approach to IT Support",
        lede="We make managed IT support easy, with a clear process designed around your business.",
        steps=[
            dict(title="Assess Your Needs",
                 text="We take time to understand your business, systems, and goals."),
            dict(title="Set Up & Onboard",
                 text="We configure tools, monitoring, and support processes tailored "
                      "to your environment."),
            dict(title="Monitor & Support",
                 text="We proactively monitor your systems and provide fast support "
                      "when you need it."),
            dict(title="Keep You Moving",
                 text="We continuously optimize, improve, and help you plan for what's next."),
        ],
    )),
    ("cards", dict(
        cols=4, variant="navy",
        eyebrow="Real Results",
        heading="A More Productive Business Starts with Reliable IT",
        lede="Partner with Sekaidao and experience the difference proactive IT support can make.",
        items=[
            dict(icon="bolt", title="Faster Response Times",
                 text="Get help when you need it so your team stays productive."),
            dict(icon="chart", title="Fewer Disruptions",
                 text="Proactive monitoring helps prevent issues before they impact your business."),
            dict(icon="shield", title="Predictable Support Costs",
                 text="Flat-rate managed support helps you budget with confidence."),
            dict(icon="users", title="More Time to Focus",
                 text="Leave IT to us, so you can focus on growing your business."),
        ],
    )),
    ("faqs", dict(
        heading="Managed IT Support FAQs", cols=1, sign="plus", show_icon=False,
        items=[
            ("What does managed IT support include?",
             "Help desk support, device management, user support, 24/7 monitoring and "
             "maintenance, patch management, and basic security oversight — all covered "
             "under one predictable monthly plan."),
            ("How quickly can you respond to IT issues?",
             "We aim to respond to every support request within one hour. Urgent issues that "
             "stop your team working are triaged first, and many are resolved remotely the "
             "same day."),
            ("Is managed IT support cost-effective for small businesses?",
             "Yes. Flat-rate managed support replaces unpredictable break-fix invoices with a "
             "fixed monthly cost, and proactive monitoring prevents many of the expensive "
             "failures that would otherwise happen."),
        ],
    )),
    ("ctaband", dict(
        heading="Get expert IT support and keep your business moving.",
        lede="Reliable. Proactive. People-focused. Let's build a stronger, "
             "more secure business together.",
    )),
]

# --------------------------------------------------------------------------
# Microsoft 365  (mockup: image0)
# --------------------------------------------------------------------------
M365 = [
    ("hero", dict(
        image="hero-m365.jpg",
        eyebrow="Managed IT Services for Small Businesses",
        h1="Microsoft 365 Setup & Administration",
        lede="Get more from Microsoft 365. We set up, configure, and manage your Microsoft 365 "
             "environment — including email, Teams, SharePoint, OneDrive, and user management "
             "— so your team can collaborate securely and work from anywhere.",
        pills=[
            ("users", "Microsoft 365", "Certified Experts"),
            ("shield-check", "Secure & Compliant", "Setup"),
            ("badge-check", "Ongoing Support", "You Can Count On"),
        ],
    )),
    ("trustbar", dict(items=[
        ("mark:microsoft", "Microsoft Solutions Partner", "Modern Work"),
        ("users", "Experienced Microsoft 365 Experts", "Certified and trusted"),
        ("shield-check", "Secure & Compliant", "Best practices for business security"),
        ("cloud", "Productivity Focused", "Tools that help your team do more"),
        ("chart", "Business-Focused", "IT solutions designed for growth"),
    ])),
    ("cards", dict(
        cols=4,
        eyebrow="Solve Everyday Challenges",
        heading="Is Microsoft 365 Working for You?",
        lede="Many businesses struggle to get the most out of Microsoft 365. We help you "
             "overcome common challenges and turn Microsoft 365 into a powerful advantage.",
        items=[
            dict(icon="mail", accent="orange", title="Messy Email Setup",
                 text="Multiple inboxes, missing domains, and email issues that create confusion."),
            dict(icon="users", title="Poor Collaboration",
                 text="Teams, SharePoint, and OneDrive not set up properly leads to wasted "
                      "time and version conflicts."),
            dict(icon="lock", accent="orange", title="Access Confusion",
                 text="Unclear permissions and file access that put sensitive data at risk."),
            dict(icon="clock", title="Inefficient Onboarding",
                 text="New team members take too long to get set up and become productive."),
        ],
    )),
    ("cards", dict(
        bg="blue", cols=6, variant="slim",
        eyebrow="Our Service",
        heading="What's Included in Microsoft 365 Setup & Administration",
        lede="We handle the technical details so you can focus on your business.",
        items=[
            dict(icon="gear", title="Tenant Setup",
                 text="Initial setup and configuration of your Microsoft 365 tenant with "
                      "best practices."),
            dict(icon="users", title="User & License Management",
                 text="Add, remove, and manage users, groups, and licenses efficiently."),
            dict(icon="mail", title="Exchange / Outlook Setup",
                 text="Professional email setup, domain configuration, and Outlook support "
                      "across all devices."),
            dict(icon="chat", title="Teams & SharePoint Configuration",
                 text="Set up Teams, SharePoint, and OneDrive for secure, seamless collaboration."),
            dict(icon="shield-check", title="Security Baselines",
                 text="Implement security settings, MFA, and compliance best practices."),
            dict(icon="chart", title="Ongoing Administration",
                 text="Continuous management, updates, monitoring, and support as your "
                      "business grows."),
        ],
    )),
    ("split", dict(
        image="team.jpg",
        eyebrow="People Productivity Progress",
        body_heading="Smoother Onboarding. Simpler Administration.",
        body_paragraphs=[
            "We make it easy to bring new team members online and keep your Microsoft 365 "
            "environment running smoothly. From user setup and license management to ongoing "
            "support and troubleshooting, we're here to ensure your team stays productive, "
            "secure, and connected.",
        ],
        cta=True,
        aside=[
            dict(icon="users", title="Faster Employee Onboarding",
                 text="Get new hires productive from day one."),
            dict(icon="gear", title="Reliable Day-to-Day Administration",
                 text="We handle the details so you don't have to."),
            dict(icon="headset", title="Responsive Support",
                 text="Get help when you need it, from a team that knows your environment."),
        ],
    )),
    ("process", dict(
        eyebrow="A Simple, Proven Process",
        heading="From Setup to Ongoing Support",
        steps=[
            dict(title="Plan", text="We assess your needs, current environment, and goals."),
            dict(title="Configure",
                 text="We set up and configure Microsoft 365 with best practices."),
            dict(title="Migrate",
                 text="We help move your email, files, and data from your existing systems."),
            dict(title="Support",
                 text="We provide ongoing administration and support to keep you running smoothly."),
        ],
    )),
    ("faqs", dict(
        heading="Microsoft 365 Setup & Administration FAQs", cols=2,
        items=[
            ("How long does Microsoft 365 setup take?",
             "A typical small business tenant is configured within a few days. Larger "
             "migrations with mailboxes and file shares to move usually run one to three "
             "weeks, scheduled around your business hours."),
            ("Do you provide ongoing Microsoft 365 management?",
             "Yes. Ongoing administration covers user and license changes, security baseline "
             "maintenance, updates, monitoring, and day-to-day support for your team."),
            ("Can you help migrate our existing email and data?",
             "We migrate mailboxes, calendars, contacts, and files from most systems — "
             "including Google Workspace, on-premises Exchange, and IMAP hosts — with minimal "
             "disruption and no lost mail."),
            ("What about security and compliance?",
             "Every tenant we build gets security baselines, multi-factor authentication, and "
             "least-privilege permissions applied from day one, aligned to Microsoft's "
             "recommended practices."),
        ],
    )),
    ("ctaband", dict(**CTA_DEFAULT)),
]

# --------------------------------------------------------------------------
# Cybersecurity & Compliance  (mockup: image6)
# --------------------------------------------------------------------------
CYBER = [
    ("hero", dict(
        image="hero-cyber.jpg",
        eyebrow="Managed IT & Security for Small Businesses",
        h1="Cybersecurity & Compliance",
        lede="Protect your business from today's threats. We help small businesses improve "
             "their security posture, reduce risk, and build practical safeguards that keep "
             "operations running.",
        pills=[
            ("shield", "Security-Focused", "Approach"),
            ("gear", "Certified", "Experts"),
            ("chart", "Real-World", "Experience"),
        ],
    )),
    ("trustbar", dict(items=[
        ("mark:securityplus", "Security+ Certified", "Trusted security expertise."),
        ("shield-check", "Practical Solutions", "Built for small businesses."),
        ("users", "Business-Focused Security", "Keep your business productive and protected."),
        ("chart", "Stronger Together", "Your success is our mission."),
    ])),
    ("cards", dict(
        bg="blue", cols=4,
        eyebrow="Real Challenges. Real Risks.",
        heading="Common Security Concerns for Small Businesses",
        lede="You're not alone. These are the top concerns we hear from business owners.",
        items=[
            dict(icon="mail", title="Phishing & Social Engineering",
                 text="Worry about employees clicking on malicious links or fake emails."),
            dict(icon="lock", title="Weak Access Controls",
                 text="Concerned about who has access to your data and systems."),
            dict(icon="document", title="Compliance Uncertainty",
                 text="Not sure what regulations apply or how to meet client requirements."),
            dict(icon="warning", title="Fear of Breaches",
                 text="Worried about downtime, financial loss, and damage to your reputation."),
        ],
    )),
    ("cards", dict(
        cols=3, variant="row",
        eyebrow="Our Services",
        heading="What's Included in Our Cybersecurity & Compliance Services",
        lede="Practical, right-sized security solutions for small businesses.",
        items=[
            dict(icon="search", title="Security Assessments",
                 text="Identify vulnerabilities, evaluate your current security posture, and "
                      "provide clear, prioritized recommendations.",
                 link="/contact.html"),
            dict(icon="users", title="Identity & Access Controls",
                 text="Help you implement stronger user access management, multi-factor "
                      "authentication (MFA), and least-privilege principles.",
                 link="/contact.html"),
            dict(icon="laptop", title="Endpoint Security Guidance",
                 text="Recommend and help deploy protection for your computers, servers, "
                      "and mobile devices.",
                 link="/contact.html"),
            dict(icon="graduation", title="Security Awareness Support",
                 text="Educate your team on real-world threats like phishing, social "
                      "engineering, and safe practices.",
                 link="/contact.html"),
            dict(icon="document", title="Policy / Baseline Guidance",
                 text="Provide practical security policies and configuration guidelines "
                      "tailored to your business.",
                 link="/contact.html"),
            dict(icon="gear", title="Incident Response Readiness",
                 text="Help you prepare for and respond to security incidents with a clear, "
                      "step-by-step plan.",
                 link="/contact.html"),
        ],
    )),
    ("split", dict(
        image="security-mug.jpg",
        eyebrow="Practical Protection. Real Business Results.",
        body_heading="Security for the Way You Do Business",
        body_paragraphs=[
            "We deliver right-sized cybersecurity solutions that fit your business — no "
            "unnecessary complexity, no overkill. Our goal is to reduce risk, keep your data "
            "and systems secure, and give you the confidence to focus on what matters most: "
            "growing your business.",
        ],
        cta=True,
        aside=[
            dict(icon="shield-check", title="Security+ Certified"),
            dict(icon="users", title="Real-World Experience"),
            dict(icon="gear", title="Practical, Business-Focused"),
            dict(icon="chart", title="Ongoing Support"),
        ],
    )),
    ("split", dict(
        image="compliance.jpg", reverse=True, bg="soft",
        eyebrow="Compliance Support",
        body_heading="Help Meeting Client & Industry Requirements",
        body_paragraphs=[
            "We help small businesses align with common client requirements and industry "
            "expectations. From documentation to basic security best practices, we make "
            "compliance more manageable and less overwhelming.",
        ],
        checks=[
            "Guidance on common frameworks (e.g., HIPAA, CMMC, SOC 2)",
            "Help with required documentation and policies",
            "Practical steps to meet client security questionnaires",
            "Ongoing support as your business and requirements evolve",
        ],
    )),
    ("faqs", dict(
        heading="Cybersecurity & Compliance FAQs", cols=3, sign="plus", view_all=False,
        items=[
            ("Do small businesses really need cybersecurity?",
             "Yes. Small businesses are targeted precisely because attackers expect weaker "
             "defences. Most incidents we see start with ordinary phishing or a reused "
             "password, not a sophisticated attack."),
            ("What compliance frameworks do you support?",
             "We regularly help clients work toward HIPAA, CMMC, and SOC 2 expectations, and "
             "we support client-driven security questionnaires from larger partners."),
            ("How do we get started?",
             "We start with a security assessment: a review of your current posture, a clear "
             "list of prioritized findings, and a practical plan you can act on."),
        ],
    )),
    ("ctaband", dict(
        heading="Stronger Security. A Brighter Tomorrow.",
        lede="Get expert IT and cybersecurity support before small issues become big problems.",
    )),
]

# --------------------------------------------------------------------------
# Cloud Migration & Backup  (mockup: image3)
# --------------------------------------------------------------------------
CLOUD = [
    ("hero", dict(
        image="hero-cloud.jpg",
        eyebrow="Managed IT Services for Small Businesses",
        h1="Cloud Migration & Backup",
        lede="Move your systems and data to the cloud safely, improve your business "
             "resiliency, and reduce the risk of downtime or data loss. We make cloud "
             "adoption simple, secure, and worry-free.",
    )),
    ("trustbar", dict(items=[
        ("mark:securityplus", "Security+ Certified", "Our IT team is certified"),
        ("mark:aws", "AWS Solutions Architect Associate on Team",
         "Cloud expertise to design, migrate and manage"),
        ("headset", "Responsive Support", "Fast, friendly, and reliable help when you need it."),
        ("users", "Business-Focused IT", "Technology that supports real business growth."),
    ])),
    ("cards", dict(
        cols=4,
        eyebrow="Common Challenges",
        heading="Keeping Your Data Safe and Your Business Running Isn't Easy.",
        lede="Many businesses face real challenges when it comes to moving to the cloud "
             "and protecting their data.",
        items=[
            dict(icon="server", title="Outdated Systems",
                 text="Legacy systems are harder to maintain, less secure, and limit your "
                      "business potential."),
            dict(icon="warning", accent="orange", title="Fear of Disruption",
                 text="Worried that migration will cause downtime or disrupt your team's "
                      "productivity."),
            dict(icon="database", title="Unreliable Backups",
                 text="Inconsistent or incomplete backups put your business at risk of data loss."),
            dict(icon="question", title="Recovery Concerns",
                 text="Not knowing if you can quickly recover after a cyber attack, system "
                      "failure, or disaster."),
        ],
    )),
    ("cards", dict(
        bg="blue", cols=6, variant="slim",
        eyebrow="Our Solution",
        heading="Everything You Need for a Secure, Successful Cloud Journey.",
        lede="We handle the planning, migration, protection, and ongoing support — "
             "so you can focus on your business.",
        items=[
            dict(icon="clipboard", title="Migration Planning",
                 text="A detailed plan tailored to your business systems, timeline, and "
                      "potential risks.",
                 link="/contact.html", link_label="Learn More", caps=True),
            dict(icon="transfer", title="Data Transfer Support",
                 text="Secure and efficient transfer of your systems and data with minimal "
                      "disruption.",
                 link="/contact.html", link_label="Learn More", caps=True),
            dict(icon="database", title="Backup Strategy",
                 text="Reliable, automated backup solutions designed for your business needs.",
                 link="/contact.html", link_label="Learn More", caps=True),
            dict(icon="refresh", title="Recovery Readiness",
                 text="Tested recovery plans to ensure you can get back up and running quickly.",
                 link="/contact.html", link_label="Learn More", caps=True),
            dict(icon="cloud", title="Cloud Storage / Collaboration Support",
                 text="Set up and optimize cloud tools like Microsoft 365, Google Workspace, "
                      "and more.",
                 link="/contact.html", link_label="Learn More", caps=True),
            dict(icon="chart", title="Ongoing Monitoring",
                 text="Continuous monitoring and management to keep your data secure and "
                      "systems healthy.",
                 link="/contact.html", link_label="Learn More", caps=True),
        ],
    )),
    ("split", dict(
        image="continuity.jpg", body_first=True,
        eyebrow="Business Continuity",
        body_heading="Be Ready for What's Next.",
        body_paragraphs=[
            "A strong cloud and backup strategy keeps your business running through "
            "unexpected events. Whether it's a cyber attack, hardware failure, or natural "
            "disaster, we help you stay resilient with secure data, fast recovery, and "
            "minimal downtime.",
        ],
        cta=True,
        aside=[
            dict(icon="shield-check", title="Reduce Downtime",
                 text="Get back to business faster."),
            dict(icon="chart", title="Protect Your Data",
                 text="Keep your critical information safe."),
            dict(icon="users", title="Maintain Productivity",
                 text="Keep your team working from anywhere."),
            dict(icon="badge-check", title="Plan for the Unexpected",
                 text="Be prepared for whatever comes next."),
        ],
    )),
    ("process", dict(
        bg="blue", step_icons=True,
        eyebrow="Our Process",
        heading="A Simple, Proven Process.",
        lede="We make cloud migration and data protection easy with a structured, "
             "step-by-step approach.",
        steps=[
            dict(icon="search", title="Assess",
                 text="We evaluate your current systems, data, and business goals."),
            dict(icon="document", title="Plan",
                 text="We design a customized migration and backup strategy with minimal "
                      "disruption."),
            dict(icon="cloud-up", title="Migrate",
                 text="We securely move your systems and data to the cloud."),
            dict(icon="shield-check", title="Protect",
                 text="We implement backups, monitoring, and recovery plans for long-term "
                      "peace of mind."),
        ],
    )),
    ("faqs", dict(
        heading="Cloud Migration & Backup FAQs", cols=3,
        items=[
            ("Will there be downtime during migration?",
             "In most cases, we can minimize or eliminate downtime. We plan carefully to keep "
             "your business running throughout the process."),
            ("How often should backups run?",
             "We recommend automated daily backups for most businesses, with more frequent "
             "backups for critical systems or high-change data."),
            ("Do you help with recovery planning?",
             "Yes. We create and test recovery plans to ensure you can quickly restore your "
             "systems and data when needed."),
        ],
    )),
    ("ctaband", dict(**CTA_DEFAULT)),
]

# --------------------------------------------------------------------------
# IT Consulting / vCIO  (mockup: image4)
# --------------------------------------------------------------------------
VCIO = [
    ("hero", dict(
        image="hero-vcio.jpg",
        crumbs=[("Services", "/services/index.html"), ("IT Consulting / vCIO", None)],
        h1="IT Consulting / vCIO Services",
        lede="Strategic guidance to help your business make smarter technology decisions. "
             "We provide planning, budgeting, and roadmaps that align IT with your business goals.",
        pills=[
            ("users", "Strategic", "Partnership"),
            ("shield", "Business-Focused", "Recommendations"),
            ("chart", "Real Results", "for Growing Businesses"),
        ],
    )),
    ("cards", dict(
        cols=4,
        eyebrow="Common Challenges",
        heading="Stop Reacting. Start Planning.",
        lede="Many small businesses make technology decisions on a reactive basis. We help "
             "you move from firefighting to a strategic, proactive approach.",
        items=[
            dict(icon="warning", accent="orange", title="Reactive Decisions",
                 text="Solving problems as they happen instead of planning ahead."),
            dict(icon="question", title="Unclear Priorities",
                 text="Not knowing what to focus on or what will have the biggest impact."),
            dict(icon="coins", title="Wasteful Spending",
                 text="Investing in the wrong technology or more than you need."),
            dict(icon="map", accent="orange", title="Lack of a Roadmap",
                 text="No clear plan for the future, making it hard to grow with confidence."),
        ],
    )),
    ("cards", dict(
        bg="blue", cols=3, variant="row",
        eyebrow="Our IT Consulting Services",
        heading="What's Included in Our vCIO Services",
        lede="Practical, experienced guidance tailored to your business.",
        items=[
            dict(icon="calendar", title="IT Planning",
                 text="Develop short- and long-term IT plans that support your business goals.",
                 link="/contact.html", caps=True),
            dict(icon="road", title="Technology Roadmaps",
                 text="A clear, phased plan for your technology investments and digital "
                      "transformation.",
                 link="/contact.html", caps=True),
            dict(icon="coins", title="Budget Guidance",
                 text="Help you plan and prioritize IT spending to maximize value and ROI.",
                 link="/contact.html", caps=True),
            dict(icon="handshake", title="Vendor Coordination",
                 text="We work with your vendors to ensure the best solutions, pricing, "
                      "and support.",
                 link="/contact.html", caps=True),
            dict(icon="shield-check", title="Security Strategy Input",
                 text="Align your security strategy with industry best practices and "
                      "business risk.",
                 link="/contact.html", caps=True),
            dict(icon="chart", title="Growth & Scalability Planning",
                 text="Make sure your technology can scale as your business evolves.",
                 link="/contact.html", caps=True),
        ],
    )),
    ("split", dict(
        image="strategy.jpg", wide_media=True,
        eyebrow="What Is a vCIO?",
        body_heading="A Virtual CIO for Your Business",
        body_paragraphs=[
            "A vCIO (Virtual Chief Information Officer) gives you access to experienced, "
            "strategic IT leadership — without the cost of a full-time CIO. We take the time "
            "to understand your business, provide expert guidance, and help you make informed "
            "decisions that drive growth, efficiency, and security.",
        ],
        cta=True,
    )),
    ("cards", dict(
        bg="blue", cols=4, variant="row",
        eyebrow="Why Strategy Matters",
        heading="Better Decisions. A Stronger Business.",
        lede="A strategic approach to IT delivers measurable benefits for your business.",
        items=[
            dict(icon="chart", title="Higher Productivity",
                 text="Right technology helps your team do more."),
            dict(icon="dollar", title="Lower Costs",
                 text="Eliminate waste and invest smarter."),
            dict(icon="shield-check", title="Stronger Security",
                 text="Reduced risk and better preparedness."),
            dict(icon="users", title="Ready for Growth",
                 text="Scalable systems that support your future."),
        ],
    )),
    ("faqs", dict(
        heading="IT Consulting / vCIO Services FAQ", cols=2,
        items=[
            ("What is a vCIO and how is it different from IT support?",
             "IT support keeps your systems running day to day. A vCIO works a level above "
             "that — planning, budgeting, and roadmapping so your technology decisions serve "
             "your business strategy."),
            ("What does a typical engagement include?",
             "Regular strategy sessions, a maintained technology roadmap, budget planning, "
             "vendor coordination, and security strategy input — scaled to the size of "
             "your business."),
            ("Is vCIO only for larger businesses?",
             "No. Small businesses benefit most, because a vCIO gives you senior IT leadership "
             "without carrying the cost of a full-time CIO."),
            ("Can you help with budgeting and technology purchases?",
             "Yes. We help you plan spending, evaluate options against your actual needs, and "
             "negotiate with vendors so you invest in the right things at the right time."),
            ("How often do we meet?",
             "Most clients meet quarterly for strategy reviews, with additional sessions "
             "around budget cycles, major projects, or growth milestones."),
            ("How do we get started?",
             "We begin with a discovery conversation about your business and goals, followed "
             "by an assessment of your current environment and a first draft roadmap."),
        ],
    )),
    ("ctaband", dict(
        heading="Let's Build a Smarter IT Strategy Together.",
        lede="Get expert guidance and a clear plan for your business.",
    )),
]

# --------------------------------------------------------------------------
# Network Setup & Troubleshooting  (no mockup — built on the same system)
# --------------------------------------------------------------------------
NETWORK = [
    ("hero", dict(
        image="hero-managed.jpg",
        crumbs=[("Home", "/index.html"), ("Services", "/services/index.html"),
                ("Network Setup & Troubleshooting", None)],
        h1="Network Setup & Troubleshooting",
        subhead="Fast, reliable connectivity your team can count on.",
        lede="Slow Wi-Fi, dropped connections, and network bottlenecks cost your team hours "
             "every week. We design, install, and troubleshoot small business networks that "
             "stay fast, stable, and secure.",
        pills=[
            ("wifi", "Reliable Coverage", None),
            ("shield-check", "Secure by Design", None),
            ("headset", "Fast Troubleshooting", None),
        ],
    )),
    ("cards", dict(
        plain=True, cols=4,
        eyebrow="Common Challenges",
        heading="When the Network Slows Down, Everything Does.",
        lede="Connectivity problems rarely announce themselves clearly. These are the "
             "symptoms we're called in to fix.",
        items=[
            dict(icon="wifi", accent="orange", title="Dead Zones & Weak Wi-Fi",
                 text="Coverage gaps that leave parts of your office unable to work reliably."),
            dict(icon="clock", title="Slow, Inconsistent Speeds",
                 text="Video calls that drop and file transfers that crawl at the worst moments."),
            dict(icon="network", title="Ageing Equipment",
                 text="Consumer-grade routers and switches that were never built for a business."),
            dict(icon="lock", title="Unsecured Networks",
                 text="Flat networks and open guest Wi-Fi that expose your business systems."),
        ],
    )),
    ("cards", dict(
        bg="soft", cols=6, variant="slim",
        eyebrow="What's Included",
        heading="Networks Designed for the Way You Work",
        lede="From a single office to multiple sites, we handle the design, build, and "
             "ongoing support.",
        items=[
            dict(icon="clipboard", title="Site Survey & Design",
                 text="We map your space and usage to design coverage that actually matches "
                      "how you work."),
            dict(icon="wifi", title="Wi-Fi Deployment",
                 text="Business-grade access points positioned and tuned for full, reliable "
                      "coverage."),
            dict(icon="network", title="Switching & Cabling",
                 text="Structured cabling and managed switches that give you a clean, "
                      "documented foundation."),
            dict(icon="shield", title="Firewall & Segmentation",
                 text="Separate guest, staff, and device networks so a problem in one stays "
                      "in one."),
            dict(icon="monitor-chart", title="Performance Monitoring",
                 text="Continuous monitoring that flags saturation and failing hardware "
                      "before you notice."),
            dict(icon="headset", title="Troubleshooting & Support",
                 text="Fast diagnosis when something breaks, with a clear explanation of "
                      "what went wrong."),
        ],
    )),
    ("process", dict(
        bg="blue", step_icons=True,
        eyebrow="Our Process",
        heading="From Diagnosis to Dependable",
        lede="A structured approach that fixes the cause, not just the symptom.",
        steps=[
            dict(icon="search", title="Diagnose",
                 text="We measure real performance across your space to find the actual "
                      "bottleneck."),
            dict(icon="document", title="Design",
                 text="We propose a right-sized fix with clear costs and expected results."),
            dict(icon="gear", title="Deploy",
                 text="We install and configure the equipment, usually outside business hours."),
            dict(icon="shield-check", title="Monitor",
                 text="We keep watch on performance and health so problems stay solved."),
        ],
    )),
    ("faqs", dict(
        heading="Network Setup & Troubleshooting FAQs", cols=2,
        items=[
            ("Can you fix our Wi-Fi without replacing everything?",
             "Often, yes. Many coverage problems come down to placement, channel selection, "
             "or a single failing access point. We measure first and only recommend hardware "
             "where it is genuinely the cause."),
            ("Do you handle cabling as well as wireless?",
             "Yes. We coordinate structured cabling, patch panels, and managed switching so "
             "your wired and wireless networks work as one documented system."),
            ("Can you separate guest Wi-Fi from our business systems?",
             "That is standard practice in every network we build. Guest, staff, and device "
             "traffic are segmented so visitors never share a network with your business data."),
            ("How quickly can you respond to an outage?",
             "Network outages are treated as urgent. We begin remote diagnosis immediately and "
             "arrange an on-site visit the same day where the fault requires hands on hardware."),
        ],
    )),
    ("ctaband", dict(**CTA_DEFAULT)),
]

# --------------------------------------------------------------------------
# About  (mockup: image1)
# --------------------------------------------------------------------------
ABOUT = [
    ("hero", dict(
        image="hero-about.jpg",
        eyebrow="About Sekaidao",
        h1="Dependable IT Support for a Stronger Tomorrow.",
        lede="Cloud. Security. Support. Built for small businesses by someone who's been "
             "in the trenches.",
    )),
    ("trustbar", dict(items=[
        ("mark:securityplus", "Security+ Certified", "CompTIA Security+ certified"),
        ("mark:aws", "AWS Solutions Architect Associate (In Progress)",
         "Continuing our commitment to cloud expertise"),
        ("headset", "Responsive Support", "Fast, friendly, and reliable help when you need it"),
        ("users", "Business-Focused", "IT solutions designed for small business growth"),
    ])),
    ("split", dict(
        image="founder.jpg", wide_media=True,
        eyebrow="Our Story",
        body_heading="Built on Experience. Focused on You.",
        body_paragraphs=[
            "Sekaidao was founded by an active duty IT systems administrator with the U.S. "
            "Navy, currently supporting a high-level intelligence watchfloor environment.",
            "The founder brings hands-on experience in access control, incident response, "
            "systems monitoring, and enterprise identity management from a real operational "
            "setting, along with a Security Plus certification and progress toward the AWS "
            "Solutions Architect Associate certification as part of an ongoing path deeper "
            "into cloud and cybersecurity.",
            "Sekaidao was built on a simple idea, that small businesses deserve the same level "
            "of IT reliability and security that large enterprises take for granted, without "
            "the enterprise price tag or complexity. Whether it's day-to-day support, a cloud "
            "migration, or shoring up security fundamentals, Sekaidao brings military-grade "
            "discipline and real operational experience to every engagement.",
        ],
    )),
    ("cards", dict(
        bg="blue", cols=4,
        eyebrow="Our Values",
        heading="What Sets Sekaidao Apart",
        items=[
            dict(icon="target", title="Mission-Driven Support",
                 text="We approach every client relationship with a commitment to service, "
                      "integrity, and results."),
            dict(icon="shield-check", title="Security-Focused Mindset",
                 text="Security isn't an add-on — it's built into everything we do."),
            dict(icon="users", title="Small Business Partnership",
                 text="We take the time to understand your business and provide practical, "
                      "right-sized solutions that help you grow."),
            dict(icon="gear", title="Real Operational Experience",
                 text="Our real-world experience in high-stakes environments brings a higher "
                      "standard of discipline and problem-solving to your business."),
        ],
    )),
    ("cards", dict(
        cols=4, variant="row",
        eyebrow="Credentials & Experience",
        heading="A Foundation You Can Trust",
        items=[
            dict(icon="mark:securityplus", title="Security+ Certified",
                 text="CompTIA Security+ certification"),
            dict(icon="mark:aws", title="AWS Solutions Architect Associate (In Progress)",
                 text="Continuing to expand cloud expertise through formal certification."),
            dict(icon="anchor", title="U.S. Navy Experience",
                 text="Active duty IT systems administrator supporting a high-level "
                      "intelligence watchfloor environment."),
            dict(icon="chart", title="Practical SMB IT Support",
                 text="Hands-on experience delivering real solutions for small businesses."),
        ],
    )),
    ("process", dict(
        bg="blue", step_icons=True,
        eyebrow="Our Process",
        heading="A Simple, Proven Approach",
        steps=[
            dict(icon="search", title="Discover",
                 text="We learn about your business, challenges, and goals."),
            dict(icon="document", title="Assess",
                 text="We evaluate your current environment and identify opportunities."),
            dict(icon="gear", title="Implement",
                 text="We deliver and configure the right solutions for your needs."),
            dict(icon="headset", title="Support",
                 text="We provide ongoing support to keep your business running smoothly."),
        ],
    )),
    ("ctaband", dict(
        eyebrow="Let's Build a Stronger Business Together",
        heading="Need a dependable IT partner?",
        lede="Get expert IT support, cloud solutions, and security guidance tailored for "
             "your small business.",
    )),
    ("promos", dict(items=[
        dict(icon="chat", title="Frequently Asked Questions",
             text="Have questions about our services, process, or what it's like to work "
                  "with Sekaidao?",
             link="/faqs.html", link_label="View FAQs"),
        dict(icon="phone", title="Get In Touch",
             text="Ready to talk? We're here to help you build a more secure, "
                  "productive business.",
             link="/contact.html", link_label="Contact Us"),
    ])),
]

# --------------------------------------------------------------------------
# Services index  (no mockup)
# --------------------------------------------------------------------------
SERVICES_INDEX = [
    ("hero", dict(
        image="hero-cloud.jpg",
        eyebrow="Managed IT Services for Small Businesses",
        h1="IT Services Built Around Your Business",
        lede="Six focused services that cover everything a small business needs from IT — "
             "day-to-day support, secure cloud, and the strategy to tie it together.",
    )),
    ("trustbar", dict(items=TRUST_STANDARD)),
    ("cards", dict(
        cols=3, variant="row",
        eyebrow="Our Services",
        heading="Everything You Need, From One Partner",
        lede="Start with what hurts most today — we'll help you build from there.",
        items=[
            dict(icon="gear", title="Managed IT Support",
                 text="Proactive monitoring, help desk, device management, and patching "
                      "under one flat monthly rate.",
                 link="/services/managed-it-support.html"),
            dict(icon="mark:microsoft", title="Microsoft 365 Setup & Administration",
                 text="Tenant setup, email migration, Teams and SharePoint configuration, "
                      "and ongoing administration.",
                 link="/services/microsoft-365.html"),
            dict(icon="shield-check", title="Cybersecurity & Compliance",
                 text="Assessments, access controls, endpoint protection, and practical "
                      "help meeting client requirements.",
                 link="/services/cybersecurity-compliance.html"),
            dict(icon="cloud", title="Cloud Migration & Backup",
                 text="Planned migrations, automated backups, and tested recovery so an "
                      "outage never becomes a crisis.",
                 link="/services/cloud-migration-backup.html"),
            dict(icon="wifi", title="Network Setup & Troubleshooting",
                 text="Business-grade Wi-Fi, structured cabling, segmentation, and fast "
                      "diagnosis when something breaks.",
                 link="/services/network-setup-troubleshooting.html"),
            dict(icon="chart", title="IT Consulting / vCIO Services",
                 text="Strategic planning, budgeting, and roadmaps that align technology "
                      "with where your business is going.",
                 link="/services/it-consulting-vcio.html"),
        ],
    )),
    ("process", dict(
        bg="blue", step_icons=True,
        eyebrow="Our Process",
        heading="A Simple, Proven Approach",
        steps=[
            dict(icon="search", title="Discover",
                 text="We learn about your business, challenges, and goals."),
            dict(icon="document", title="Assess",
                 text="We evaluate your current environment and identify opportunities."),
            dict(icon="gear", title="Implement",
                 text="We deliver and configure the right solutions for your needs."),
            dict(icon="headset", title="Support",
                 text="We provide ongoing support to keep your business running smoothly."),
        ],
    )),
    ("ctaband", dict(**CTA_DEFAULT)),
]

# --------------------------------------------------------------------------
# Blog / Contact / FAQs  (no mockup — composed from the same system)
# --------------------------------------------------------------------------
_POSTS = [
    ("blog1.jpg", "Operations",
     "Blog Post Title Placeholder 1",
     "A short description of the blog post will go here. This is placeholder text for "
     "your latest article."),
    ("blog2.jpg", "Cloud",
     "Blog Post Title Placeholder 2",
     "A short description of the blog post will go here. This is placeholder text for "
     "your latest article."),
    ("blog3.jpg", "Security",
     "Blog Post Title Placeholder 3",
     "A short description of the blog post will go here. This is placeholder text for "
     "your latest article."),
]

_BLOG_CARDS = "".join(
    f'<article class="postcard"><img src="static/img/{img}" alt="" loading="lazy">'
    f'<div class="postcard__body"><div class="postcard__meta">{cat}</div>'
    f"<h3>{title}</h3><p>{text}</p>"
    f'<a class="arrow-link" href="#">Read More'
    f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
    f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    f'<path d="M4 12h15M13 6l6 6-6 6"/></svg></a></div></article>'
    for img, cat, title, text in _POSTS
)

BLOG = [
    ("rich", dict(html=f"""
<section class="pagehead">
  <div class="container">
    <span class="eyebrow">Latest Insights</span>
    <h1>From Our Blog</h1>
    <p>Practical guidance on IT support, cloud, and security for small businesses.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid--3">{_BLOG_CARDS}</div>
  </div>
</section>""")),
    ("ctaband", dict(**CTA_DEFAULT)),
]

_SERVICE_OPTIONS = "".join(f"<option>{name}</option>" for name, _ in SERVICES)

CONTACT = [
    ("rich", dict(html=f"""
<section class="pagehead">
  <div class="container">
    <span class="eyebrow">Get In Touch</span>
    <h1>Let's Talk About Your IT</h1>
    <p>Tell us what's slowing your business down and we'll come back with a clear,
       right-sized recommendation — no obligation.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split split--reverse">
      <div class="split__body">
        <span class="eyebrow">Request a Free Quote</span>
        <h2>Tell us what you need</h2>
        <form class="form" data-quote-form novalidate>
          <div class="form__row">
            <div class="field"><label for="name">Name</label>
              <input id="name" name="name" type="text" autocomplete="name" required></div>
            <div class="field"><label for="company">Company</label>
              <input id="company" name="company" type="text" autocomplete="organization"></div>
          </div>
          <div class="form__row">
            <div class="field"><label for="email">Email</label>
              <input id="email" name="email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="phone">Phone</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel"></div>
          </div>
          <div class="field"><label for="service">What can we help with?</label>
            <select id="service" name="service">
              <option>I'm not sure yet</option>{_SERVICE_OPTIONS}
            </select></div>
          <div class="field"><label for="message">How can we help?</label>
            <textarea id="message" name="message"
              placeholder="Tell us a little about your business and what you're running into."></textarea></div>
          <div>
            <button class="btn btn--primary" type="submit">Send Request
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
                   stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M4 12h15M13 6l6 6-6 6"/></svg></button>
          </div>
          <p class="form__note" data-form-note>We typically reply within one business hour.</p>
        </form>
      </div>
      <figure class="media" style="margin:0">
        <img src="static/img/continuity.jpg" alt="" loading="lazy">
      </figure>
    </div>
  </div>
</section>
<section class="section section--blue">
  <div class="container">
    <div class="grid grid--3">
      <div class="card card--row"><span class="chip">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
             stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M6.6 3h3l1.5 4-2 1.5a12 12 0 006.4 6.4l1.5-2 4 1.5v3a2 2 0 01-2.2 2A17.5 17.5 0 014.5 5.2 2 2 0 016.6 3z"/>
        </svg></span>
        <div><h3>Call us</h3><p><a href="{PHONE_HREF}">{PHONE}</a></p></div></div>
      <div class="card card--row"><span class="chip">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
             stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="M3 6.5l9 6.5 9-6.5"/>
        </svg></span>
        <div><h3>Email us</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
      <div class="card card--row"><span class="chip">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"
             stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M12 21s7-6.1 7-11a7 7 0 10-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>
        </svg></span>
        <div><h3>Where we are</h3><p>{CITY}</p></div></div>
    </div>
  </div>
</section>""")),
    ("ctaband", dict(**CTA_DEFAULT)),
]

FAQS = [
    ("rich", dict(html="""
<section class="pagehead">
  <div class="container">
    <span class="eyebrow">Frequently Asked Questions</span>
    <h1>Answers to Common Questions</h1>
    <p>How we work, what we cover, and what to expect when you partner with Sekaidao.</p>
  </div>
</section>""")),
    ("faqs", dict(
        heading="Working With Sekaidao", eyebrow="General", cols=2, view_all=False,
        items=[
            ("How does Sekaidao operate?",
             "We take a proactive, partnership-based approach, monitoring your systems, "
             "preventing issues, and providing fast support when you need it."),
            ("What are your typical response times?",
             "We strive to respond to all support requests within 1 hour, with many issues "
             "resolved much faster."),
            ("What are your general policies?",
             "We operate with clear, transparent policies covering support, billing, and "
             "service delivery. Full details are provided during onboarding."),
            ("Do you offer refunds or guarantees?",
             "Yes. We stand behind our work with a satisfaction guarantee. If you're not "
             "happy, we'll make it right."),
            ("What size businesses do you work with?",
             "Most of our clients run between 5 and 75 people. That is the range where our "
             "flat-rate model and hands-on approach deliver the most value."),
            ("Do you require a long-term contract?",
             "Managed support runs on a rolling monthly agreement. Project work is quoted "
             "and scoped separately before anything begins."),
        ],
    )),
    ("faqs", dict(
        heading="Services & Delivery", eyebrow="Services", cols=2, bg="soft", view_all=False,
        items=[
            ("What does managed IT support include?",
             "Help desk support, device management, user support, 24/7 monitoring and "
             "maintenance, patch management, and basic security oversight."),
            ("Can you help migrate our existing email and data?",
             "Yes — mailboxes, calendars, contacts, and files from Google Workspace, "
             "on-premises Exchange, and IMAP hosts, with minimal disruption."),
            ("Will there be downtime during migration?",
             "In most cases, we can minimize or eliminate downtime. We plan carefully to keep "
             "your business running throughout the process."),
            ("How often should backups run?",
             "We recommend automated daily backups for most businesses, with more frequent "
             "backups for critical systems or high-change data."),
            ("What compliance frameworks do you support?",
             "We regularly help clients work toward HIPAA, CMMC, and SOC 2 expectations, and "
             "support client-driven security questionnaires from larger partners."),
            ("Do small businesses really need cybersecurity?",
             "Yes. Small businesses are targeted precisely because attackers expect weaker "
             "defences. Most incidents start with ordinary phishing or a reused password."),
        ],
    )),
    ("ctaband", dict(**CTA_DEFAULT)),
]

# --------------------------------------------------------------------------
# Page registry
# --------------------------------------------------------------------------
PAGES = {
    "/index.html": dict(
        title="Sekaidao | Reliable IT Support for Small Businesses",
        description="Proactive managed IT support, Microsoft 365, cybersecurity, and cloud "
                    "services for small businesses in Philadelphia, PA.",
        blocks=HOME,
        footer=dict(partner=False, socials=("linkedin", "x", "youtube")),
    ),
    "/services/index.html": dict(
        title="IT Services for Small Businesses | Sekaidao",
        description="Managed IT support, Microsoft 365, cybersecurity, cloud migration, "
                    "networking, and vCIO services from one partner.",
        blocks=SERVICES_INDEX,
    ),
    "/services/managed-it-support.html": dict(
        title="Managed IT Support | Sekaidao",
        description="Proactive managed IT support that reduces downtime, prevents problems, "
                    "and keeps your team productive.",
        blocks=MANAGED,
        footer=dict(partner="tomorrow",
                    socials=("linkedin", "facebook", "youtube", "instagram")),
    ),
    "/services/microsoft-365.html": dict(
        title="Microsoft 365 Setup & Administration | Sekaidao",
        description="Microsoft 365 tenant setup, email migration, Teams and SharePoint "
                    "configuration, security baselines, and ongoing administration.",
        blocks=M365,
    ),
    "/services/cybersecurity-compliance.html": dict(
        title="Cybersecurity & Compliance | Sekaidao",
        description="Security assessments, access controls, endpoint guidance, and practical "
                    "compliance support for small businesses.",
        blocks=CYBER,
        footer=dict(partner=False, socials=("linkedin", "x", "youtube")),
    ),
    "/services/cloud-migration-backup.html": dict(
        title="Cloud Migration & Backup | Sekaidao",
        description="Plan, migrate, and protect your data in the cloud with reliable backups "
                    "and tested recovery.",
        blocks=CLOUD,
        footer=dict(partner=False),
    ),
    "/services/network-setup-troubleshooting.html": dict(
        title="Network Setup & Troubleshooting | Sekaidao",
        description="Business-grade Wi-Fi, structured cabling, network segmentation, and fast "
                    "troubleshooting for small businesses.",
        blocks=NETWORK,
        footer=dict(partner=False),
    ),
    "/services/it-consulting-vcio.html": dict(
        title="IT Consulting / vCIO Services | Sekaidao",
        description="Strategic IT planning, technology roadmaps, budget guidance, and vCIO "
                    "leadership for growing small businesses.",
        blocks=VCIO,
        footer=dict(partner=False),
    ),
    "/about.html": dict(
        title="About Sekaidao | Dependable IT Support",
        description="Founded by an active duty U.S. Navy IT systems administrator, Sekaidao "
                    "brings military discipline and real operational experience to small "
                    "business IT.",
        blocks=ABOUT,
        footer=dict(partner=False),
    ),
    "/blog.html": dict(
        title="Blog | Sekaidao",
        description="Practical guidance on IT support, cloud, and security for small businesses.",
        blocks=BLOG,
        footer=dict(partner=False),
    ),
    "/contact.html": dict(
        title="Contact Sekaidao | Get a Free Quote",
        description=f"Call {PHONE} or send a message. We typically reply within one "
                    "business hour.",
        blocks=CONTACT,
        footer=dict(partner=False),
    ),
    "/faqs.html": dict(
        title="FAQs | Sekaidao",
        description="How we work, what we cover, and what to expect when you partner "
                    "with Sekaidao.",
        blocks=FAQS,
        footer=dict(partner=False),
    ),
}

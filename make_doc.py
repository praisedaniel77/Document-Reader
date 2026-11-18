from fpdf import FPDF

text = """Prestige Observability Platform - Internal Documentation

1. Overview
Prestige is Acme's internal observability platform. It collects metrics, logs and traces from all production services.

2. Alert policy
Critical alerts page the on-call engineer through the pager rotation named Falcon. Warning alerts go to the #prestige-alerts channel.

3. Data retention
Metrics are kept for 45 days. Logs are kept for 14 days. Traces are kept for 7 days.

4. Onboarding
New services must register with Prestige using the command: prestige-cli register --service NAME. Registration needs approval from the platform lead, Ngozi Bello.

5. Dashboards
Every service gets a default dashboard named after the service. Custom dashboards must be reviewed by two engineers before publishing.
"""

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 8, text)
pdf.output("knowledge/Prestige_Observability_Platform_Docs.pdf")
print("created")

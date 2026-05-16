import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.pdfgen import canvas

class EliteNumberedCanvas(canvas.Canvas):
    """Advanced canvas driving professional grid overlays, thin borders, and dynamic footer telemetry."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Clean Dark Green border wrap
        self.setStrokeColor(colors.HexColor("#133B2E"))
        self.setLineWidth(0.75)
        self.rect(0.5 * inch, 0.5 * inch, 7.5 * inch, 10 * inch)

        # Upper Running Header Rule
        self.setStrokeColor(colors.HexColor("#E6DFD3"))
        self.setLineWidth(0.5)
        self.line(0.5 * inch, 10.1 * inch, 8.0 * inch, 10.1 * inch)

        # Telemetry Data Elements
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#2C4A3E"))
        self.drawString(0.55 * inch, 10.18 * inch, "THERMO FISHER JIC NATIONAL ENTRY")
        self.drawRightString(7.95 * inch, 10.18 * inch, "CATEGORY: ENVIRONMENTAL & PLANT SCIENCES")

        # Lower Running Footer Elements
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#2C4A3E"))
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(7.85 * inch, 0.65 * inch, footer_text)
        self.drawString(0.65 * inch, 0.65 * inch, "Research Candidate: Geeta Putlur — Project Code: ENV-2026")
        self.restoreState()

def create_publication_chart():
    """Generates a high-density vector horizontal bar graph using a cream and dark green hierarchy."""
    d = Drawing(500, 150)
    # Background warm cream container
    d.add(Rect(0, 0, 500, 150, fillColor=colors.HexColor("#FAF6EE"), strokeColor=colors.HexColor("#D1C7BD"), strokeWidth=0.5))

    # 3-Hour Mean Remediation Metrics
    data = [
        ("Biochar + AMF Fungi Grid", 86.68, 7.94, "#0D2B21"),  # Primary Extra Deep Forest Green
        ("AMF Fungi Standalone", 85.13, 2.64, "#1E4D3E"),      # Classic Dark Green
        ("Biochar Standalone", 78.15, 24.80, "#446B5A"),       # Muted Medium Green
        ("Sterile Soil Baseline", 71.29, 15.00, "#739686"),     # Pale Sage Green
    ]

    # Plotting loop with precise positioning matrices
    y_pos = 115
    for label, val, sd, hex_color in data:
        # Clear Data Text Label
        d.add(String(15, y_pos + 3, label, fontName="Helvetica-Bold", fontSize=9, fillColor=colors.HexColor("#0D2B21")))

        # Map percentages to structural chart widths
        bar_width = (val / 100.0) * 230
        d.add(Rect(165, y_pos, bar_width, 14, fillColor=colors.HexColor(hex_color), strokeColor=None))

        # Metrics readouts positioned directly on the bar threshold boundary
        metric_str = f"{val}% [SD &plusmn; {sd}%]"
        d.add(String(175 + bar_width, y_pos + 3, metric_str, fontName="Helvetica", fontSize=8.5, fillColor=colors.HexColor("#0D2B21")))

        y_pos -= 28

    # Appending the Negative Source Control Element Cleanly
    d.add(String(15, 10, "Chamber Control (No Plant)", fontName="Helvetica-Bold", fontSize=9, fillColor=colors.HexColor("#0D2B21")))
    d.add(Rect(165, 7, 35, 14, fillColor=colors.HexColor("#802219"), strokeColor=None)) # Dark Red warning indicator for failure axis
    d.add(String(210, 10, "[Source Leak / Chamber Saturation: Net Increase +96.46% | SD &plusmn; 103.4%]", fontName="Helvetica-Oblique", fontSize=8, fillColor=colors.HexColor("#802219")))

    return d

def build_pdf(filename="ThermoFisher_Cream_Green_Visual_Aid.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.8 * inch,
        bottomMargin=0.9 * inch
    )

    styles = getSampleStyleSheet()

    # Sophisticated Academic Typography Framework - Cream & Dark Green Themes
    title_style = ParagraphStyle('EliteTitle', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor("#133B2E"), spaceAfter=3, alignment=1)
    subtitle_style = ParagraphStyle('EliteSub', fontName='Helvetica', fontSize=9.5, leading=12, textColor=colors.HexColor("#4A6B5D"), spaceAfter=14, alignment=1)

    h1_style = ParagraphStyle('EliteH1', fontName='Helvetica-Bold', fontSize=11.5, leading=14, textColor=colors.HexColor("#133B2E"), spaceBefore=11, spaceAfter=5, keepWithNext=True)
    body_style = ParagraphStyle('EliteBody', fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor("#25332E"), spaceAfter=6, alignment=4) # Justified
    bullet_style = ParagraphStyle('EliteBullet', parent=body_style, leftIndent=10, firstLineIndent=-7, spaceAfter=3.5)
    caption_style = ParagraphStyle('EliteCaption', fontName='Helvetica-Oblique', fontSize=7.5, leading=10, textColor=colors.HexColor("#4A6B5D"), spaceAfter=4, spaceBefore=2)

    story = []

    # ==========================================
    # PAGE 1: MACRO OVERVIEW, METABOLISM & ARREST SYSTEM
    # ==========================================
    story.append(Paragraph("Fungi-Powered Phytoremediation: How Mycorrhizal Soil Amendments Enhance Spider Plant Formaldehyde Removal", title_style))
    story.append(Paragraph("<b>Candidate Name: Geeta Putlur</b> &bull; Phase II Continuation Framework &bull; Academic Visual Record", subtitle_style))

    col1_content = [
        Paragraph("The Epidemiological Imperative", h1_style),
        Paragraph("&bull; <b>Carcinogenic Threat Base:</b> Gaseous Formaldehyde (HCHO) is categorized universally as a dangerous Group 1 human carcinogen, actively driving nasopharyngeal malignancies and chronic respiratory track disease parameters.", bullet_style),
        Paragraph("&bull; <b>Exposure Bottlenecks:</b> Global urban cohorts spend roughly 90% of their lifespans inside tightly sealed building shells, where modern insulation arrays systematically trap hazardous outgassing.", bullet_style),
        Paragraph("&bull; <b>Concentration Ratios:</b> Indoor air matrices display baseline pollutant concentrations that scale 2x to 5x higher than surrounding outdoor environments, presenting an immediate consumer health risk.", bullet_style)
    ]

    col2_content = [
        Paragraph("The Mycorrhizal Architecture", h1_style),
        Paragraph("Arbuscular Mycorrhizal Fungi (AMF) establish an obligatory symbiote relationship within the radical systems of <i>Chlorophytum comosum</i>. The microscopic fungal structures penetrate the plant cortical boundaries, developing intricate internal arbuscule node grids. This structural integration scales the total functional root absorption interface area by a factor of 10x to 100x, creating an expansive biological bio-filter grid capable of rapid gaseous molecular capture.", body_style)
    ]

    p1_grid = Table([[col1_content, col2_content]], colWidths=[245, 245], spaceAfter=10)
    p1_grid.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('RIGHTPADDING', (0,0), (0,0), 10),
        ('LEFTPADDING', (1,0), (1,0), 10),
    ]))
    story.append(p1_grid)

    # Pathway Box styled in Cream and Soft Forest Border
    pathway_box = [[Paragraph("<b>[BIOLOGICAL SYSTEM CONTROL FLOW: ENZYMATIC DEGRADATION MODEL]</b><br/>Airborne HCHO Capture &rarr; Root Zone Stomatal Ingestion &rarr; Hyphae Matrix Transport &rarr; Formaldehyde Dehydrogenase Pathway Cleavage &rarr; Metabolic Conversion to Safe Plant Formates &rarr; Calvin Cycle Biomass Fixation", ParagraphStyle('PathTxt', parent=body_style, alignment=1, fontSize=8, textColor=colors.HexColor("#133B2E"), leading=11))]]
    pathway_table = Table(pathway_box, colWidths=[490], spaceAfter=4)
    pathway_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FDFBF7")), # True rich cream background
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#4A6B5D")),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(pathway_table)
    story.append(Paragraph("Figure 1.1: Functional schematic model of systemic enzymatic breakdown. Logical workflow mapped independently by Geeta Putlur.", caption_style))

    story.append(Paragraph("Experimental Chamber Boundary Configurations", h1_style))
    story.append(Paragraph("To rigorously test this botanical defense system, 9 distinct testing arrays were managed inside custom environmental containment structures. Continuous micro-climatic tracking profiles were verified across 5 experimental treatment assignments over 3-hour durations. Gaseous introduction loops utilized isolated delivery checks, and all containment barriers were reinforced with high-density physical seal matrices to block external environmental gas changes.", body_style))

    # Parameter Data Table - Cream Muted Rows
    param_data = [
        [Paragraph("<b>Experimental Target Matrix</b>", body_style), Paragraph("<b>Operational Project Parameters & Boundary Rules</b>", body_style)],
        [Paragraph("Independent Boundary Matrix", body_style), Paragraph("Soil Variables: Baseline Sterile Soil, Standalone AMF Fungi, Pure Biochar, Integrated Co-Amended Grid", body_style)],
        [Paragraph("Dependent Telemetry Points", body_style), Paragraph("Formaldehyde Concentration (ppm), Ambient Temperature Vector, Relative Humidity, Soil pH Profiles", body_style)],
        [Paragraph("Isolation Variables", body_style), Paragraph("Airtight chambers, constant light lux values, Frost King physical barrier insulation wraps", body_style)]
    ]
    param_table = Table(param_data, colWidths=[160, 330], spaceAfter=4)
    param_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), colors.HexColor("#FAF6EE")), # Cream row header
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D1C7BD")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(param_table)
    story.append(Paragraph("Table 1.1: Scientific parameter setup, control tracking rules, and environment boundaries. Data compiled independently by Geeta Putlur.", caption_style))

    story.append(PageBreak())

    # ==========================================
    # PAGE 2: ANALYTICAL DATA, RIGOR & DISCOVERIES
    # ==========================================
    story.append(Paragraph("Empirical Analytics & Statistical Rigor Profiles", title_style))
    story.append(Paragraph("Quantifying Remediation Velocities, Statistical Inferences, and Root Boundary Limits", subtitle_style))

    story.append(Paragraph("Remediation Performance Vectors (Mean Total HCHO % Deletion Over 3 Hours)", h1_style))
    story.append(Spacer(1, 3))
    story.append(create_publication_chart())
    story.append(Spacer(1, 1))
    story.append(Paragraph("Figure 2.1: Experimental tracking output mapping mean formaldehyde clearance velocities. Standard deviation variance markers explicitly mapped. Statistical vector graphics compiled independently by Geeta Putlur via experimental spreadsheet data arrays.", caption_style))

    story.append(Paragraph("Hypothesis Validation & Mathematical Rigor Matrices", h1_style))
    story.append(Paragraph("The primary hypothesis predicted that co-amending testing matrices with both biochar and AMF fungi would unleash a synergistic optimization curve that significantly surpassed standalone allocations. Quantitative checking <b>conclusively rejected the synergy hypothesis</b>. While the integrated co-amended group matched the top clearance velocities, post-trial tracking isolated critical structural instability traits within biochar applications, making pure AMF fungi the most reliable consumer deployment option.", body_style))

    # Inference Table
    infer_data = [
        [Paragraph("<b>Applied Inference Test</b>", body_style), Paragraph("<b>Computed Value Metrics</b>", body_style), Paragraph("<b>Scientific Significance Verdict</b>", body_style)],
        [Paragraph("One-Way Analysis of Variance (ANOVA)", body_style), Paragraph("<i>F</i>(4, 15) = 10.05<br/><b>p = 0.0004</b>", body_style), Paragraph("<b>Highly Significant:</b> Rejects the null hypothesis. Confirms distinct structural variations exist across the tested soil profiles.", body_style)],
        [Paragraph("Tukey HSD: AMF vs. Sterile Soil", body_style), Paragraph("Pairwise Critical Q<br/><b>p = 0.021</b>", body_style), Paragraph("<b>Statistically Significant:</b> Confirms that biological soil adjustments drastically outperform plain non-amended options.", body_style)],
        [Paragraph("Tukey HSD: Combo Grid vs. AMF Alone", body_style), Paragraph("Pairwise Critical Q<br/><b>p = 0.576</b>", body_style), Paragraph("<b>Not Significant:</b> Establishes that adding biochar fails to provide any clear statistical clean-air advantage.", body_style)]
    ]
    infer_table = Table(infer_data, colWidths=[150, 110, 230], spaceAfter=4)
    infer_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (2,0), colors.HexColor("#FAF6EE")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D1C7BD")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(infer_table)
    story.append(Paragraph("Table 2.1: Advanced pairwise statistical analysis matrix. Probabilities calculated independently using the Stats Kingdom ANOVA model engine.", caption_style))

    # Dark Border Cream Panel for Anomaly Callout
    anomaly_box = [[
        Paragraph("<b>CRITICAL DATA DISCOVERY: THE ACIDIFICATION ANOMALY</b><br/>Post-trial micro-environmental assessments uncovered an abrupt soil chemistry crisis. Testing units containing standalone biochar experienced an intense drop in soil pH, plummeting from a balanced 6.5 down to an acidic range of 3.5 to 4.0. This severe drop restricted root cell metabolism and plant health. This biological disruption explains the massive outcome variance ($SD = \\pm 24.8\\%$) logged in biochar groups, proving that standalone AMF is the superior choice for consistent consumer safety.", ParagraphStyle('AnomTxt', parent=body_style, fontSize=8.5, leading=12, textColor=colors.HexColor("#5C1D16")))
    ]]
    anomaly_table = Table(anomaly_box, colWidths=[490], spaceAfter=3)
    anomaly_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FDF6F5")), # Muted subtle cream-red tint for attention
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#A83224")),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(Spacer(1, 4))
    story.append(anomaly_table)
    story.append(Paragraph("Table 2.2: Localized substrate soil pH tracking values logged pre- and post-trial by Geeta Putlur.", caption_style))

    story.append(PageBreak())

    # ==========================================
    # PAGE 3: CLOUD COMPUTING ENGINE & DATA DISCLOSURE
    # ==========================================
    story.append(Paragraph("Digital Scaling Solutions & System Deployment Infrastructure", title_style))
    story.append(Paragraph("Translating Botanical Laboratory Discoveries into Scalable Public Health Cloud Architectures", subtitle_style))

    story.append(Paragraph("Predictive Analytics Platform: Google Colab Framework", h1_style))
    story.append(Paragraph("To scale these micro-chamber findings for real-world application, raw telemetry points logged during the initial 60 minutes of the experimental tracking windows were pushed to a predictive data framework written in Python via Google Colab. The model evaluated clean remediation trajectories across multi-hour targets, securing a verified <b>93.1% validation accuracy score</b> (Mean Absolute Percentage Error bounded tightly at 6.9%).", body_style))

    story.append(Paragraph("Public Health Translation: Cloud Deployment via Netlify Servers", h1_style))
    story.append(Paragraph("The verified predictive algorithm was compiled into an active web calculator engine and deployed publicly on Netlify cloud architectures. This tool translates complex laboratory data into direct public utility, allowing users to enter custom room variables and calculate the exact quantity of plants required to maintain standard safety margins.", body_style))

    # Web Interface Mockup themed with Deep Green headers and Cream panels
    web_app_mock = [
        [Paragraph("<b>&Xi; CLOUD APP BUILD PRODUCTION ENVIRONMENT: PHYTOREMEDIATION VOLUME DESK</b>", ParagraphStyle('WHead', fontName='Helvetica-Bold', fontSize=8.5, textColor=colors.HexColor("#FAF6EE")))],
        [Paragraph("<b>Target Environmental Variable Field Inputs:</b><br/>&bull; Structural Spatial Footprint Capacity: <b>50 m³ (Standard Household Bedroom Area)</b><br/>&bull; Baseline Ambient Formaldehyde Metric: <b>0.15 ppm (Elevated Atmospheric Toxins Detected)</b><br/>&bull; HVAC Ventilation Air Exchange Coefficient: <b>0.2 ACH (Restricted Air Renewal Environment)</b>", ParagraphStyle('WBody', parent=body_style, fontSize=8, leading=11))],
        [Paragraph("<b>Automated Predictive Engine Output Result:</b><br/>To safely process and drive current indoor HCHO pollutants below the established World Health Organization (WHO) exposure safety ceiling of 0.08 ppm inside a strict 3-Hour remediation target window, this space layout requires: <b>28 AMF Fungi-Amended Spider Plants (Chlorophytum comosum)</b>.", ParagraphStyle('WResult', parent=body_style, fontSize=8.5, leading=12, textColor=colors.HexColor("#133B2E")))]
    ]
    web_table = Table(web_app_mock, colWidths=[490], spaceAfter=3)
    web_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#133B2E")), # Dark Forest green interface banner
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#FAF6EE")), # Smooth light cream inputs
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#EAF2EE")), # Light moss green focus panel
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#133B2E")),
        ('PADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(web_table)
    story.append(Paragraph("Figure 3.1: Active layout check of the live production calculator tool hosted on Netlify cloud systems. Software engine, data links, and layout built independently by Geeta Putlur.", caption_style))

    # Disclosures Column Grid Split
    disc_col1 = [
        Paragraph("Candidate Transparency Checklist", h1_style),
        Paragraph("&bull; <b>Data Filtering Protocol:</b> 4 out of 8 initial tracking cycles were actively removed from final calculation datasets due to automated sensor glitches or enclosure seals dropping pressure. This preserves absolute data integrity.", bullet_style),
        Paragraph("&bull; <b>Assistance & AI Systems Disclosure:</b> In strict compliance with 2026 fair rules, Claude AI (Anthropic) was used as an engineering sounding board to cross-verify statistical scripts and optimize the public web app layout.", bullet_style)
    ]

    disc_col2 = [
        Paragraph("Academic Literature Records", h1_style),
        Paragraph("1. <b>Wolverton, B. C. (1982).</b> Foliage plants for removing formaldehyde from contaminated air. <i>NASA Technical Report</i> (NASA-TP-2286).", ParagraphStyle('B1', fontName='Helvetica', fontSize=7, leading=9, spaceAfter=2)),
        Paragraph("2. <b>U.S. Environmental Protection Agency (2025).</b> Formaldehyde's impact on long-term indoor air quality index frameworks. <i>EPA IAQ Review Docs</i>.", ParagraphStyle('B2', fontName='Helvetica', fontSize=7, leading=9, spaceAfter=2)),
        Paragraph("3. <b>Wahab, A. (2023).</b> Role of arbuscular mycorrhizal fungi in regulating structural root growth matrices. <i>Plants</i>, 12(17), 3102.", ParagraphStyle('B3', fontName='Helvetica', fontSize=7, leading=9, spaceAfter=2)),
        Paragraph("4. <b>Lehmann, J. (2011).</b> Biochar effects on soil biota and structural chemistry. <i>Soil Biology & Biochemistry</i>, 43(9), 1812-1836.", ParagraphStyle('B4', fontName='Helvetica', fontSize=7, leading=9, spaceAfter=2))
    ]

    p3_grid = Table([[disc_col1, disc_col2]], colWidths=[255, 235])
    p3_grid.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('RIGHTPADDING', (0,0), (0,0), 8),
        ('LEFTPADDING', (1,0), (1,0), 8),
    ]))
    story.append(p3_grid)

    doc.build(story, canvasmaker=EliteNumberedCanvas)

if __name__ == "__main__":
    build_pdf()
    print("Success: 'ThermoFisher_Cream_Green_Visual_Aid.pdf' generated with advanced institutional styling.")

import datetime
import unicodedata
from fpdf import FPDF

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def export_to_pdf(report_text: str) -> str:

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, "AI Agent - GA4 Analyticky Report", ln=True, align='C')
    
    pdf.set_font("Helvetica", size=10)
    date_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    pdf.cell(0, 10, f"Vygenerovane dna: {date_str}", ln=True, align='C')
    pdf.ln(10)
    
    clean_text = report_text.replace('**', '').replace('###', '')

    replacements = {
        '–': '-', '—': '-', '←': '<-', '→': '->', 
        '•': '*', '✅': 'OK:', '🚀': ''
    }
    for old, new in replacements.items():
        clean_text = clean_text.replace(old, new)

    clean_text = strip_accents(clean_text)
    clean_text = clean_text.encode('ascii', 'ignore').decode('ascii')
    
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 8, txt=clean_text)
    
    filename = f"GA4_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)
    
    return f"Report bol uspesne vygenerovany ako: {filename}"
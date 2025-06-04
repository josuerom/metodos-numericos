from fpdf import FPDF
from database.db import connect

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Historial de Métodos Numéricos', ln=True, align='C')
        self.ln(10)

    def chapter_body(self, row):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 8, f"Método: {row[1]}\nEntrada: {row[2]}\nResultado: {row[3]}\nExplicación: {row[4]}\nFecha: {row[5]}")
        self.ln(5)

    def print_history(self, data):
        for row in data:
            self.chapter_body(row)

def export_history_to_pdf():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historial")
    data = cursor.fetchall()
    conn.close()

    pdf = PDF()
    pdf.add_page()
    pdf.print_history(data)
    pdf.output("docs/resultados_métodos.pdf")
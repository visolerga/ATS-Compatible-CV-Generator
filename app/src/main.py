from app.services.user_service import UserService
from app.services.cv_service import CVService
from fpdf import FPDF
# import os
# import sys

# # Añadir el directorio raíz al PYTHONPATH
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def generate_cv(data, output_path="cv.pdf"):
    """Genera un CV en formato PDF basado en los datos proporcionados."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Personal Info
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Personal Information", ln=True)
    pdf.set_font("Arial", size=12)
    for key, value in data["personal_info"].items():
        pdf.cell(0, 10, f"{key.capitalize()}: {value}", ln=True)

    # Professional Summary
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Professional Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data["professional_summary"])

    # Work Experience
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Work Experience", ln=True)
    pdf.set_font("Arial", size=12)
    for experience in data["work_experience"]:
        pdf.cell(0, 10, f"{experience['job_title']} at {experience['company']}", ln=True)
        pdf.cell(0, 10, f"Duration: {experience['duration']}", ln=True)
        pdf.multi_cell(0, 10, "Responsibilities: " + ", ".join(experience["responsibilities"]))

    # Skills
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ", ".join(data["skills"]))

    # Save the PDF
    pdf.output(output_path)
    print(f"CV generated successfully: {output_path}")


if __name__ == "__main__":
    from app.database.database import init_db

    # Inicializar base de datos
    init_db()

    # Obtener el usuario y su CV
    user_service = UserService()
    cv_service = CVService()

    # ID del usuario para la prueba
    user_id = 1  # Cambiar según los datos en la base de datos
    user = user_service.get_user_by_id(user_id)
    if not user:
        print(f"No user found with ID {user_id}")
        exit(1)

    # Obtener el CV del usuario
    cv = cv_service.get_cv_by_user_id(user_id)
    if not cv:
        print(f"No CV found for user ID {user_id}")
        exit(1)

    # Generar el PDF usando los datos del CV
    generate_cv(cv)

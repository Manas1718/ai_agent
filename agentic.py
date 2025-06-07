# Rebuilt: AI-Powered Student Performance Feedback System (From Scratch)

import json
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
from datetime import datetime


def load_student_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)[0]


def extract_overview(data):
    subject_map = ['Physics', 'Chemistry', 'Maths']
    overview = {
        'total_score': data['totalMarkScored'],
        'accuracy': round(data['accuracy'], 2),
        'total_time': data['totalTimeTaken'],
        'subjects': []
    }
    for idx, subj in enumerate(data['subjects']):
        overview['subjects'].append({
            'name': subject_map[idx],
            'score': subj['totalMarkScored'],
            'accuracy': round(subj['accuracy'], 2),
            'time_taken': subj['totalTimeTaken'],
            'attempted': subj['totalAttempted'],
            'correct': subj['totalCorrect']
        })
    return overview


def generate_feedback(overview):
    strengths = []
    focus_areas = []
    suggestions = []

    for s in overview['subjects']:
        if s['accuracy'] >= 70:
            strengths.append(s['name'])
        elif s['accuracy'] < 40:
            focus_areas.append(s['name'])
            suggestions.append(f"Revise basics in {s['name']} and practice 10 questions daily.")

    feedback = f"Hi there!\n\nYou have done a solid job in this assessment. Total score: {overview['total_score']} marks with {overview['accuracy']}% accuracy.\n\n"
    if strengths:
        feedback += f"Great performance in: {', '.join(strengths)}\n"
    if focus_areas:
        feedback += f"Needs improvement in: {', '.join(focus_areas)}\n"
    feedback += "\nSuggestions:\n"
    feedback += "\n".join(suggestions or ["Keep up consistent practice and time-bound mock tests."])
    return feedback

def plot_performance_chart(subjects):
    plt.figure(figsize=(6, 4))
    sns.barplot(x=[s['name'] for s in subjects], y=[s['accuracy'] for s in subjects], color='skyblue')
    plt.title('Subject-wise Accuracy')
    plt.xlabel('Subjects')
    plt.ylabel('Accuracy (%)')
    plt.ylim(0, 100)
    plt.tight_layout()
    chart_file = 'accuracy_chart.png'
    plt.savefig(chart_file)
    plt.close()
    return chart_file

#pdf
def create_pdf(overview, feedback, chart_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Student Performance Report', ln=True, align='C')
    pdf.ln(10)

    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Total Score: {overview['total_score']}", ln=True)
    pdf.cell(0, 10, f"Accuracy: {overview['accuracy']}%", ln=True)
    pdf.cell(0, 10, f"Total Time: {overview['total_time']} seconds", ln=True)
    pdf.ln(5)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Subject-wise Details:', ln=True)
    pdf.set_font('Arial', '', 11)
    for s in overview['subjects']:
        line = f"{s['name']}: Score {s['score']}, Accuracy {s['accuracy']}%, Time {s['time_taken']}s, Attempted {s['attempted']}, Correct {s['correct']}"
        pdf.cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    pdf.ln(8)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Feedback & Suggestions:', ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 10, feedback.encode('latin-1', 'replace').decode('latin-1'))

    pdf.ln(5)
    pdf.image(chart_file, x=10, w=180)

    report_file = f"student_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(report_file)
    return report_file



def generate_student_report(json_path):
    data = load_student_data(json_path)
    overview = extract_overview(data)
    feedback = generate_feedback(overview)
    chart_path = plot_performance_chart(overview['subjects'])
    pdf_file = create_pdf(overview, feedback, chart_path)
    print(f"✅ Report generated: {pdf_file}")

if __name__ == '__main__':
    generate_student_report('sample_submission_analysis_1.json')

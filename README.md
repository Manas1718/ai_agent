# AI Agent - Student Performance Feedback System

This repository contains an AI-powered Student Performance Feedback System that analyzes student test data, generates personalized insights, and produces PDF reports.

---

## API(s) Used

- **OpenAI API**: Used for natural language processing tasks such as generating personalized feedback, insights, and summary comments based on student test data.
- **FPDF Library**: For creating and exporting PDF reports containing the generated feedback and visualizations.
- (Optional) Other Python libraries for data manipulation and visualization, such as `matplotlib` for charts.

---

## Prompt Logic

The system constructs prompts dynamically to feed into the OpenAI API, based on the student test results. The prompts include:

- An overview of the student’s performance.
- Identification of strengths and weaknesses.
- Personalized advice and suggestions for improvement.
- Contextual interpretation of the test data, such as question-wise analysis.

This prompt engineering ensures meaningful and relevant AI-generated feedback tailored to each student’s data.

---

## Report Structure

The final output report is generated as a PDF and includes:

1. **Overview Section**  
   A summary of overall student performance.

2. **Detailed Feedback Section**  
   Personalized comments highlighting strengths and areas for improvement.

3. **Visualizations**  
   - Bar charts representing scores across topics or sections.
   - Scatter charts or other graphs to depict performance trends or comparisons.

4. **Additional Insights**  
   Any further analysis or recommendations extracted from the AI model’s output.

---

## How to Use

1. Prepare student test data in JSON format.
2. Run the `generate_student_report()` function providing the JSON file path.
3. The system generates a PDF report with detailed AI-driven feedback and visualizations.

---


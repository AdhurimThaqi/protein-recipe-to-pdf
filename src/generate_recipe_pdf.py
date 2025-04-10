from fpdf import FPDF

# Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Protein Recipes', align='C', ln=True, bold=True)
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
    
    def chapter_body(self, title, ingredients, instructions, nutrition):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, f'Title: {title}')
        self.multi_cell(0, 10, 'Ingredients:')
        for item in ingredients:
            self.multi_cell(0, 10, f"- {item}")
        self.multi_cell(0, 10, 'Instructions:')
        for step in instructions:
            self.multi_cell(0, 10, step)
        self.multi_cell(0, 10, 'Nutritional Info:')
        for fact in nutrition:
            self.multi_cell(0, 10, fact)
        self.ln(10)

# Create PDF instance
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add a chapter (your recipe)
pdf.chapter_title("Protein Pancakes")
pdf.chapter_body(
    title="Protein Pancakes",
    ingredients=[
        "1/2 cup oats",
        "2 eggs",
        "1/2 tsp baking powder",
        "1 tsp vanilla sugar",
        "1 scoop vanilla whey protein powder",
        "1 ripe banana"
    ],
    instructions=[
        "1. Add oats, eggs, baking powder, vanilla sugar, whey protein powder, and banana into a blender. Blend until smooth.",
        "2. Heat a non-stick pancake pan over medium heat.",
        "3. Pour small amounts of the batter into the pan and cook 2-3 minutes per side.",
        "4. Serve warm. Optionally top with fruit or yogurt."
    ],
    nutrition=[
        "Protein: ~20-25g",
        "Carbohydrates: Moderate",
        "Fats: Healthy fats from eggs",
        "Refined Sugar: None"
    ]
)

# Save the PDF to a file
pdf.output('protein_recipes.pdf')

from fpdf import FPDF

# Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Protein Recipes', align='C', ln=True)
    
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

# PDF instance
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Chapter 1: Protein Pancakes
pdf.chapter_title("1. Protein Pancakes")
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

# Add another chapter (Pasta recipe)
pdf.chapter_title("Protein Pasta")
pdf.chapter_body(
    title="High-Protein Yogurt Pasta",
    ingredients=[
        "1 serving whole-grain or high-protein pasta",
        "1/2 cup cottage cheese or Greek yogurt",
        "Salt, pepper, and herbs to taste"
    ],
    instructions=[
        "1. Boil pasta according to package instructions.",
        "2. Drain and mix with Greek yogurt or cottage cheese.",
        "3. Season to taste and serve warm."
    ],
    nutrition=[
        "Protein: ~30g depending on pasta and yogurt",
        "Low Cost",
        "Creamy and satisfying"
    ]
)
# List of recipes
recipes = [
    {
        "title": "Protein Pancakes",
        "ingredients": [
            "1/2 cup oats",
            "2 eggs",
            "1/2 tsp baking powder",
            "1 tsp vanilla sugar",
            "1 scoop vanilla whey protein powder",
            "1 ripe banana"
        ],
        "instructions": [
            "Add oats, eggs, baking powder, vanilla sugar, whey protein powder, and banana into a blender.",
            "Blend until smooth.",
            "Heat a non-stick pan over medium heat.",
            "Pour small amounts of the batter into the pan and cook 2-3 minutes per side.",
            "Serve warm with toppings like fruit or yogurt."
        ],
        "nutrition": [
            "Protein: ~25g",
            "Low Sugar",
            "Moderate Carbs",
            "Good Fats from eggs"
        ]
    },
    {
        "title": "High-Protein Yogurt Pasta",
        "ingredients": [
            "1 serving whole-grain or high-protein pasta",
            "1/2 cup cottage cheese or Greek yogurt",
            "Salt, pepper, and herbs to taste"
        ],
        "instructions": [
            "Boil pasta according to package instructions.",
            "Drain and mix with Greek yogurt or cottage cheese.",
            "Season to taste and serve warm."
        ],
        "nutrition": [
            "Protein: ~30g depending on pasta and yogurt",
            "Low Cost",
            "Creamy and satisfying"
        ]
    },
    {
        "title": "Tuna Egg Bowl",
        "ingredients": [
            "1 can tuna",
            "2 boiled eggs",
            "Mixed salad greens",
            "1 tbsp olive oil",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Boil eggs and slice them.",
            "Mix tuna and greens in a bowl.",
            "Add sliced eggs and drizzle olive oil.",
            "Season and serve."
        ],
        "nutrition": [
            "Protein: ~35g",
            "Low Carb",
            "Rich in Omega-3s"
        ]
    },
    {
        "title": "Cottage Cheese Toast",
        "ingredients": [
            "2 slices whole grain bread",
            "1/2 cup cottage cheese",
            "Cherry tomatoes",
            "Salt and pepper"
        ],
        "instructions": [
            "Toast the bread slices.",
            "Spread cottage cheese over each toast.",
            "Top with sliced cherry tomatoes.",
            "Season with salt and pepper."
        ],
        "nutrition": [
            "Protein: ~20g",
            "High Fiber",
            "Low Cost"
        ]
    },
    {
        "title": "Greek Yogurt Parfait",
        "ingredients": [
            "1 cup Greek yogurt",
            "1/2 cup berries",
            "1 tbsp chia seeds",
            "1 tbsp honey (optional)"
        ],
        "instructions": [
            "Layer Greek yogurt and berries in a cup.",
            "Top with chia seeds and honey if desired."
        ],
        "nutrition": [
            "Protein: ~20g",
            "Low Sugar (if no honey)",
            "Great for breakfast"
        ]
    },
    {
        "title": "Egg & Spinach Wrap",
        "ingredients": [
            "2 eggs",
            "1 handful spinach",
            "1 whole wheat wrap",
            "1 tbsp olive oil"
        ],
        "instructions": [
            "Scramble eggs with spinach in olive oil.",
            "Wrap in tortilla and serve."
        ],
        "nutrition": [
            "Protein: ~22g",
            "Iron from spinach",
            "Budget-friendly"
        ]
    },
    {
        "title": "Protein Oats",
        "ingredients": [
            "1/2 cup oats",
            "1 scoop whey protein",
            "1 cup water or milk",
            "1/2 banana"
        ],
        "instructions": [
            "Cook oats with water or milk.",
            "Stir in whey protein and mashed banana."
        ],
        "nutrition": [
            "Protein: ~30g",
            "Easy and fast",
            "Filling and warm"
        ]
    },
    {
        "title": "Chickpea Salad",
        "ingredients": [
            "1 can chickpeas",
            "Chopped cucumber, tomatoes, onion",
            "1 tbsp olive oil",
            "Lemon juice"
        ],
        "instructions": [
            "Mix all ingredients in a bowl.",
            "Toss and serve chilled."
        ],
        "nutrition": [
            "Protein: ~18g",
            "High Fiber",
            "Plant-based option"
        ]
    },
    {
        "title": "Egg Muffins",
        "ingredients": [
            "4 eggs",
            "Chopped bell peppers and onions",
            "Salt, pepper"
        ],
        "instructions": [
            "Preheat oven to 180°C (350°F).",
            "Mix eggs and veggies, pour into muffin tins.",
            "Bake for 15-20 mins."
        ],
        "nutrition": [
            "Protein: ~30g per 4 muffins",
            "Meal prep friendly",
            "Portable snack"
        ]
    },
    {
        "title": "Lentil Stew",
        "ingredients": [
            "1 cup lentils",
            "Carrots, onions, tomatoes",
            "Garlic, cumin, paprika"
        ],
        "instructions": [
            "Sauté veggies and garlic.",
            "Add lentils and spices with water.",
            "Simmer until soft (20-30 mins)."
        ],
        "nutrition": [
            "Protein: ~25g per bowl",
            "High fiber and filling",
            "Vegan & low cost"
        ]
    },
    {
        "title": "Protein Smoothie",
        "ingredients": [
            "1 scoop whey protein",
            "1/2 banana",
            "1 cup milk or water",
            "Ice cubes"
        ],
        "instructions": [
            "Blend all ingredients until smooth.",
            "Serve chilled."
        ],
        "nutrition": [
            "Protein: ~25g",
            "Great post-workout",
            "Takes 2 mins"
        ]
    },
    {
        "title": "Turkey Lettuce Wraps",
        "ingredients": [
            "100g ground turkey",
            "Lettuce leaves",
            "Soy sauce, ginger, garlic"
        ],
        "instructions": [
            "Cook turkey with garlic, ginger, soy sauce.",
            "Scoop into lettuce leaves and eat like tacos."
        ],
        "nutrition": [
            "Protein: ~30g",
            "Low carb",
            "Great for lunch"
        ]
    }
]

# This is the Oat Bread recipe - low calorie
pdf.chapter_title("High Protein Bread")
pdf.chapter_body(
    title="High-Protein Bread",
    ingredients=[
        "150gr of grinded oats - (oat flour)",
        "1/2 cup cottage cheese or Greek yogurt",
        "2 eggs",
        "Salt, pepper, and herbs to taste"
    ],
    instructions=[
        "1. put the 150gr of oat flour into a bowl",
        "2. Add the cottage cheese or Greek Yogurt / around 200gr.",
        "3. Season to taste and put it on the oven for 25-30 min at 200 degree Celcius"
    ],
    nutrition=[
        "Protein: ~40g depending on cottage cheese",
        "Low Cost",
        "Low calorie and high carb - ideal for pre workout meal"
    ]
)

# Save the PDF to a file
pdf.output('protein_recipes.pdf')

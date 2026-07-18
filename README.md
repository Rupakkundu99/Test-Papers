# AeroAssess — Elite Assessment Hub

AeroAssess is a dynamic, reusable, and hostable assessment platform designed to serve multiple question papers with section timings, interactive answer submissions, immediate grading, and explanation reviews.

## Project Structure

The project separates layout and logic from the actual quiz content. This makes the platform scalable and easy to extend:

```
├── index.html            # Dashboard / Portal (lists all papers)
├── test.html             # Assessment Engine (runs the timing & tests)
├── papers/
│   ├── catalog.json      # Registry / Index of all available tests
│   ├── aptitude_test_1.json   # Question paper 1 data
│   └── aptitude_test_2.json   # Question paper 2 data (mock test)
└── README.md             # This guide
```

---

## How to Run Locally

Because the dashboard and assessment engine dynamically load your papers using web requests (`fetch`), browsers prevent direct loading from your local hard drive (double-clicking the `.html` file) due to CORS security policies.

To run and test the website on your computer, you must run a simple local web server:

### Option A: VS Code Live Server (Recommended)
1. Open this folder in VS Code.
2. Install the **Live Server** extension (by Ritwick Dey).
3. Click **Go Live** in the bottom-right corner of VS Code.

### Option B: Python (Simple & fast)
1. Open your terminal in this directory.
2. Run:
   ```bash
   python -m http.server 8000
   ```
3. Open your browser and navigate to `http://localhost:8000`.

### Option C: NodeJS
1. Open your terminal in this directory.
2. Run:
   ```bash
   npx serve
   ```
3. Open `http://localhost:3000`.

*Note: Once you deploy the website to a hosting platform, it will work instantly for anyone, with no extra setup required!*

---

## How to Add New Question Papers

Adding a new paper takes only two simple steps and requires **no code changes**.

### Step 1: Create the Paper JSON
Create a new JSON file inside the `papers/` folder (e.g., `papers/aptitude_test_3.json`). Use this structure:

```json
[
  {
    "name": "Section Name (e.g. Quantitative)",
    "duration": 25,
    "questions": [
      {
        "q": "Question text here.\nSupports multiline text.",
        "options": [
          "Option A text",
          "Option B text",
          "Option C text",
          "Option D text"
        ],
        "correct": 0,
        "explanation": "Detailed explanation of why Option A is correct."
      }
    ]
  }
]
```
*Note: The `correct` field is 0-indexed (0 = A, 1 = B, 2 = C, 3 = D).*

### Step 2: Register it in the Catalog
Open `papers/catalog.json` and add an entry for your new paper:

```diff
[
  {
    "id": "aptitude_test_1",
    "title": "Aptitude Assessment - Set 1",
    "description": "Comprehensive timed test covering Numerical, Reasoning, Quantitative, and Verbal skills.",
    "duration": 101,
    "questionsCount": 79
  },
  {
    "id": "aptitude_test_2",
    "title": "Aptitude Assessment - Set 2",
    "description": "A second shorter practice test containing sample math and reasoning questions to test dynamic loading.",
    "duration": 10,
    "questionsCount": 4
  },
+ {
+   "id": "aptitude_test_3",
+   "title": "Aptitude Assessment - Set 3",
+   "description": "Describe your new test here to show on the dashboard.",
+   "duration": 25,
+   "questionsCount": 1
+ }
]
```
The dashboard (`index.html`) will automatically detect it and render a start card!

---

## How to Host Your Website For Free

You can publish this website so anyone can solve these tests online for free.

### Option 1: GitHub Pages (Easiest & Automatic Updates)
1. Go to [GitHub](https://github.com) and create a new repository (e.g., `my-assessments`).
2. Upload these files to the repository.
3. In your GitHub repository, click on **Settings** (top tab).
4. Scroll down to **Pages** in the left sidebar.
5. Under **Build and deployment** -> **Branch**, select `main` (or `master`) and `/ (root)`, then click **Save**.
6. GitHub will give you a public link (e.g., `https://yourusername.github.io/my-assessments/`). Anyone can visit it to solve the papers!

### Option 2: Netlify (Drag & Drop, Under 30 seconds)
1. Go to [Netlify](https://www.netlify.com) and create a free account.
2. Log in and go to the **Sites** tab.
3. Scroll to the bottom where it says **"Want to deploy a new site without connecting to Git?"**.
4. Drag and drop this folder directly into the designated upload area.
5. Netlify will instantly host your site and give you a public URL!

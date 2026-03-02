import streamlit as st
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from groq import Groq

st.set_page_config(page_title="Ultimate AI Calculator", page_icon="🧠", layout="centered")

st.title("🧠 Ultimate AI Mathematics & Physics Calculator")

# ================= SIDEBAR =================
mode = st.sidebar.selectbox(
    "Select Mode",
    [
        "Basic",
        "Scientific",
        "Advanced Algebra",
        "Polynomial Solver",
        "Matrix & Determinant",
        "Complex Numbers",
        "Integration / Differentiation",
        "Graph Plotter",
        "Geometry 2D/3D",
        "Unit Converter",
        "Merit & GPA",
        "Physics Library",
        "AI Smart Solver"
    ]
)

# ================= BASIC =================
def basic():
    st.header("Basic Calculator")
    a = st.number_input("Number 1")
    b = st.number_input("Number 2")
    op = st.selectbox("Operation", ["+", "-", "*", "/", "%", "Power"])

    if st.button("Calculate"):
        try:
            if op == "+": st.success(a+b)
            elif op == "-": st.success(a-b)
            elif op == "*": st.success(a*b)
            elif op == "/": st.success(a/b)
            elif op == "%": st.success(a%b)
            elif op == "Power": st.success(a**b)
        except:
            st.error("Invalid Input")

# ================= SCIENTIFIC =================
def scientific():
    st.header("Scientific Calculator")
    expression = st.text_input("Enter Expression (sin(30)+sqrt(16))")

    safe_dict = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "pi": math.pi,
        "e": math.e,
        "abs": abs
    }

    if st.button("Evaluate"):
        try:
            result = eval(expression, {"__builtins__": None}, safe_dict)
            st.success(result)
        except Exception as e:
            st.error(f"Invalid Expression: {e}")

# ================= ADVANCED ALGEBRA =================
def advanced():
    st.header("Equation Solver")
    eq = st.text_input("Enter Equation (x**2 - 5*x + 6)")
    if st.button("Solve"):
        try:
            x = sp.symbols('x')
            solution = sp.solve(sp.sympify(eq), x)
            st.success(solution)
        except:
            st.error("Invalid Equation")

# ================= POLYNOMIAL =================
def polynomial():
    st.header("Polynomial Solver")
    eq = st.text_input("Enter Polynomial")
    if st.button("Solve Polynomial"):
        x = sp.symbols('x')
        sol = sp.solve(sp.sympify(eq), x)
        st.success(sol)

# ================= MATRIX =================
def matrix_calc():
    st.header("Matrix Calculator (2x2)")
    a = st.number_input("a")
    b = st.number_input("b")
    c = st.number_input("c")
    d = st.number_input("d")

    matrix = sp.Matrix([[a,b],[c,d]])

    if st.button("Determinant"):
        st.success(matrix.det())

# ================= COMPLEX =================
def complex_calc():
    st.header("Complex Numbers")
    c1 = complex(st.text_input("Enter First Complex (e.g 3+4j)"))
    c2 = complex(st.text_input("Enter Second Complex (e.g 1+2j)"))

    if st.button("Add"):
        st.success(c1 + c2)

# ================= CALCULUS =================
def calculus():
    st.header("Integration / Differentiation")
    expr = st.text_input("Enter Expression (x**2 + 3*x)")
    x = sp.symbols('x')

    if st.button("Differentiate"):
        st.success(sp.diff(sp.sympify(expr), x))

    if st.button("Integrate"):
        st.success(sp.integrate(sp.sympify(expr), x))

# ================= GRAPH =================
def graph_plot():
    st.header("Graph Plotter")
    expr = st.text_input("Enter function (x**2)")
    x = sp.symbols('x')

    if st.button("Plot Graph"):
        f = sp.lambdify(x, sp.sympify(expr), "numpy")
        x_vals = np.linspace(-10,10,400)
        y_vals = f(x_vals)
        plt.plot(x_vals,y_vals)
        st.pyplot(plt)

# ================= GEOMETRY =================
def geometry():
    st.header("Geometry")
    shape = st.selectbox("Shape", ["Circle","Sphere"])

    if shape=="Circle":
        r = st.number_input("Radius")
        if st.button("Area"):
            st.success(math.pi*r*r)

    if shape=="Sphere":
        r = st.number_input("Radius")
        if st.button("Surface Area"):
            st.success(4*math.pi*r*r)

# ================= UNIT =================
def unit():
    st.header("Unit Converter")
    value = st.number_input("Enter Value")
    option = st.selectbox("Convert", ["Meter to KM","KG to Gram"])

    if st.button("Convert"):
        if option=="Meter to KM":
            st.success(value/1000)
        else:
            st.success(value*1000)

# ================= MERIT =================
def merit():
    st.header("Merit & GPA")
    obtained = st.number_input("Obtained Marks")
    total = st.number_input("Total Marks")

    if st.button("Calculate %"):
        st.success((obtained/total)*100)

# ================= PHYSICS =================
def physics():
    st.header("Physics Library")
    formula = st.selectbox("Formula",[
        "Force (F=m*a)",
        "Velocity (v=d/t)",
        "KE (1/2mv^2)"
    ])

    if formula=="Force (F=m*a)":
        m=st.number_input("Mass")
        a=st.number_input("Acceleration")
        if st.button("Calculate"):
            st.success(m*a)

# ================= AI =================
def ai_solver():
    st.header("🤖 AI Smart Solver")

    question = st.text_area("Ask any Math / Physics Question")

    if st.button("Solve with AI"):
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])

            prompt = f"""
            Solve step by step from basic to advanced level.
            Explain formulas used.
            Question:
            {question}
            """

            response = client.chat.completions.create(
                messages=[{"role":"user","content":prompt}],
                model="llama-3.3-70b-versatile",
            )

            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")

# ================= MODE CONTROL =================
if mode=="Basic": basic()
elif mode=="Scientific": scientific()
elif mode=="Advanced Algebra": advanced()
elif mode=="Polynomial Solver": polynomial()
elif mode=="Matrix & Determinant": matrix_calc()
elif mode=="Complex Numbers": complex_calc()
elif mode=="Integration / Differentiation": calculus()
elif mode=="Graph Plotter": graph_plot()
elif mode=="Geometry 2D/3D": geometry()
elif mode=="Unit Converter": unit()
elif mode=="Merit & GPA": merit()
elif mode=="Physics Library": physics()
elif mode=="AI Smart Solver": ai_solver()

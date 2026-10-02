"""Streamlit web interface for the calculator."""
import streamlit as st
from calculator import calculate, OPERATIONS

st.set_page_config(page_title="Python Calculator", page_icon="+", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #202a29;
        --muted: #75807d;
        --paper: #f5f6f2;
        --line: #e3e7e1;
        --green: #16745a;
        --primary-color: #16745a;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    html, body, [class*="css"] { font-family: 'Manrope', sans-serif; }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 1120px; padding-top: 3rem; padding-bottom: 4rem; }
    .eyebrow { color: var(--green); font-size: 12px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; }
    .page-title { color: var(--ink); font-size: 38px; font-weight: 800; letter-spacing: 0; margin: 5px 0 4px; }
    .page-subtitle { color: var(--muted); font-size: 14px; margin-bottom: 28px; }
    .st-key-calculator_panel, .st-key-history_panel { background: #fff; border-radius: 8px; }
    .display { background: #202a29; border-radius: 7px; color: #fff; padding: 22px 24px; margin: 2px 0 25px; }
    .display-label { color: #aab8b1; font-size: 11px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; }
    .display-value { font-family: 'DM Mono', monospace; font-size: 34px; font-weight: 500; line-height: 1.3; overflow-wrap: anywhere; padding-top: 8px; }
    .display-expression { color: #b8c5bf; font-family: 'DM Mono', monospace; font-size: 13px; padding-top: 8px; }
    .section-label { color: var(--ink); font-size: 15px; font-weight: 800; margin-bottom: 14px; }
    .stNumberInput label, .stRadio label { color: var(--muted) !important; font-size: 12px !important; font-weight: 700 !important; }
    .stNumberInput input { font-family: 'DM Mono', monospace; }
    div[role="radiogroup"] { gap: 8px; }
    div[role="radiogroup"] label { background: #f2f5f1; border: 1px solid var(--line); border-radius: 6px; color: var(--ink) !important; padding: 8px 13px; }
    div[role="radiogroup"] label * { color: var(--ink) !important; }
    div[role="radiogroup"] label:has(input:checked) { background: var(--green); border-color: var(--green); color: #fff !important; }
    div[role="radiogroup"] label:has(input:checked) * { color: #fff !important; }
    .stButton > button { border-radius: 6px; min-height: 44px; font-weight: 800; }
    .stButton > button[kind="primary"] { background: var(--green); border-color: var(--green); }
    .stButton > button[kind="secondary"] { color: var(--ink); border-color: var(--line); background: #fff; }
    .history-title { color: var(--ink); font-size: 17px; font-weight: 800; margin-bottom: 4px; }
    .history-caption { color: var(--muted); font-size: 12px; margin-bottom: 18px; }
    .history-item { border-top: 1px solid var(--line); padding: 14px 0; }
    .history-expression { color: var(--muted); font-family: 'DM Mono', monospace; font-size: 12px; }
    .history-result { color: var(--ink); font-family: 'DM Mono', monospace; font-size: 17px; font-weight: 500; margin-top: 5px; }
    .history-time { color: var(--muted); font-size: 11px; margin-top: 4px; }
    @media (max-width: 700px) {
        .block-container { padding: 1.5rem 1rem 3rem; }
        .page-title { font-size: 30px; }
        .panel { padding: 18px; }
        .display-value { font-size: 27px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "history" not in st.session_state:
    st.session_state.history = []
if "answer" not in st.session_state:
    st.session_state.answer = None

st.markdown('<div class="eyebrow">PDC · QUICK CALCULATIONS</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">Python Calculator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="page-subtitle">A precise place to work through the numbers.</div>',
    unsafe_allow_html=True,
)

calculator_column, history_column = st.columns([1.65, 1], gap="large")

with calculator_column:
    with st.container(border=True, key="calculator_panel"):
        if st.session_state.answer is None:
            display_value = "Ready"
            display_expression = "Enter an expression to begin"
        else:
            display_value = st.session_state.answer["result"]
            display_expression = st.session_state.answer["expression"]

        st.markdown(
            f'<div class="display"><div class="display-label">Result</div>'
            f'<div class="display-value">{display_value}</div>'
            f'<div class="display-expression">{display_expression}</div></div>',
            unsafe_allow_html=True,
        )
        st.markdown('<div class="section-label">New calculation</div>', unsafe_allow_html=True)

        first_number, second_number = st.columns(2, gap="medium")
        with first_number:
            a = st.number_input("First number", value=0.0, format="%g", key="first_number")
        with second_number:
            b = st.number_input("Second number", value=0.0, format="%g", key="second_number")

        op = st.radio("Operation", list(OPERATIONS.keys()), horizontal=True, label_visibility="collapsed")
        calculate_column, clear_column = st.columns([2, 1], gap="small")
        with calculate_column:
            calculate_clicked = st.button("Calculate", type="primary", use_container_width=True)
        with clear_column:
            clear_clicked = st.button("Clear", use_container_width=True)

        if calculate_clicked:
            try:
                result, elapsed = calculate(a, op, b)
                expression = f"{a:g} {op} {b:g}"
                result_text = f"{result:g}" if isinstance(result, (int, float)) else str(result)
                entry = {
                    "expression": expression,
                    "result": result_text,
                    "elapsed": elapsed,
                }
                st.session_state.answer = entry
                st.session_state.history.insert(0, entry)
                st.session_state.history = st.session_state.history[:8]
                st.rerun()
            except ZeroDivisionError as error:
                st.error(str(error))

        if clear_clicked:
            st.session_state.answer = None
            st.rerun()

with history_column:
    with st.container(border=True, key="history_panel"):
        st.markdown('<div class="history-title">Recent calculations</div>', unsafe_allow_html=True)
        st.markdown('<div class="history-caption">Your latest results in this session</div>', unsafe_allow_html=True)
        if not st.session_state.history:
            st.caption("Your calculations will appear here.")
        else:
            for item in st.session_state.history:
                st.markdown(
                    f'<div class="history-item"><div class="history-expression">{item["expression"]}</div>'
                    f'<div class="history-result">= {item["result"]}</div>'
                    f'<div class="history-time">{item["elapsed"] * 1e6:.2f} μs</div></div>',
                    unsafe_allow_html=True,
                )

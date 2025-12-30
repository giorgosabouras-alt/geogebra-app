import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("Δυναμικό Γεωμετρικό Μοντέλο (AB)")

AB = st.slider("Μεταβλητή AB", 0.5, 10.0, 3.0, 0.1)

A = np.array([0.0, 0.0])
B = np.array([AB, 0.0])

t = np.linspace(0, 2*np.pi, 400)

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(AB*np.cos(t), AB*np.sin(t), label="Κύκλος ακτίνας AB")
ax.plot([A[0], B[0]], [A[1], B[1]], "ro-", label="Τμήμα AB")

ax.text(*A, "A")
ax.text(*B, "B")

ax.axis("equal")
ax.grid(True)
ax.legend()

st.pyplot(fig)||
Προσθήκη app.py

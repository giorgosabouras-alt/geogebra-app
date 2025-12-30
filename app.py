import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------- ΡΥΘΜΙΣΕΙΣ ----------
st.set_page_config(layout="centered")
st.title("Γεωμετρική Κατασκευή – Μεταβλητή AB")

# ---------- SLIDER ----------
a = st.slider("Μήκος AB", 0.5, 10.0, 3.0, 0.05)

# ---------- ΒΑΣΙΚΑ ----------
O = np.array([0.0, 0.0])
A = np.array([-a/2, 0.0])
B = np.array([ a/2, 0.0])

# Κύκλοι
R_out = a
R_in  = a / np.pi

t = np.linspace(0, 2*np.pi, 600)

# ---------- ΣΧΕΔΙΑΣΗ ----------
fig, ax = plt.subplots(figsize=(6, 6))

# Άξονες
ax.axhline(0, lw=1)
ax.axvline(0, lw=1)

# Τμήμα AB
ax.plot([A[0], B[0]], [A[1], B[1]], 'r-o', lw=2)
ax.text(A[0], A[1], "A", fontsize=11, ha="right", va="top")
ax.text(B[0], B[1], "B", fontsize=11, ha="left",  va="top")

# Εξωτερικός κύκλος
ax.plot(R_out*np.cos(t), R_out*np.sin(t), lw=2, label="Εξωτερικός κύκλος")

# Εσωτερικός κύκλος
ax.plot(R_in*np.cos(t), R_in*np.sin(t), lw=2, label="Εσωτερικός κύκλος")

# ---------- ΙΧΝΟΣ (locus) ----------
theta = np.linspace(0, 2*np.pi, 400)
x_locus = (a/2) * np.cos(theta)
y_locus = (a/np.pi) * np.sin(theta)
ax.plot(x_locus, y_locus, '--', lw=2, label="Ίχνος")

# ---------- ΑΡΙΘΜΗΤΙΚΑ ----------
perimeter = 2 * np.pi * R_out
ZT = np.pi * R_in

ax.text(0.02, 0.98, f"ZΘ ≈ {ZT:.5f}", transform=ax.transAxes, va="top")
ax.text(0.02, 0.93, f"Περίμετρος ≈ {perimeter:.5f}", transform=ax.transAxes, va="top")

# ---------- ΤΕΛΙΚΑ ----------
ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend(loc="lower right")

st.pyplot(fig)

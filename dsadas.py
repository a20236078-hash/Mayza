import streamlit as st
import tkinter as tk

def responder_si():
    label.config(text="¡Gracias! Tú también me caes genial 😎")

def responder_no():
    label.config(text="En 2026 hablamos, bye 👋")

# Crear la ventana principal
root = tk.Tk()
root.title("Pregunta para ti 🤔")
root.geometry("400x200")        # Tamaño de la ventana
root.configure(bg="#add8e6")    # Fondo celeste (amistoso)

# Texto principal
label = tk.Label(root, 
                 text="¿Te caigo bien?", 
                 font=("Arial", 16, "bold"), 
                 bg="#add8e6", 
                 fg="black")
label.pack(pady=30)

# Botón "Sí"
boton_si = tk.Button(root, 
                     text="Sí 👍", 
                     command=responder_si, 
                     bg="green", 
                     fg="white", 
                     font=("Arial", 12, "bold"),
                     width=12)
boton_si.pack(side="left", padx=40)

# Botón "No"
boton_no = tk.Button(root, 
                     text="No 👎", 
                     command=responder_no, 
                     bg="gray", 
                     fg="white", 
                     font=("Arial", 12, "bold"),
                     width=12)
boton_no.pack(side="right", padx=40)

# Iniciar ventana
root.mainloop()

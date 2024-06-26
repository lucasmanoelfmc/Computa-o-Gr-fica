import tkinter as tk
import customtkinter as ctk
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from opengl_frame import AppOgl

def main():
    root = tk.Tk()
    root.title("Computação Gráfica")
    root.geometry("1000x600")
    root.configure(background="#000C66")

    # Frame para o lado esquerdo
    frame_left = tk.Frame(root, width=150, height=600)
    frame_left.configure(background="#000C66")
    frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    # Frame intermediário1
    frame_mid1 = tk.Frame(root, width=75, height=600)
    frame_mid1.configure(background="#000C66")
    frame_mid1.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    # Frame intermediário2
    frame_mid2 = tk.Frame(root, width=75, height=600)
    frame_mid2.configure(background="#000C66")
    frame_mid2.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

    # Frame para o lado direito
    frame_right = tk.Frame(root, width=700, height=600)
    frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
    
    # Adicionar o frame OpenGL ao lado direito
    ogl_frame = AppOgl(frame_right, width=700, height=600)
    ogl_frame.pack(fill=tk.BOTH, expand=False)  # Definindo expand=False para manter o tamanho fixo

    ogl_frame.animate = 1

    # Botão para desenhar um quadrado, chama a função desejada ao apertar botão(command=funcao_executada)
    btn_desenhar_quadrado = tk.Button(frame_left, text="Desenhar\nQuadrado", command=lambda: ogl_frame.square_points(int(entry_tamanho.get())))
    btn_desenhar_quadrado.pack()

    # Caixa de entrada para o tamanho do quadrado
    entry_tamanho = ctk.CTkEntry(frame_left, placeholder_text="size", height=10, width=40)
    entry_tamanho.pack(pady=0)

    # Botão para Escala
    btn_scale = tk.Button(frame_left, text="Aplicar\nEscala", command=lambda: ogl_frame.escala(float(entry_sx.get()), float(entry_sy.get()))) #Converter para int sempre que chamar a função
    btn_scale.pack()

    # Caixa de entrada para Fator de escala Sx
    entry_sx = ctk.CTkEntry(frame_left, placeholder_text="sx", height=10, width=40)
    entry_sx.pack(pady=0)

    # Caixa de entrada para Fator de escala Sy
    entry_sy = ctk.CTkEntry(frame_left, placeholder_text="sy", height=10, width=40)
    entry_sy.pack(pady=0)

    # Botão para Translação
    btn_translate = tk.Button(frame_left, text="Aplicar\nTranslação", command=lambda: ogl_frame.translacao(int(entry_tx.get()), int(entry_ty.get())))
    btn_translate.pack()

    # Caixa de entrada para Translação Tx
    entry_tx = ctk.CTkEntry(frame_left, placeholder_text="Tx", height=10, width=40)
    entry_tx.pack(pady=0)

    # Caixa de entrada para Translação Ty
    entry_ty = ctk.CTkEntry(frame_left, placeholder_text="Ty", height=10, width=40)
    entry_ty.pack(pady=0)

    # Botão para Rotação
    btn_translate = tk.Button(frame_left, text="Aplicar\nRotação", command=lambda: ogl_frame.rotacao(int(entry_rot.get())))
    btn_translate.pack()

    # Caixa de entrada para ângulo de Rotação
    entry_rot = ctk.CTkEntry(frame_left, placeholder_text="ang", height=10, width=40)
    entry_rot.pack(pady=0)

    # Botão para Cisalhamento
    btn_translate = tk.Button(frame_left, text="Aplicar\nCisalhamento", command=lambda: ogl_frame.cisalhamento(int(entry_a.get()), int(entry_b.get())))
    btn_translate.pack()

    # Caixa de entrada para Fator A de cisalhamento
    entry_a = ctk.CTkEntry(frame_left, placeholder_text="a", height=10, width=40)
    entry_a.pack(pady=0)

    # Caixa de entrada para Fator B de cisalhamento
    entry_b = ctk.CTkEntry(frame_left, placeholder_text="b", height=10, width=40)
    entry_b.pack(pady=0)

    # Botão para Reflexão em X
    btn_translate = tk.Button(frame_mid1, text="Ref X", command=lambda: ogl_frame.reflexaoX())
    btn_translate.pack()

    # Botão para Reflexão em Y
    btn_translate = tk.Button(frame_mid1, text="Ref Y", command=lambda: ogl_frame.reflexaoY())
    btn_translate.pack()

    # Botão para Reflexão na Origem
    btn_translate = tk.Button(frame_mid1, text="Ref Origem", command=lambda: ogl_frame.reflexaoOrigem())
    btn_translate.pack()

    # Botão para Reflexão na Reta de 45 graus
    btn_translate = tk.Button(frame_mid1, text="Ref Reta 45", command=lambda: ogl_frame.reflexao45())
    btn_translate.pack()

    # Botão para Reflexão Qualquer
    btn_translate = tk.Button(frame_left, text="Aplicar\nReflexao\nQualquer", command=lambda: ogl_frame.reflexaoQualquer(float(entry_m.get()), float(entry_b_reta.get())))
    btn_translate.pack()

    # Caixa de entrada para M da Reta da Reflexão Qualquer
    entry_m = ctk.CTkEntry(frame_left, placeholder_text="m", height=10, width=40)
    entry_m.pack(pady=0)

    # Caixa de entrada para B da Reta da Reflexão Qualquer
    entry_b_reta = ctk.CTkEntry(frame_left, placeholder_text="b", height=10, width=40)
    entry_b_reta.pack(pady=0)

    root.mainloop()

if __name__ == '__main__':
    main()
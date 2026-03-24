import tkinter as tk

# ── DICCIONARIO COMPLETO DE ERRORES ─────────────────────────
errores = [
    # PYTHON
    {"num":"01","lenguaje":"Python","nombre":"KeyError",
     "descripcion":"Clave no existe en diccionario",
     "error":"d={'a':1}\nprint(d['b'])",
     "solucion":"print(d.get('b','No existe'))",
     "tip":"Usa get()"},

    {"num":"02","lenguaje":"Python","nombre":"IndexError",
     "descripcion":"Indice fuera de rango",
     "error":"l=[1,2]\nprint(l[5])",
     "solucion":"if 5<len(l): print(l[5])",
     "tip":"Valida tamaño"},

    {"num":"03","lenguaje":"Python","nombre":"TypeError",
     "descripcion":"Tipos incompatibles",
     "error":"'2'+2",
     "solucion":"int('2')+2",
     "tip":"Convierte tipos"},

    {"num":"04","lenguaje":"Python","nombre":"ZeroDivisionError",
     "descripcion":"Dividir entre cero",
     "error":"5/0",
     "solucion":"if x!=0: 5/x",
     "tip":"Evita dividir por 0"},

    {"num":"05","lenguaje":"Python","nombre":"NameError",
     "descripcion":"Variable no definida",
     "error":"print(x)",
     "solucion":"x=10\nprint(x)",
     "tip":"Declara variables"},

    {"num":"06","lenguaje":"Python","nombre":"AttributeError",
     "descripcion":"Metodo no existe",
     "error":"'hola'.append('x')",
     "solucion":"lista=[]\nlista.append('x')",
     "tip":"Revisa métodos"},

    {"num":"07","lenguaje":"Python","nombre":"ValueError",
     "descripcion":"Valor inválido",
     "error":"int('abc')",
     "solucion":"try:\n int('abc')\nexcept:\n print('Error')",
     "tip":"Usa try/except"},

    {"num":"08","lenguaje":"Python","nombre":"ImportError",
     "descripcion":"Modulo inexistente",
     "error":"import fake",
     "solucion":"pip install modulo",
     "tip":"Instala librerías"},

    {"num":"09","lenguaje":"Python","nombre":"IndentationError",
     "descripcion":"Indentación incorrecta",
     "error":"if True:\nprint('x')",
     "solucion":"if True:\n    print('x')",
     "tip":"Respeta espacios"},

    {"num":"10","lenguaje":"Python","nombre":"SyntaxError",
     "descripcion":"Error de sintaxis",
     "error":"if True print('x')",
     "solucion":"if True:\n print('x')",
     "tip":"Usa ':'"},

    {"num":"11","lenguaje":"Python","nombre":"TypeError None",
     "descripcion":"Operar con None",
     "error":"None+1",
     "solucion":"if x is not None:",
     "tip":"Valida None"},

    {"num":"12","lenguaje":"Python","nombre":"RecursionError",
     "descripcion":"Recursión infinita",
     "error":"def f(): f()",
     "solucion":"def f(n):\n if n==0:return",
     "tip":"Caso base"},

    {"num":"13","lenguaje":"Python","nombre":"MemoryError",
     "descripcion":"Sin memoria",
     "error":"a=[1]*10**10",
     "solucion":"usar generadores",
     "tip":"Optimiza memoria"},

    {"num":"14","lenguaje":"Python","nombre":"AssertionError",
     "descripcion":"Assert falla",
     "error":"assert False",
     "solucion":"assert 5>3",
     "tip":"Condición correcta"},

    # JAVA
    {"num":"15","lenguaje":"Java","nombre":"NullPointerException",
     "descripcion":"Objeto null",
     "error":"s.length();",
     "solucion":"if(s!=null){}",
     "tip":"Verifica null"},

    {"num":"16","lenguaje":"Java","nombre":"ArrayIndexOutOfBounds",
     "descripcion":"Indice inválido",
     "error":"a[5];",
     "solucion":"if(i<a.length){}",
     "tip":"Usa length"},

    {"num":"17","lenguaje":"Java","nombre":"NumberFormatException",
     "descripcion":"Texto a número",
     "error":"Integer.parseInt('a');",
     "solucion":"try{}catch{}",
     "tip":"Valida datos"},

    {"num":"18","lenguaje":"Java","nombre":"ClassCastException",
     "descripcion":"Cast inválido",
     "error":"(Integer)'hola';",
     "solucion":"instanceof",
     "tip":"Verifica tipo"},

    {"num":"19","lenguaje":"Java","nombre":"StackOverflowError",
     "descripcion":"Recursión infinita",
     "error":"f();",
     "solucion":"caso base",
     "tip":"Detener recursión"},

    {"num":"20","lenguaje":"Java","nombre":"ArithmeticException",
     "descripcion":"División por cero",
     "error":"5/0;",
     "solucion":"if(b!=0){}",
     "tip":"Evita 0"},

    {"num":"21","lenguaje":"Java","nombre":"IllegalArgumentException",
     "descripcion":"Argumento inválido",
     "error":"metodo(-1);",
     "solucion":"validar input",
     "tip":"Chequea valores"},

    {"num":"22","lenguaje":"Java","nombre":"IOException",
     "descripcion":"Error IO",
     "error":"leer archivo",
     "solucion":"try/catch",
     "tip":"Maneja archivos"},

    {"num":"23","lenguaje":"Java","nombre":"FileNotFoundException",
     "descripcion":"Archivo no existe",
     "error":"open('x')",
     "solucion":"verificar ruta",
     "tip":"Revisa path"},

    {"num":"24","lenguaje":"Java","nombre":"InterruptedException",
     "descripcion":"Hilo interrumpido",
     "error":"sleep()",
     "solucion":"try/catch",
     "tip":"Maneja hilos"},

    {"num":"25","lenguaje":"Java","nombre":"OutOfMemoryError",
     "descripcion":"Sin memoria",
     "error":"new int[999999999]",
     "solucion":"optimizar",
     "tip":"Cuida memoria"},

    {"num":"26","lenguaje":"Java","nombre":"NoSuchMethodError",
     "descripcion":"Método no existe",
     "error":"obj.x()",
     "solucion":"revisar métodos",
     "tip":"Compilar bien"},

    {"num":"27","lenguaje":"Java","nombre":"NoClassDefFoundError",
     "descripcion":"Clase no encontrada",
     "error":"new X()",
     "solucion":"classpath",
     "tip":"Configura proyecto"},

    {"num":"28","lenguaje":"Java","nombre":"IllegalStateException",
     "descripcion":"Estado inválido",
     "error":"uso incorrecto",
     "solucion":"orden correcto",
     "tip":"Controla flujo"},
]

# ── INTERFAZ ───────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Repositorio de 28 Errores")
        self.geometry("900x600")

        self.lista = tk.Listbox(self, width=35)
        self.lista.pack(side="left", fill="y")

        self.texto = tk.Text(self, wrap="word")
        self.texto.pack(side="right", fill="both", expand=True)

        for e in errores:
            self.lista.insert("end", f"{e['num']} - {e['nombre']}")

        self.lista.bind("<<ListboxSelect>>", self.mostrar)

    def mostrar(self, event):
        i = self.lista.curselection()
        if not i:
            return

        e = errores[i[0]]

        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END,
            f"Lenguaje: {e['lenguaje']}\n\n"
            f"Error: {e['nombre']}\n\n"
            f"Descripción:\n{e['descripcion']}\n\n"
            f"❌ Código con error:\n{e['error']}\n\n"
            f"✅ Corrección:\n{e['solucion']}\n\n"
            f"💡 Tip:\n{e['tip']}"
        )

# ── EJECUCIÓN ──────────────────────────────────────────────
if __name__ == "__main__":
    App().mainloop()
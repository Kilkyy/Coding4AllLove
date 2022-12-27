import math
import sympy
import tkinter as tk

# Matematiksel işlemleri gerçekleştiren fonksiyonlar
def sin(x):
  return math.sin(x)

def cos(x):
  return math.cos(x)

def derivative(f, x):
  h = 1e-4
  return (f(x+h) - f(x)) / h

def integral(f, x):
  x = sympy.Symbol('x')
  result = sympy.integrate(f, x)
  return result

# Kullanıcı arayüzünü oluşturan fonksiyon
def create_calculator():
  # Pencere oluştur
  window = tk.Tk()
  window.title("Bilimsel Hesap Makinesi")

  # Girdi alanı oluştur
  input_field = tk.Entry(window)
  input_field.grid(row=0, column=0, columnspan=3)

  # Düğmeleri oluştur ve işlevlerini ata
  def button_click(number):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, str(current) + str(number))

  def button_clear():
    input_field.delete(0, tk.END)

  def button_equal():
    result = eval(input_field.get())
    input_field.delete(0, tk.END)
    input_field.insert(0, str(result))

  button_1 = tk.Button(window, text="1", command=lambda: button_click(1))
  button_2 = tk.Button(window, text="2", command=lambda: button_click(2))
  button_3 = tk.Button(window, text="3", command=lambda: button_click(3))
  button_4 = tk.Button(window, text="4", command=lambda: button_click(4))
  button_5 = tk.Button(window, text="5", command=lambda: button_click(5))
  button_6 = tk.Button(window, text="6", command=lambda: button_click(6))
  button_7 = tk.Button(window, text="7", command=lambda: button_click(7))
  button_8 = tk.Button(window, text="8", command=lambda: button_click(8))
  button_9 = tk.Button(window, text="9", command=lambda: button_click(9))
  button_0 = tk.Button(window, text="0", command=lambda: button_click(0))
    button_add = tk.Button(window, text="+", command=lambda: button_click("+"))
  button_subtract = tk.Button(window, text="-", command=lambda: button_click("-"))
  button_multiply = tk.Button(window, text="*", command=lambda: button_click("*"))
  button_divide = tk.Button(window, text="/", command=lambda: button_click("/"))
  button_decimal = tk.Button(window, text=".", command=lambda: button_click("."))
  button_sin = tk.Button(window, text="sin", command=lambda: button_click("sin("))
  button_cos = tk.Button(window, text="cos", command=lambda: button_click("cos("))
  button_derivative = tk.Button(window, text="derivative", command=lambda: button_click("derivative("))
  button_integral = tk.Button(window, text="integral", command=lambda: button_click("integral("))
  button_clear = tk.Button(window, text="C", command=button_clear)
  button_equal = tk.Button(window, text="=", command=button_equal)

  # Düğmeleri ekran üzerine yerleştir
  button_1.grid(row=3, column=0)
  button_2.grid(row=3, column=1)
  button_3.grid(row=3, column=2)
  button_4.grid(row=2, column=0)
  button_5.grid(row=2, column=1)
  button_6.grid(row=2, column=2)
  button_7.grid(row=1, column=0)
  button_8.grid(row=1, column=1)
  button_9.grid(row=1, column=2)
  button_0.grid(row=4, column=0)
  button_add.grid(row=4, column=1)
  button_subtract.grid(row=4, column=2)
  button_multiply.grid(row=5, column=0)
  button_divide.grid(row=5, column=1)
  button_decimal.grid(row=5, column=2)
  button_sin.grid(row=6, column=0)
  button_cos.grid(row=6, column=1)
  button_derivative.grid(row=6, column=2)
  button_integral.grid(row=7, column=0)
  button_clear.grid(row=7, column=1)

  


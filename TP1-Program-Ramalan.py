import math
from turtle import *
import random

def hearta(k):
    return 16 * math.sin(k)**3

def heartb(k):
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

def draw_heart():
    speed(0)
    color("#f73487")
    penup()
    goto(0, -200)
    pendown()
    begin_fill()
    for i in range(1000):
        k = i * math.pi / 500
        goto(hearta(k) * 20, heartb(k) * 20)
    end_fill()

def display_info(nama, umur, nama_pasangan, umur_pasangan, cocok):
    penup()
    goto(0, 50)
    color('white')
    write(f"{nama} [{umur}] tahun", align="center", font=("Arial", 16, "bold"))
    goto(0, 20)
    write(f"{nama_pasangan} [{umur_pasangan}] tahun", align="center", font=("Arial", 16, "bold"))
    goto(0, -10)
    write(f"Kecocokan: {cocok}%", align="center", font=("Arial", 16, "bold"))
    pendown()

def main():
    print("Selamat Datang Di Program Ramalan Cupu")
    print('+' * 40)

    print("Data Anda : ")
    print('\u2764' * 7)
    nama = input("Masukkan Nama Anda  : ")
    umur = int(input("Masukkan Umur Anda  : "))
    print("Data Pasangan Anda : ")
    print('\u2764' * 13)
    nama_pasangan = input("Masukkan Nama Pasangan Anda  : ")
    umur_pasangan = int(input("Masukkan Umur Pasangan Anda  : "))

    cocok = round(random.randint(50, 100) / 1.1, 2)

    input("Tekan ENTER untuk melihat pola love dan hasil ramalan...")

    bgcolor('black')
    penup()
    goto(0, 0)
    pendown()

    draw_heart()
    display_info(nama, umur, nama_pasangan, umur_pasangan, cocok)
    done()

if __name__ == "__main__":
    main()
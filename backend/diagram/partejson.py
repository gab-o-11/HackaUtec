# generar_mermaid.py

print("🔷 Ingresa tu diagrama Mermaid línea por línea. Escribe una línea vacía para terminar:")

lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

chart = "\n".join(lines)

with open("state_diagram.mmd", "w") as f:
    f.write(chart)


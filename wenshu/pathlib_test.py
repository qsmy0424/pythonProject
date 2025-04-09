from pathlib import Path
import random

p = Path("C:\\Users\\qsmy\\Desktop\\99a75eb2f320250311100209.png")

print(p.name)
print(p.suffix)
print(p.stat)
print(p.parent)
print(p.stem)

print(p.exists())
print(p.is_dir())

print(p.is_file())

n1 = Path("C:\\Users\\qsmy\\Desktop\\123")
n1.mkdir(exist_ok=True)

n2 = Path("C:\\Users\\qsmy\\Desktop\\123\\123.txt")

n2.touch()

print(n2.read_text(encoding="utf-8"))
n2.write_text("123")
print(n2.read_text())
n2.write_text("456")
print(n2.read_text())


p_top = Path(".")
# for item in p_top.iterdir():
#     print(item)

for file in p_top.glob("*.py"):
    print(file)

n2.unlink()

n3 = Path("C:\\Users\\qsmy\\Desktop\\.env")
with n3.open(mode="r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


name = "qsmy"
age = 18
print(f"my name is {name}, age is {age}")

print(name[::-1])
print(name[::-2])


list = [1, 2, 3, 4, 5, "python"]

print(list[1:3])

print(list[1 : (1 + 1)])

print(len(list))

print(random.choice(list))

print(random.choices(list, k=4))


print(random.sample(list, k=len(list)))
print(random.sample(list, k=len(list)))
print(random.sample(list, k=len(list)))

print(list)

random.shuffle(list)
print(list)

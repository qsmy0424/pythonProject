with open('url.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

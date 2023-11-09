
heart = []
for y in range(30, -30, -1):
    line = []
    for x in range(-50, 50):
        if ((x*0.025)**2 + (y*0.1)**2-1)**3 - (x*0.025)**2*(y*0.1)**3 <= 0:
            line.append('Я люблю'[(x - y) % 7])
        else:
            line.append(' ')
    heart.append(''.join(line))
print('\n'.join(heart))

s = 'i love Python so much'
file = open("filename.txt", "w")
file.write(s[7::])
file.close()
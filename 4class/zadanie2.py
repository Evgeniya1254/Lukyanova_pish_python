string = "abracadabra"
podschet = {}

for char in string:
    if char in podschet:
        podschet[char] += 1
    else:
        podschet[char] = 1

print(podschet)
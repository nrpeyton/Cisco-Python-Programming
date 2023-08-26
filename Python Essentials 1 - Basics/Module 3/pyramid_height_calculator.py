blocks = int(input("Enter the number of blocks: "))

this_layer = 0
total_required = 0
height = 0

while total_required < blocks:
    this_layer += 1
    this_layer_blocks = this_layer + 1
    total_required = total_required + this_layer_blocks
    height += 1

print("The height of the pyramid:", height,"\n")


for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
    
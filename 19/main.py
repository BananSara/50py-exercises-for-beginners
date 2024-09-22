def replace_number():
    print('99 bottles of beer on the wall,99 bottles of beer')
    for i in range(99, 0, -1):
        text = 'Take one down, pass it around,' + str(i-1) +   ' bottles of beer on the wall.'
        update_text = text.replace('99', str(i))
        print(update_text)

print(replace_number())
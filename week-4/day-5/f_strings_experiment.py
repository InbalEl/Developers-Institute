l = ['-', '-', '-']

f_string = f'{l[0]} | {l[1]} | {l[2]}'
dot_format = '{} | {} | {}'.format(l[0], l[1], l[2])

print(f_string)
l[1] = 'X'
print(f_string)
dot_format = '{} | {} | {}'.format(l[0], l[1], l[2])
print(dot_format)

from string import Template


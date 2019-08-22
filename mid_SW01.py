in1, in2, in3 = input().split()
if (in1 == 'A'):
  print(int(in2) + int(in3))
elif (in1 == '%'):
  print(int(in2) % int(in3))
elif (in1 == 'S'):
  print(int(in2) - int(in3))
elif (in1 == '>'):
  print(int(in2>in3))
elif (in1 == '<'):
  print(int(in2<in3))
else:
  print('Invalid Operation!')

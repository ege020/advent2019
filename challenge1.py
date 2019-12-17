<<<<<<< HEAD
filepath = 'challenge1.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   total = 0
   while line:
       fuel = (int(line)//3)-2
       total += fuel
       if fuel > 6:
          line = fuel
          continue
       line = fp.readline()
       cnt += 1

=======
filepath = 'challenge1.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   total = 0
   while line:
       fuel = (int(line)//3)-2
       total += fuel
       if fuel > 6:
          line = fuel
          continue
       line = fp.readline()
       cnt += 1

>>>>>>> ba80abafa32e5830856c4f742bd5eafc5ce3bbc9
print(total)
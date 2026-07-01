try:
  a=10
  b=0
  c=a/b
  print(c)
except Exception as e:
  print("Error:" , e)

finally:
  print("I Always Run")

#Zero Division Error:division by Zero
#NameError:name 'x' is not defind
#TypeError:unsupported operand type(s) for/: 'int' and 'str'
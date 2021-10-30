#Enter a string
a='amma'
half=int(len(a)/2)
if len(a)%2==0:
  first=a[half:]
  last=a[:half]
else:
  first=a[half:]
  last=a[:half+1]
if first==last:
  print('The given string is a symmertical')
else:
  print('The given string is not symmertical')
if first==last[::-1]:
  print('The given string is a palindrome')
else:
  print('The given string is not a palindrome')
  

  
  
  
 
  

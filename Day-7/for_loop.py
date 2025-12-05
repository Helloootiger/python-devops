# for loop

for i in range(5):
   print(i)

for x in range(5):
   print("Hello")

#break condition

for i in range(5):
   if i == 3:
      break 
   print(i)

#continue/skip condition

for i in range(5):
   if i == 3:
      continue 
   print(i)

#using variable

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
      print(line)

   if "ERROR" in line:
      break
   print(line)

# here output will be interesting 
#INFO: Operation successful
#ERROR: File not found - because first if "ERROR" performed but since first line has no error its skipped, second if as well don't find error so it will keep on printing till finding an error.

#if we want 2 errors to be printted we should not include break, break will stop the loop as soon as it find first error.

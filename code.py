def my_function(nums, groups):
  result = True
  for x in nums:
       result = any(x in sl for sl in groups)
       if result == False:
           return False


  return result

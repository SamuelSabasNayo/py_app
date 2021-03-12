def find_max(arr):
  maximum_num = arr[0]
  for i in arr:
    if i > maximum_num:
      maximum_num = i
  return maximum_num

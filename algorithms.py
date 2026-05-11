# Write your CUSTOM search algorithm (a function) and an sorting algorithm (a function) AS DESCRIBED IN THE ASSIGNMENT INSTRUCTIONS here
# You MAY NOT USE any pre-built python functions
def partition(contact_list, left, right):
  middle = (left + right) // 2
  pivot = contact_list[middle]
  contact_list[middle], contact_list[right] = contact_list[right], contact_list[middle]

  boundary = left
  for index in range(left, right):
    if contact_list[index] < pivot:
      contact_list[index], contact_list[boundary] = contact_list[boundary], contact_list[index]
      boundary += 1

  contact_list[right], contact_list[boundary] = contact_list[boundary], contact_list[right]

  return boundary

def quick_recurse(contact_list, left, right):
  if left >= right:
    return
  pivot_position = partition(contact_list, left, right)

  quick_recurse(contact_list, left, pivot_position - 1)
  quick_recurse(contact_list, pivot_position + 1, right)
  
def quick_sort(contact_list):
   quick_recurse(contact_list, 0, len(contact_list) - 1)

def binary_search(contact_list, lower_index, upper_index, target_contact);
  if lower_index <= upper_index:
    midpoint_index = (lower_index + upper_index) // 2

    print("lower index:", lower_index)
    print("upper index:", upper_index)
    print("midpoint index:", midpoint_index)

    if contact_list[midpoint_index] == target_contact:
      return midpoint_index

    elif (contact_list [midpoint_index] > target_contact:
      return binary_search(contact_list, lower_index, midpoint_index - 1, target_contact)

    else:
      return binary_search(contact_list, midpoint_index + 1, upper_index, target_contact)

return -1


  

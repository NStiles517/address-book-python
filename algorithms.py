# Write your CUSTOM search algorithm (a function) and an sorting algorithm (a function) AS DESCRIBED IN THE ASSIGNMENT INSTRUCTIONS here
# You MAY NOT USE any pre-built python functions
import main
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

  quick_recurse(contact_list, left, pivot_position -1)
  quick_recurse(contact_list, pivot_position +1, right)

def quick_sort(contact_list):

    quick_recurse(contact_list, 0, len(contact_list) - 1)



  

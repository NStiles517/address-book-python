# Create your Contact class here
class Contact():
  def __init__(self, first_name, last_name, phone_number):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
  def __eq__(self, other):
    if self.first_name == other.first_name and self.last_name == other.last_name:
      return True
    else:
      return False

def __lt__(self, other):
  if self.first_name < other.first_name:
    return True
  else:
    return False

def __gt__(self, other):
  if self.first_name > other.first_name:
    return True
  else:
    return False


    
  
  
    

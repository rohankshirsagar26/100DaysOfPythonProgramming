# Functions with outputs

def format_name():
  f_name = input("First Name: ")
  l_name = input("Last Name: ")
  if f_name == "" or l_name == "":
    return
  return f"Result: {f_name.title()} {l_name.title()}"

print(format_name())
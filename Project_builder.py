import os 

def dir_create(directory: str) -> None:
  if not os.path.exists(directory):
      os.makedirs(directory)


class project_creator:
  def __init__(self) -> None:
    self.project_name = input("Enter the name of the project: ")
    self.project_path = input("Enter the path of the project: ")
    self.project_description = input("Enter the description of the project: ")


  def create_project(self):
    dir_create(self.project_path)
    dir_create(f"{self.project_path}\{self.project_name}")
    with open(f"{self.project_path}\{self.project_name}\{self.project_name}" + ".py", "w") as main:
      main.write(8 * "#" + " " + self.project_name + " " + 8 * "#" + "\n" + f"\n ####{self.project_description}####")
      



project = project_creator()
project.create_project()
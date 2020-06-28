import cx_Freeze 
  
executables = [cx_Freeze.Executable(script="main.py", icon="assets\icone.ico")]

cx_Freeze.setup(name='RecycleEdu',
    options={'build_exe': {'packages': ['pygame'],
                           "include_files":["Assets", "engine"]
                           }}, executables=executables
   
)
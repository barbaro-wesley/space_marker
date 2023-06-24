import cx_Freeze
executables = [
    cx_Freeze.Executable(script="trabalho.py", icon="icone.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options = {
        "build_exe":{
            "packages": ["pygame"],
            "include_files": [
                "bg.jpg",
                "space.png"
            ]
        }
    } , executables = executables
)


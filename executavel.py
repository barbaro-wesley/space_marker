import cx_Freeze

executables = [
    cx_Freeze.Executable("trabalho.py", base="Win32GUI", icon="space_icone.png")
]

cx_Freeze.setup(
    name="Space Marker",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": [
                "bg.jpg",
                "space_icone.jpg",
                "novatrilha.mp3"
            ]
        }
    },
    executables=executables
)


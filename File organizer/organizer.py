from pathlib import Path

fls_cats = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
}
def exts(exxx):
    for cats,exts in fls_cats.items():
        if exxx.lower() in exts:
            return cats
    return "others"

def create(bspt,fldnm):
    fldpth = bspt/fldnm
    if not fldpth.exists():
        print(f"creating folder {fldnm} in {fldpth}")
        fldpth.mkdir()
    return fldpth

def move(flpth,tfldr):
    dstn = tfldr/flpth.name
    print(f"Moving {flpth.name} to {dstn.name}")
    flpth.rename(dstn)

print("File Chaos Terminator initialing")

dir = Path("./Files & Folders")
print("directory: ", dir.resolve())

for item in dir.iterdir():
    if item.is_file():
        category = exts(item.suffix)
        # print(f"File: {item.name} | Extention: {item.suffix}")
        # print(f"this nigga belongs to {category}")
        print(f"This Nigga the {item.stem} with {item.suffix} extention belongs in {category} folder.")
        folder = create(dir,category)
        move(item,folder)



print("File Chaos Terminator initialized")
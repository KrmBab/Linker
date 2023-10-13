import os

PATHDist = "Widgets"
PATHSrc = "GUI"
if __name__ == "__main__":

    files = os.listdir(PATHSrc)
    for f in files:
        if ".ui" in f:
            os.system(f'pyside6-uic {PATHSrc}/{f} -o {PATHDist}/{f.replace(".ui", ".py")}')

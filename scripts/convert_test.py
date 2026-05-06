import json, glob
        
for path in glob.glob("**/*.ipynb", recursive=True):
        nb = json.load(open(path))
        new_cell = {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": ["print('Action이 추가했어요!')"]
        }
        nb["cells"].append(new_cell)
        json.dump(nb, open(path, "w"), ensure_ascii=False, indent=2)
        print(f"수정완료: {path}")
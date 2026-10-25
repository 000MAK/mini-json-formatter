import argparse,json
from pathlib import Path

def format_json(source,destination):
    src,dst=Path(source).resolve(),Path(destination).resolve()
    if src==dst: raise ValueError("Output must differ from input")
    if dst.exists(): raise FileExistsError(dst)
    data=json.loads(src.read_text(encoding="utf-8-sig"))
    dst.parent.mkdir(parents=True,exist_ok=True); dst.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return data

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("output"); a=ap.parse_args(); format_json(a.input,a.output); print(f"Valid JSON formatted to {a.output}")
if __name__=="__main__": main()

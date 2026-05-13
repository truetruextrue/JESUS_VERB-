import os
import json
import datetime

AUDIO_EXTS = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'}
VIDEO_EXTS = {'.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv'}
MEDIA_EXTS = AUDIO_EXTS | VIDEO_EXTS

CATALOG_FILE = "catalogo_media.json"
LOG_FILE = "scan_media.log"

def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")

def get_media_type(extension):
    ext = extension.lower()
    if ext in AUDIO_EXTS:
        return "áudio"
    elif ext in VIDEO_EXTS:
        return "vídeo"
    return "desconhecido"

def scan_media_files(root_dir="."):
    catalog = []
    log("Iniciando varredura de mídia.")
    for folder, _, files in os.walk(root_dir):
        for fname in files:
            _, ext = os.path.splitext(fname)
            if ext.lower() in MEDIA_EXTS:
                relpath = os.path.relpath(os.path.join(folder, fname), root_dir)
                fstat = os.stat(os.path.join(folder, fname))
                size_mb = round(fstat.st_size / (1024*1024), 2)
                mtime = datetime.datetime.fromtimestamp(fstat.st_mtime)
                media_type = get_media_type(ext)
                entry = {
                    "nome": fname,
                    "caminho_relativo": relpath,
                    "tamanho_MB": size_mb,
                    "data_modificacao": mtime.strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": media_type
                }
                catalog.append(entry)
                log(f"Arquivo encontrado: {relpath} ({media_type}, {size_mb} MB)")
    log(f"Total de arquivos de mídia encontrados: {len(catalog)}")
    return catalog

def main():
    catalog = scan_media_files(".")
    with open(CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    log(f"Catálogo salvo em {CATALOG_FILE}")

if __name__ == "__main__":
    main()

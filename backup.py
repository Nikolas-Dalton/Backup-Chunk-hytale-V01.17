import os
import shutil
from pathlib import Path

def get_hytale_region_filename(chunk_x: int, chunk_z: int) -> str:
    """
    Converte coordenadas globais de chunk do Hytale para o nome do arquivo da região.
    """
    region_size = 32  # Hytale usa regiões de 32x32 chunks
    region_x = chunk_x // region_size
    region_z = chunk_z // region_size
    return f"{region_x}.{region_z}.region.bin"

def backup_specific_regions(chunk_coordinates):
    # Define o diretório atual onde o script está rodando (onde devem estar os .bin)
    source_dir = Path.cwd()
    backup_dir = source_dir / "backup"

    # 1. Cria a pasta de backup se não existir
    if not backup_dir.exists():
        backup_dir.mkdir()
        print(f"📁 Pasta criada: {backup_dir}")
    else:
        print(f"📁 Pasta de backup encontrada: {backup_dir}")

    # 2. Calcula os nomes dos arquivos e remove duplicatas usando set()
    files_to_backup = set()

    print(f"\n--- Processando {len(chunk_coordinates)} coordenadas de chunk ---")

    for x, z in chunk_coordinates:
        filename = get_hytale_region_filename(x, z)
        files_to_backup.add(filename)
        # Opcional: Mostrar qual chunk virou qual arquivo
        # print(f"Chunk ({x}, {z}) -> {filename}")

    print(f"ℹ️  Total de arquivos de região únicos encontrados: {len(files_to_backup)}")
    print("-" * 40)

    # 3. Copia os arquivos
    success_count = 0
    missing_count = 0

    for filename in files_to_backup:
        source_file = source_dir / filename
        dest_file = backup_dir / filename

        if source_file.exists():
            try:
                # copy2 preserva metadados (datas de modificação, etc)
                shutil.copy2(source_file, dest_file)
                print(f"✅ Copiado: {filename}")
                success_count += 1
            except Exception as e:
                print(f"❌ Erro ao copiar {filename}: {e}")
        else:
            print(f"⚠️  Arquivo não encontrado na pasta atual: {filename}")
            missing_count += 1

    # Resumo final
    print("-" * 40)
    print(f"Concluído! {success_count} arquivos copiados. {missing_count} arquivos ausentes.")

if __name__ == "__main__":
    # --- INSIRA SUAS COORDENADAS AQUI ---
    # Formato: (ChunkX, ChunkZ) - Os números que aparecem dentro do "in (...)"
    my_chunks = [
        (-16, 2),    # Exemplo da sua imagem
        (-55, 3),    # Vizinho (mesmo arquivo)
        (-16, 2),    # Duplicata intencional para teste
    ]

    backup_specific_regions(my_chunks)

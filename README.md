# 🗺️ Hytale Region Backup Script

Um script em **Python** para criar **backup seletivo de regiões** de um save do **Hytale**, baseado em coordenadas específicas de **chunks**.

Em vez de copiar o mundo inteiro, o script identifica quais arquivos `.region.bin` realmente são necessários e salva apenas eles em uma pasta de backup.

---

## ✨ Funcionalidades

* 🔢 Converte coordenadas globais de chunk `(x, z)` em arquivos de região do Hytale
* 📦 Remove duplicatas automaticamente (mesma região não é copiada duas vezes)
* 📁 Cria a pasta `backup/` automaticamente
* 🗂️ Copia apenas os arquivos de região relevantes
* 🕒 Preserva metadados dos arquivos originais (`shutil.copy2`)
* ⚠️ Exibe avisos caso algum arquivo de região não seja encontrado

---

## 📌 Requisitos

* **Python 3.x** instalado no computador
* O script deve ser executado **na pasta onde estão os arquivos `.region.bin`** do save

---

## ▶️ Como usar

### 1️⃣ Configure os chunks

No final do arquivo, adicione as coordenadas dos chunks que você deseja salvar:

```python
my_chunks = [
    (-16, 2),
    (-55, 3),
]
```

> 💡 Use exatamente os valores `(ChunkX, ChunkZ)` que aparecem no jogo ou em ferramentas de visualização de mapa.

---

### 2️⃣ Posicione o script

Coloque o arquivo `.py` **dentro da pasta que contém os arquivos de região do seu save** do Hytale.

Exemplo:

```
MeuSave/
├── -1.0.region.bin
├── -2.0.region.bin
├── 0.0.region.bin
└── backup_regions.py
```

---

### 3️⃣ Execute o script

No terminal, execute:

```bash
python backup_regions.py
```

---

### 4️⃣ Resultado

* Os arquivos de região correspondentes serão copiados para a pasta:

```
backup/
```

* O terminal exibirá um resumo com:

  * Quantos arquivos foram copiados
  * Quantos arquivos estavam ausentes

---

## 🧠 Como funciona

* O Hytale utiliza **regiões de 32x32 chunks**
* O script converte as coordenadas globais de chunk para o formato:

```
regionX.regionZ.region.bin
```

* Se múltiplos chunks pertencem à mesma região, o arquivo é copiado **apenas uma vez**

---

## 🛠️ Casos de uso

* Backup parcial de mundos
* Migração seletiva de mapas
* Proteção de áreas importantes do save
* Debug e análise de regiões específicas

---

## ⚠️ Observações importantes

* O script **não modifica** nenhum arquivo original
* Apenas arquivos existentes são copiados
* Arquivos ausentes são ignorados com aviso no terminal

---

## 📜 Licença

Uso livre para fins pessoais ou educacionais.

---

Se quiser contribuir, melhorar ou adaptar para outros formatos de save, fique à vontade 🚀

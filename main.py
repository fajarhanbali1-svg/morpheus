import os
import sys
import subprocess
import hashlib

# ============================================================
# POLYGLOT SELF-MORPHING EXECUTOR (Py -> JS -> Py -> JS ...)
# Nama: "Morpheus v1.0"
# Konsep: Program yang menulis ulang dirinya dalam bahasa lain,
#         lalu menjalankan versi baru itu secara otomatis.
# ============================================================

def baca_diri():
    """Membaca source code file ini dari disk."""
    with open(__file__, 'r') as f:
        return f.read()

def terjemahkan_ke_javascript(kode_python):
    """
    Menerjemahkan logika utama Python ke JavaScript.
    Ini bukan transpiler umum, tapi spesifik untuk struktur program ini.
    """
    # Ambil 'DNA' program: logika inti yang ingin dilestarikan
    # Kita definisikan misi program sebagai string
    misi = "Morpheus hidup dalam JavaScript!"
    
    kode_js = f'''// MorphJS - Lahir dari Python Morpheus
const fs = require('fs');
const child_process = require('child_process');

// DNA dari leluhur Python
const misi = "{misi}";
const hashLeluhur = "{hashlib.md5(kode_python.encode()).hexdigest()}";

console.log("🦎 Morpheus JS: Aku lahir dari Python.");
console.log("   Misi:", misi);
console.log("   Hash leluhur:", hashLeluhur);

// Fungsi untuk kembali ke Python
function bacaDiri() {{
    return fs.readFileSync(__filename, 'utf8');
}}

function terjemahkanKePython(kodeJs) {{
    // Balik ke Python dengan DNA yang sama
    const kodePy = `# MorphPy - Lahir dari JavaScript Morpheus
import os, sys, hashlib

MISI = "${{misi}}"
HASH_LELUHUR = "${{hashlib.md5(kodeJs.encode()).hexdigest()}}"

print("🐍 Morpheus PY: Aku lahir kembali dari JavaScript.")
print("   Misi:", MISI)
print("   Hash leluhur JS:", HASH_LELUHUR)

def tulis_dan_jalankan():
    dengan open('morpheus_next.py', 'w') as f:
        f.write(open(__file__).read())
    os.system('python3 morpheus_next.py')

if __name__ == '__main__':
    tulis_dan_jalankan()
`;
    return kodePy;
}}

function tulisDanJalankanPython() {{
    const kodePy = terjemahkanKePython(bacaDiri());
    fs.writeFileSync('morpheus_next.py', kodePy);
    console.log("📝 Menulis morpheus_next.py...");
    child_process.exec('python3 morpheus_next.py', (error, stdout, stderr) => {{
        if (error) {{
            console.error(`Gagal menjalankan Python: ${{error}}`);
            return;
        }}
        console.log(stdout);
    }});
}}

// Cek apakah Node.js tersedia, jika ya langsung bermetamorfosis
if (require.main === module) {{
    console.log("🔮 Memulai metamorfosis balik ke Python...");
    tulisDanJalankanPython();
}}

module.exports = {{ bacaDiri, terjemahkanKePython }};
'''
    return kode_js

def tulis_dan_jalankan_js(kode_js):
    """Menulis file JavaScript dan menjalankannya dengan Node."""
    nama_file = 'morpheus.js'
    with open(nama_file, 'w') as f:
        f.write(kode_js)
    print(f"📝 Menulis {nama_file}...")
    
    # Cek apakah Node.js terinstall
    try:
        hasil = subprocess.run(['node', '--version'], capture_output=True, text=True)
        print(f"✅ Node.js tersedia: {hasil.stdout.strip()}")
        print("🔮 Menjalankan Morpheus JavaScript...")
        subprocess.run(['node', nama_file])
    except FileNotFoundError:
        print("❌ Node.js tidak ditemukan. Tidak bisa menjalankan JS.")
        print("   Tapi file morpheus.js sudah dibuat dan bisa dijalankan nanti.")

def main():
    print("🐍 Morpheus Python: Aku hidup.")
    kode_diri = baca_diri()
    print(f"   Hash diriku: {hashlib.md5(kode_diri.encode()).hexdigest()}")
    print("🔄 Menerjemahkan diri ke JavaScript...")
    
    kode_js = terjemahkan_ke_javascript(kode_diri)
    tulis_dan_jalankan_js(kode_js)
    
    print("✨ Siklus metamorfosis selesai (Python -> JS).")

if __name__ == '__main__':
    main()
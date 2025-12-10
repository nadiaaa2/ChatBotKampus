from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# ====== RULES CHATBOT ======
rules = {
    r"(jam|waktu) kuliah": "Jam kuliah dimulai pukul 08.30 – 21.00.",
    r"(jadwal|schedule) (kuliah|kelas)": "Cek jadwal kuliah melalui Simak & Siakad kampus.",
    r"(lokasi|dimana) ruang administrasi": "Ruang administrasi di Gedung A lantai 2.",
    r"(cara|bagaimana) daftar ulang": "Daftar ulang dilakukan melalui Simak menu Registrasi.",
    r"(syarat|berkas) krs": "Syarat KRS: bayar UKT & tidak ada tunggakan.",
    r"(wifi|internet) kampus": "Akun WiFi: gunakan NIM & password tanggal lahir.",
    r"(jam|waktu) layanan administrasi": "Buka Senin–Jumat pukul 08.00–16.00.",
    r"(jadwal) ujian": "Jadwal ujian diumumkan di Simak & Siakad.",
    r"(cuti|pengajuan cuti)": "Pengajuan cuti melalui bagian administrasi.",
    r"(transkrip nilai|khs)": "KHS dapat diunduh dari Simak & Siakad.",
    r"(beasiswa)": "Informasi beasiswa ada di website & Instagram kampus.",
    r"(parkir)": "Parkir mahasiswa bisa diarea parkir P1 sampai P5.",
    r"(pmb|pendaftaran mahasiswa baru)": "PMB dilakukan melalui website resmi kampus.",
    r"(apa itu krs|pengertian krs)": "KRS adalah Kartu Rencana Studi untuk memilih mata kuliah setiap semester.",
    r"(kapan|jadwal) krs": "Pengisian KRS biasanya dibuka pada awal semester melalui Simak & Siakad.",
    r"(berapa|mak) sks (maksimal|max)": "Maksimal SKS biasanya 24, tergantung nilai IP semester sebelumnya.",
    r"(berapa|min) sks (minimal|min)": "Minimal SKS adalah 6 SKS per semester.",
    r"(ubah|ganti) krs": "Perubahan KRS bisa dilakukan selama masa revisi KRS.",
    r"(nilai|cek nilai)": "Nilai dapat dilihat melalui portal Simak & Siakad pada menu KHS.",
    r"(remidi|remedial)": "Remedial diberikan jika ada kebijakan dari dosen mata kuliah terkait.",
    r"(ujian|uts|uas) online": "UTS/UAS online mengikuti kebijakan masing-masing dosen.",
    r"(ujian susulan|susulan ujian)": "Ujian susulan dapat diajukan dengan surat keterangan resmi.",
    r"(materi ujian|cakupan ujian)": "Materi ujian berdasarkan silabus dan arahan dosen pengampu.",
    r"(alamat kampus|lokasi kampus)": "Alamat kampus berada di Jl. Perintis Kemerdekaan I No.33, RT.007/RW.003, Babakan, Cikokol, Kec. Tangerang, Kota Tangerang, Banten 15118.",
    r"(nomor telepon kampus|kontak kampus)": "Nomor telepon kampus: 62 81320663294.",
    r"(rektor|nama rektor)": "Rektor saat ini adalah  Dr. H. Desri Arwen, M.Pd.",
    r"(maks|batas) cuti": "Mahasiswa dapat mengambil cuti maksimal 4 semester selama studi.",
    r"(lama studi|masa studi)": "Masa studi maksimal program S1 adalah 14 semester.",
    r"(reset password|lupa password)": "Reset password dapat dilakukan melalui menu Lupa Password di Simak & Siakad.",
    r"(email mahasiswa|akun email)": "Akun email mahasiswa menggunakan format NIM@student.kampus.ac.id.",
    r"(siakad error|tidak bisa login)": "Jika Siakad error, coba bersihkan cache browser atau hubungi admin TI.",
    r"(cicilan ukt|angsuran ukt)": "Cicilan UKT dapat diajukan melalui bagian keuangan.",
    r"(beasiswa internal|beasiswa kampus)": "Beasiswa internal tersedia setiap semester melalui Biro Akademik.",
    r"(syarat beasiswa)": "Syarat beasiswa: IPK minimal 3.0 dan tidak memiliki tunggakan.",
    r"(perpustakaan|jam perpustakaan)": "Perpustakaan buka Senin–Jumat pukul 08.00–17.00.",
    r"(pinjam buku|peminjaman buku)": "Peminjaman buku maksimal 7 hari dan dapat diperpanjang.",
    r"(lab komputer|laboratorium komputer)": "Lab komputer berada di Gedung C lantai 17.",
    r"(kantin|makan di kampus)": "Kantin kampus buka pukul 08.00–20.00.",
    r"(parkir motor|parkir mobil)": "Parkir motor di Gedung B, parkir mobil di area belakang kampus.",
    r"(ukm|unit kegiatan mahasiswa)": "Daftar UKM bisa dilihat di website kampus bagian Kemahasiswaan.",
    r"(organisasi mahasiswa|ormawa)": "ORMawa meliputi BEM, IMM dan himpunan fakultas lainnya.",
    r"(pendaftaran ukm|join ukm)": "Buka pendaftaran UKM setiap awal semester.",
}

def get_reply(text):
    text = text.lower()
    for pattern, response in rules.items():
        if re.search(pattern, text):
            return response
    return "Maaf, saya tidak memahami pertanyaan Anda."


# ===== ROUTES =====
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json["message"]
    bot_reply = get_reply(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
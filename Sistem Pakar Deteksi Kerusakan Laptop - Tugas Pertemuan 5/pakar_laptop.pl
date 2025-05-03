:- dynamic gejala_pos/1.

% Pertanyaan untuk tiap gejala
pertanyaan(tidak_menyala, "Apakah laptop tidak bisa dinyalakan?").
pertanyaan(sering_restart, "Apakah laptop sering mati atau restart sendiri?").
pertanyaan(overheat, "Apakah laptop terasa sangat panas saat digunakan?").
pertanyaan(lambat, "Apakah laptop sangat lambat saat digunakan?").
pertanyaan(layar_gelap, "Apakah layar tidak menampilkan apa-apa atau hanya hitam?").
pertanyaan(garis_di_layar, "Apakah ada garis-garis aneh muncul di layar?").
pertanyaan(baterai_bor, "Apakah baterai laptop sangat cepat habis?").

% Deteksi kerusakan
kerusakan("Kerusakan Power Supply / Charger") :-
    gejala_pos(tidak_menyala),
    gejala_pos(baterai_bor).

kerusakan("Kerusakan Motherboard") :-
    gejala_pos(tidak_menyala),
    gejala_pos(sering_restart).

kerusakan("Masalah Overheat / Fan") :-
    gejala_pos(overheat),
    gejala_pos(sering_restart).

kerusakan("Kinerja Lambat (Harddisk/RAM)") :-
    gejala_pos(lambat),
    \+ gejala_pos(overheat).

kerusakan("Kerusakan Layar / GPU") :-
    gejala_pos(layar_gelap);
    gejala_pos(garis_di_layar).

kerusakan("Tidak terdeteksi") :-
    \+ gejala_pos(_).

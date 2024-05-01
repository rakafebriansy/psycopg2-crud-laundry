CREATE TABLE paket (
	id SERIAL PRIMARY KEY,
	jenis VARCHAR(60) NOT NULL,
	harga INT NOT NULL
);
CREATE TABLE karyawan (
	id SERIAL PRIMARY KEY,
	nama VARCHAR(60) NOT NULL,
	no_telp VARCHAR(15) UNIQUE
);
CREATE TABLE transaksi (
	id serial PRIMARY KEY,
	tanggal_transaksi DATE NOT NULL DEFAULT CURRENT_DATE,
	nama_pelanggan VARCHAR(60) NOT NULL,
	no_telp_pelanggan VARCHAR(60) NOT NULL,
	id_paket INT NOT NULL,
	id_karyawan INT NOT NULL,
	CONSTRAINT fk_paket_transaksi FOREIGN KEY (id_paket) REFERENCES paket(id),
	CONSTRAINT fk_karyawan_transaksi FOREIGN KEY (id_karyawan) REFERENCES karyawan(id)
);
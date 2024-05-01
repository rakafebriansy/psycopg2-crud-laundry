CREATE TABLE pelanggan (
	id SERIAL PRIMARY KEY,
	nama VARCHAR(60) NOT NULL,
	nomor_telepon VARCHAR(15) NOT NULL UNIQUE
);
CREATE TABLE paket (
	id SERIAL PRIMARY KEY,
	jenis_paket VARCHAR(60) NOT NULL,
	harga INT NOT NULL
);
CREATE TABLE karyawan (
	id SERIAL PRIMARY KEY,
	nama VARCHAR(60) NOT NULL,
	nomor_telepon VARCHAR(15) UNIQUE
);
CREATE TABLE transaksi (
	id serial PRIMARY KEY,
	tanggal_transaksi DATE NOT NULL DEFAULT CURRENT_DATE,
	id_paket INT,
	id_pelanggan INT,
	id_karyawan INT,
	CONSTRAINT fk_paket_transaksi FOREIGN KEY (id_paket) REFERENCES paket(id),
	CONSTRAINT fk_pelanggan_transaksi FOREIGN KEY (id_pelanggan) REFERENCES pelanggan(id),
	CONSTRAINT fk_karyawan_transaksi FOREIGN KEY (id_karyawan) REFERENCES karyawan(id)
);
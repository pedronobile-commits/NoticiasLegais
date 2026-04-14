CREATE DATABASE IF NOT EXISTS noticias_db;

USE noticias_db;

CREATE TABLE IF NOT EXISTS usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS categorias(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS noticias(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    data_publicacao DATETIME NOT NULL,
    autor VARCHAR(255) NOT NULL,
    fonte VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    conteudo VARCHAR(500) NOT NULL,
    imagem LONGBLOB NOT NULL
);

CREATE TABLE IF NOT EXISTS favoritas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    noticia_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (noticia_id) REFERENCES noticias(id) ON DELETE CASCADE,
    UNIQUE KEY unique_favorita (usuario_id, noticia_id)
);


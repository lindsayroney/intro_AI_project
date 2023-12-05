File imagemDestino = new File(diretorioImagens, nomeImagem);
Files.copy(imagemOrigem.toPath(), imagemDestino.toPath());

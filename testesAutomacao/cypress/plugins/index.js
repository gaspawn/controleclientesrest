/// <reference types="cypress" />

const fs = require('fs-extra');   //node File System - permite ler arquivos, dentre outros
const path = require('path');  // modulo do node para resolver caminhos

function buscarArquivoDeConfig(arquivo){
  const caminhoDoArquivo = path.resolve('.', 'cypress', 'config', `${arquivo}.json`);  //cria o caminho até o arquivo de config criado (que pode ser escolhido no parametro)
  return fs.readJson(caminhoDoArquivo);  // lê o arquivo nesse caminho
}


/**
 * 
 */
// eslint-disable-next-line no-unused-vars
module.exports = (on, config) => {
  const arquivo = config.env.configFile || 'dev'; //associa o que será passado em configFile via linha de comando, e define, um valor padrão
  require('cypress-mochawesome-reporter/plugin')(on); 
  return buscarArquivoDeConfig(arquivo);
}

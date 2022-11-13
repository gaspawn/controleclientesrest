/// <reference types="cypress" />

//imports:
import { faker } from '@faker-js/faker'
import Factory from '../fixtures/factory'

//lista de variáveis para path:
const URL_PESSOAS = '/pessoas/'


describe('Casos de teste da API desenvolvida no PI3', ()=>{

    it('Deve retornar a listagem das pessoas cadastradas', ()=>{
        cy.restNoAuth('GET', URL_PESSOAS).then(res=>{
            expect(res.status).to.be.eq(200);
            expect(res.body.length).to.be.greaterThan(0);
            cy.writeFile('cypress/fixtures/usersList.json', res.body); //salvando num json a lista de usuários retornada
            cy.contractValidation(res, 'get_pessoas', 200);
            cy.log(JSON.stringify(res.body))
        })
    })

    it('Deve cadastrar nova pessoa com sucesso', ()=>{
        let pessoa = Factory.gerarUsuario();
        cy.restNoAuth('POST', URL_PESSOAS, pessoa).then(res=>{
            cy.log(JSON.stringify(res.body))
            expect(res.status).to.be.eq(201);
            expect(res.body).to.haveOwnProperty('id');
            cy.writeFile('cypress/fixtures/lastUserPosted.json', res.body)
            cy.contractValidation(res, 'post_pessoas', 201)
        })
    })

    it('Deve buscar uma pessoa cadastrada', ()=>{
        cy.fixture('lastUserPosted.json').then(pessoa =>{
            let id = pessoa.id;
            cy.restNoAuth('GET', URL_PESSOAS+id).then(res =>{
                expect(res.status).to.be.eq(200);
                expect(res.body.id).to.be.eq(id);
                cy.contractValidation(res, 'get_pessoa_id', 200)
            })
        })
    })

    it('Deve alterar os dados de uma pessoa cadastrada', ()=>{
        cy.fixture('lastUserPosted.json').then(pessoa =>{
            let id = pessoa.id;
            let novaPessoa = pessoa;
            novaPessoa.last_name = pessoa.last_name + ' >> ALT <<';
            cy.restNoAuth('PUT', URL_PESSOAS+id+'/', novaPessoa).then(res =>{
                expect(res.status).to.be.eq(200)
                cy.contractValidation(res, 'put_pessoa_id', 200)
                cy.log(JSON.stringify(res.body))
                cy.writeFile('cypress/fixtures/lastUserPosted.json', res.body)
            })
        })
    })

    it('Deve deletar um usuário cadastrado', ()=>{
        cy.fixture('lastUserPosted.json').then(pessoa=>{
            let id = pessoa.id;
            cy.restNoAuth('DELETE', URL_PESSOAS+id+'/').then(res=>{
                expect(res.status).to.be.eq(204);
                cy.writeFile('cypress/fixtures/lastUserPosted.json', ' ')
            })
        })
    })
    



})
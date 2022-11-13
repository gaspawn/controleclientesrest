import Ajv from 'ajv'
const ajv = new Ajv({allErrors: true, verbose: true, strict: false})

//Já vou deixar esse comando aqui, pq acho que não vai mudar mto

Cypress.Commands.add('contractValidation', (res, schema, status)=>{   //validar esquemas com AJV
    cy.fixture(`schemas/${schema}/${status}.json`).then( schema => {
        const validate = ajv.compile(schema)       
        const valid = validate(res.body)

        //cy.log(JSON.stringify(validate.errors));
        if(!valid){
            var errors = ''
            for (let i in validate.errors){
                let err = validate.errors[i];
                errors += `\n ${err.instancePath} ${err.message}, but received a ${typeof err.data}`
                throw new Error('Erros encontrados na validação de contrato, por favor verifique: '+ errors)
            }
        }   else { cy.log('Contrato válido')}
    })
})


Cypress.Commands.add('rest', (method='GET', url='/', body=null, token=null, failOnStatusCode=false) => {
    return cy.request({
        method: method,
        url: url,
        failOnStatusCode: failOnStatusCode,
        body: body,
        auth: {                     //Atenção para o formato da autenticação 
            bearer: Cypress.env('token')
        }
    })
})

Cypress.Commands.add('restNoAuth', (method='GET', url='/', body=null, failOnStatusCode=false) => {
    return cy.request({
        method: method,
        url: url,
        failOnStatusCode: failOnStatusCode,
        body: body
    })
})


//imports
import { faker } from '@faker-js/faker';
import { generate } from 'gerador-validador-cpf'


//Aqui vamos utilizar a faker-js para produzer dados aleatórios
//e a lib de geração de CPF

export default class Factory {

    static gerarUsuario(){
        return {
            "username": faker.internet.userName(),
            "cpf": generate(),
            "first_name": faker.name.firstName(),
            "last_name": faker.name.lastName(),
            "endereco": faker.address.streetAddress(),
            "nascimento": JSON.stringify(faker.date.past()).slice(1, 11),
            "telefone": faker.phone.number('###########'),
            "email": faker.internet.email(),
            "is_atendente": faker.datatype.boolean(),
            "is_gerente": faker.datatype.boolean(),
            "new_password": faker.internet.password()
        }
    }


       

}
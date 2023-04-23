import axios from "axios";

let model: any = {};

function SetModel(input: any) {
    model = input;
}

const data = {
    isAdmin: false,
};

async function MethodLogin(login: string, password: string) {
    console.log(login);
    console.log(password);
}

async function MethodRegistration(name: string, lastname: string, login: string, password: string) {
    console.log(name);
    console.log(lastname);
    console.log(login);
    console.log(password);
}

const method = {
    login: MethodLogin,
    registration: MethodRegistration,
  };
  
  export { SetModel, data, method };
import * as auth from "../api/authApi";

let model: any = {};

function SetModel(input: any) {
    model = input;
}

const data = {
    isAdmin: false as boolean | null,
    authorized: false,
    firstName: '' as string | null,
    lastName: '' as string | null,
    login: '' as string | null,
};

async function MethodLogin(login: string, password: string) {
    try {
        const response = await auth.login(login, password);
        localStorage.setItem('auth_token', response[0].auth_token);
        localStorage.setItem('login', login);
        localStorage.setItem('firstName', response[1].first_name);
        localStorage.setItem('lastName', response[2].last_name);
        localStorage.setItem('isAdmin', response[3].is_superuser);
        MethodGetInfo();
    } catch (err: any) {
        throw new Error('Неверно введён логин или пароль');
    }
}

async function MethodRegistration(name: string, lastname: string, login: string, password: string) {
    const response = await auth.registration(name, lastname, login, password);
    if (response.response === true) {
        await MethodLogin(login, password);
    } else if (response.username.length > 0) {
        throw new Error('Ползователь с таким логином уже существует')
    }
}

async function  MethodLogout() {
    data.authorized = false;
    data.isAdmin = false;
    data.firstName = '';
    data.lastName = '';
    data.login = '';
    MethodRemoveInfo();
}

async function MethodGetInfo() {
    if (localStorage.getItem('auth_token') !== null) {
        data.login = localStorage.getItem('login');
        data.firstName = localStorage.getItem('firstName');
        data.lastName = localStorage.getItem('lastName');
        data.isAdmin = localStorage.getItem('isAdmin') === "true";
        data.authorized = true;
    }
}

async function MethodRemoveInfo() {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('login');
    localStorage.removeItem('firstName');
    localStorage.removeItem('lastName');
    localStorage.removeItem('isAdmin');
}

const method = {
    login: MethodLogin,
    registration: MethodRegistration,
    logout: MethodLogout,
    getInfo: MethodGetInfo,
    removeInfo: MethodRemoveInfo,
};

export { SetModel, data, method };
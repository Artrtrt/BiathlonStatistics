import axios from "axios";

async function login(login: string, password: string) {
  const bodyFormData = new FormData();
  bodyFormData.append("username", login);
  bodyFormData.append("password", password);
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/login/",
      bodyFormData
    );
    return response.data;
  } catch (err) {
    throw new Error("Ошибка при авторизации");
  }
}

async function registration(
  name: string,
  lastname: string,
  login: string,
  password: string
) {
  const bodyFormData = new FormData();
  bodyFormData.append("username", login);
  bodyFormData.append("password", password);
  bodyFormData.append("first_name", name);
  bodyFormData.append("last_name", lastname);
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/registration/",
      bodyFormData
    );
    return response.data;
  } catch (err) {
    throw new Error("Ошибка при авторизации");
  }
}

export { login, registration };

import axios from "axios";

async function fetchMessageList() {
  try {
    const chatList = await axios.get("http://127.0.0.1:8000/all_chat/");
    return chatList.data;
  } catch (err) {
    throw new Error("Ошибка при получении сообщений");
  }
}

async function sendMessage(message: string, login: string, token: string) {
  const bodyFormData = new FormData();
  bodyFormData.append("message", message);
  bodyFormData.append("login", login);
  try {
    await axios.post("http://127.0.0.1:8000/add_message/", bodyFormData, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
  } catch (err) {
    throw new Error("Ошибка при отправке сообщения");
  }
}

export { fetchMessageList, sendMessage };

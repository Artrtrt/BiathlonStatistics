import * as chatApi from "../api/chatApi";
import * as model from "@/module/model";

type MessageUnit = {
  message: string;
  login: string;
};

const data = {
  messageList: [] as MessageUnit[],
};

async function MethodImport() {
  const response = await chatApi.fetchMessageList();
  response.forEach((message: MessageUnit) => {
    data.messageList.push(message);
  });
}

async function MethodSendMessage(message: string) {
  data.messageList.push({ message, login: model.data.auth.login as string });
  await chatApi.sendMessage(
    message,
    model.data.auth.login as string,
    localStorage.getItem("auth_token") as string
  );
}

const method = {
  import: MethodImport,
  sendMessage: MethodSendMessage,
};

export { data, method };

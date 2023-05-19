import * as app from "./model/app";
import * as auth from "./model/auth";
import * as chat from "./model/chat";

const data = {
  app: app.data,
  auth: auth.data,
  chat: chat.data,
};

const method = {
  app: app.method,
  auth: auth.method,
  chat: chat.method,
};

const model = {
  data,
  method,
  chat,
};

export { data, method };

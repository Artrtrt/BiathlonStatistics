import * as app from "./model/app";
import * as auth from "./model/auth";

const data = {
  app: app.data,
  auth: auth.data,
};

const method = {
  app: app.method,
  auth: auth.method,
};

const model = {
  data,
  method,
};

app.SetModel(model);
auth.SetModel(model);

export { data, method };

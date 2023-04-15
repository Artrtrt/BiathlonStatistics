import * as app from "./model/app";

const data = {
  app: app.data,
};

const method = {
  app: app.method,
};

const model = {
  data,
  method,
};

app.SetModel(model);

export { data, method };

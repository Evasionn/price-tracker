const { useState } = React;
const request = async (url, data = {}, method = "POST") => {
  const response = await fetch(url, {
    method,
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
};

const FAIL_MESSAGE =
  "Something went wrong. Application settings couldn't be saved.";
const SUCCESS_MESSAGE = "Application settings has been saved successfully.";

const EMPTY_FIELD_MESSAGE = "There are some empty fields.";

const LOGIN_ATTEMPT_FAILED =
  "SMTP Login is failed. Please check sender gmail address and password.";

const LOGIN_ATTEMPT_SUCCESSFUL =
  "SMTP Login is successful. You can save and use this configuration.";

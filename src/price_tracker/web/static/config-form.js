const ConfigForm = (config) => {
  const [configValues, setConfigValues] = useState(
    JSON.parse(config.replaceAll("&#39;", '"'))
  );
  const handleRemove = () => {
    request("/config", {}, "DELETE")
      .then((r) => {
        if (r.status === 200) {
          setConfigValues({
            sender_gmail: "",
            gmail_password: "",
            receiver_email: "",
          });
          alert(SUCCESS_MESSAGE);
        } else alert(FAIL_MESSAGE);
      })
      .catch(() => alert(FAIL_MESSAGE));
  };

  const handleOnChange = (e) => {
    setConfigValues({ ...configValues, [e.target.name]: e.target.value });
  };

  const checkEmptyField = () => {
    let isValid = true;
    Object.keys(configValues).forEach((key) => {
      if (configValues[key] === "") isValid = false;
    });
    if (!isValid) {
      alert(EMPTY_FIELD_MESSAGE);
      return;
    }
    return isValid;
  };

  const handleSave = () => {
    if (!checkEmptyField()) return;
    request("/config", configValues, "PUT")
      .then((r) => {
        if (r.status === 200) alert(SUCCESS_MESSAGE);
        else alert(FAIL_MESSAGE);
      })
      .catch(() => alert(FAIL_MESSAGE));
  };

  const handleSmtpLogin = () => {
    if (!checkEmptyField()) return;
    request(
      "/check-login",
      {
        email: configValues["sender_gmail"],
        password: configValues["gmail_password"],
      },
      "POST"
    )
      .then((r) => {
        if (r.status === 200) alert(LOGIN_ATTEMPT_SUCCESSFUL);
        else alert(LOGIN_ATTEMPT_FAILED);
      })
      .catch(() => alert(LOGIN_ATTEMPT_FAILED));
  };

  return (
    <React.Fragment>
      <h1>Config</h1>

      <div>
        <label>
          Sender gmail:
          <input
            type="text"
            name="sender_gmail"
            value={configValues.sender_gmail}
            onChange={handleOnChange}
          />
        </label>
      </div>
      <div>
        <label>
          Gmail password:
          <input
            type="password"
            name="gmail_password"
            value={configValues.gmail_password}
            onChange={handleOnChange}
          />
        </label>
      </div>
      <div>
        <label>
          Receiver email:
          <input
            type="text"
            name="receiver_email"
            value={configValues.receiver_email}
            onChange={handleOnChange}
          />
        </label>
      </div>
      <div>
        <input type="button" value="Save" onClick={handleSave} />
        <input type="button" value="Delete" onClick={handleRemove} />
        <input type="button" value="Try SMTP Login" onClick={handleSmtpLogin} />
      </div>
    </React.Fragment>
  );
};

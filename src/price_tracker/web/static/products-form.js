const ProductsForm = (products) => {
  const [productList, setProductList] = useState([
    ...JSON.parse(products.replaceAll("&#39;", '"')),
    {}, // add an empty row
  ]);

  const handleRemove = (index) => {
    productList.splice(index, 1);

    setProductList([...productList]);
  };

  const handleAddRow = () => {
    setProductList([...productList, {}]);
  };

  const handleOnChange = (e, index) => {
    productList[index][e.target.name] = e.target.value;
    setProductList([...productList]);
  };

  const handleSave = () => {
    let isValid = true;
    productList.forEach((item) => {
      if (item.url === "" || item.warn_price === "") isValid = false;
    });

    if (!isValid) {
      alert(EMPTY_FIELD_MESSAGE);
      return;
    }

    request("/products", productList, "PUT")
      .then((r) => {
        if (r.status === 200) alert(SUCCESS_MESSAGE);
        else alert(FAIL_MESSAGE);
      })
      .catch(() => alert(FAIL_MESSAGE));
  };

  const handleRemoveAll = () => {
    request("/products", {}, "DELETE")
      .then((r) => {
        if (r.status === 200) {
          setProductList([{ url: "", warn_price: "" }]);
          alert(SUCCESS_MESSAGE);
        } else alert(FAIL_MESSAGE);
      })
      .catch(() => alert(FAIL_MESSAGE));
  };

  return (
    <React.Fragment>
      <h1>Products</h1>
      <form>
        {productList.map((item, index) => {
          const { url, warn_price } = item;
          return (
            <div key={index}>
              <label>
                Url:
                <input
                  type="text"
                  name="url"
                  value={url}
                  onChange={(e) => handleOnChange(e, index)}
                />
              </label>
              <label>
                Warn Price:
                <input
                  type="number"
                  name="warn_price"
                  value={warn_price}
                  placeholder="0.00"
                  pattern="^\d+(?:\.\d{1,2})?$"
                  onChange={(e) => handleOnChange(e, index)}
                />
              </label>
              <input
                type="button"
                onClick={() => handleRemove(index)}
                value="Remove"
                class="ml"
              />
            </div>
          );
        })}

        <div>
          <input type="button" value="Save" onClick={handleSave} />
          <input
            type="button"
            value="Delete"
            class="ml"
            onClick={handleRemoveAll}
          />
          <input
            type="button"
            value="Add row"
            onClick={handleAddRow}
            class="ml"
          />
        </div>
      </form>
    </React.Fragment>
  );
};

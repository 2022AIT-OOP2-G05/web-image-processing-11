class Main {
  constructor() {
    this.form = document.getElementById("form");
    this.fileInput = document.getElementById("file-input");
    this._configure();
  }

  _submitHandler(e) {
    e.preventDefault();
    this._postImg();
  }

  _configure() {
    this.form.addEventListener("submit", this._submitHandler.bind(this));
  }

  async _postImg() {
    const formData = new FormData(this.form);
    const fileInput = document.getElementById("file-input");

    formData.append("file", fileInput.files[0]);

    try {
      if (fileInput.files[0]) {
        await fetch("/upload", {
          method: "POST",
          body: formData,
        });
        fileInput.value = "";
      }
    } catch (err) {
      console.log(err);
    }
  }
}

new Main();

import { fetchBase } from "./utils/fetch.js";

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

    if (fileInput.value) {
      await fetchBase.fetch("/upload", "POST", formData);
      fileInput.value = "";
    }
  }
}

new Main();
